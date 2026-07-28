#!/usr/bin/env python3
"""
Porgie → HF Cloud → witnessos-compliance Bridge

Pulls Porgie's discovery docs from HuggingFace cloud and commits them
to the witnessos-compliance repo in the correct directories.

Usage:
    python3 scripts/pull_porgie_docs.py              # dry run (show what would change)
    python3 scripts/pull_porgie_docs.py --commit      # actually commit and push
    python3 scripts/pull_porgie_docs.py --force       # pull even if no changes detected
"""

import os, sys, json, hashlib, subprocess
from pathlib import Path

import pyarrow.parquet as pq
import urllib.request

REPO_ROOT = Path(__file__).resolve().parent.parent
HF_DATASET = 'Narko4u/porgie-memory'
HF_PARQUET = 'data/train-00000-of-00001.parquet'
HF_URL = f'https://huggingface.co/datasets/{HF_DATASET}/resolve/main/{HF_PARQUET}'

# Mapping: Porgie's discovery topics → repo directories
TOPIC_MAP = {
    'ai-agent-governance-2026': 'mappings/',
    'csa-ai-agent-governance-gap-analysis': 'mappings/',
    'ai-agent-security-competitive-landscape': 'content/',
    'aurascape-vs-witnessos': 'content/',
}

# EU template pattern: any file with "eu" or "evidence" or "e0-e4" in name
TEMPLATE_KEYWORDS = ['eu-ai-act', 'evidence', 'e0', 'e4', 'template', 'article']

def get_hf_token():
    """Get HF token from Porgie's .env."""
    env_path = Path('/home/vault/.hermes/profiles/porgie/.env')
    if not env_path.exists():
        # Fallback: try the main .env
        env_path = Path('/home/vault/.env')
    if not env_path.exists():
        print("! No .env found for Porgie HF token", file=sys.stderr)
        sys.exit(1)
    
    for line in env_path.read_text().splitlines():
        if line.startswith('HF_TOKEN') and '=' in line:
            val = line.split('=', 1)[1].strip().strip('"').strip("'")
            if val:
                return val
    print("! HF_TOKEN not found in .env", file=sys.stderr)
    sys.exit(1)

def fetch_hf_parquet(token):
    """Fetch the HF parquet file and return list of {path, content, hash}."""
    req = urllib.request.Request(HF_URL, headers={'Authorization': f'Bearer {token}'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    
    tmp = '/tmp/porgie-bridge.parquet'
    with open(tmp, 'wb') as f:
        f.write(data)
    
    table = pq.read_table(tmp)
    docs = []
    for i in range(len(table)):
        path = table.column('path')[i].as_py()
        content = str(table.column('content')[i].as_py())
        content_hash = hashlib.sha256(content.encode()).hexdigest()[:12]
        docs.append({'path': path, 'content': content, 'hash': content_hash})
    
    os.remove(tmp)
    return docs

def classify_doc(path):
    """Determine which repo directory a discovery doc belongs in."""
    name = os.path.splitext(os.path.basename(path))[0].lower()
    
    # Check explicit topic map
    for key, dest in TOPIC_MAP.items():
        if key in name:
            return dest
    
    # Check for EU/template keywords
    for kw in TEMPLATE_KEYWORDS:
        if kw in name:
            return 'templates/eu-ai-act/'
    
    # Default to mappings
    return 'mappings/'

def get_existing_hashes():
    """Get SHA256 hashes of files already committed, by path."""
    hashes = {}
    for root, dirs, files in os.walk(REPO_ROOT):
        if '.git' in root.split(os.sep):
            continue
        for fname in files:
            if fname.endswith('.md') and fname != 'README.md':
                fpath = os.path.join(root, fname)
                rel = os.path.relpath(fpath, REPO_ROOT)
                hashes[rel] = hashlib.sha256(open(fpath, 'rb').read()).hexdigest()[:12]
    return hashes

def main():
    dry_run = '--commit' not in sys.argv
    force = '--force' in sys.argv
    
    print(f"{'DRY RUN' if dry_run else 'LIVE'} — {'force' if force else 'changes only'}\n")
    
    token = get_hf_token()
    print(f"✓ Fetched HF token")
    
    docs = fetch_hf_parquet(token)
    print(f"✓ Found {len(docs)} files in HF dataset")
    
    existing = get_existing_hashes()
    
    # Filter to discovery/journal files (skip pure reports)
    relevant = [d for d in docs if 'discoveries/' in (d['path'] or '') or 'journal/' in (d['path'] or '')]
    print(f"  → {len(relevant)} discovery/journal files")
    
    changes = []
    for doc in relevant:
        basename = os.path.basename(doc['path'])
        dest_dir = classify_doc(doc['path'])
        
        # For journal files, just save to content/ por reference
        if 'journal/' in (doc['path'] or ''):
            dest_dir = 'content/reference/'
        
        dest_path = os.path.join(REPO_ROOT, dest_dir, basename)
        rel_path = os.path.relpath(dest_path, REPO_ROOT)
        
        if os.path.exists(dest_path):
            current_hash = hashlib.sha256(open(dest_path, 'rb').read()).hexdigest()[:12]
            if current_hash == doc['hash'] and not force:
                continue  # unchanged
        
        changes.append((dest_path, rel_path, doc['content']))
    
    if not changes:
        print("\n✓ No new or changed files. Nothing to do.")
        return
    
    print(f"\n{'='*60}")
    print(f"Changes to apply ({len(changes)} files):")
    print(f"{'='*60}")
    for dest_path, rel_path, content in changes:
        size_kb = len(content) / 1024
        print(f"  📄 {rel_path}  ({size_kb:.0f}KB)")
    
    if dry_run:
        print(f"\n⚠️  Dry run — use --commit to apply")
        return
    
    # Write files
    for dest_path, rel_path, content in changes:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, 'w') as f:
            f.write(content)
        print(f"  ✓ Wrote {rel_path}")
    
    # Git commit and push
    result = subprocess.run(
        ['git', '-C', str(REPO_ROOT), 'add', '-A'],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"! Git add failed: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    
    result = subprocess.run(
        ['git', '-C', str(REPO_ROOT), 'diff', '--cached', '--quiet'],
        capture_output=True
    )
    if result.returncode == 0:
        print("\n✓ No changes to commit")
        return
    
    result = subprocess.run(
        ['git', '-C', str(REPO_ROOT), 'commit', '-m', 
         f'auto: sync Porgie discovery docs from HF ({len(changes)} files)'],
        capture_output=True, text=True
    )
    print(f"\n  {result.stdout.strip()}")
    
    result = subprocess.run(
        ['git', '-C', str(REPO_ROOT), 'push'],
        capture_output=True, text=True
    )
    print(f"  {result.stdout.strip() if result.stdout else '✓ Pushed to GitHub'}")

if __name__ == '__main__':
    main()
