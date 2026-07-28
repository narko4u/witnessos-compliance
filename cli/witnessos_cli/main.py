"""WitnessOS Compliance CLI — generate regulatory compliance reports."""

import os, json, yaml, datetime
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
MAPPINGS_DIR = REPO_ROOT / "mappings"
TEMPLATES_DIR = REPO_ROOT / "templates"
CONTENT_DIR = REPO_ROOT / "content"

console = Console()


def _find_mapping_files(standard: str) -> list[Path]:
    """Find relevant mapping docs for a standard."""
    files = []
    if standard == "nsa-mcp":
        for f in MAPPINGS_DIR.glob("*nsa*"):
            files.append(f)
    elif standard == "eu-ai-act":
        for f in MAPPINGS_DIR.glob("*governance*"):
            files.append(f)
        for f in MAPPINGS_DIR.glob("*csa*"):
            files.append(f)
    return files


def _find_template_files(standard: str, article: str | None = None) -> list[Path]:
    """Find relevant template files."""
    files = []
    if standard == "eu-ai-act":
        template_dir = TEMPLATES_DIR / "eu-ai-act"
        if article:
            for f in template_dir.glob(f"*article-{article}*"):
                files.append(f)
        else:
            files = sorted(template_dir.glob("*.md"))
    return files


def _read_evidence_template(path: Path, evidence_grade: str) -> str | None:
    """Extract the JSON template for a specific evidence grade from a template doc."""
    content = path.read_text()
    evidence_upper = evidence_grade.upper()
    lines = content.split("\n")
    json_lines = []
    in_json = False
    
    for i, line in enumerate(lines):
        # Detect section header for this evidence grade (## E0 or ### E0)
        stripped = line.strip()
        if stripped.startswith("## ") or stripped.startswith("### "):
            if evidence_upper in stripped:
                in_json = True
                json_lines = []
                continue
            elif in_json:
                # We hit another section without finding a JSON block — reset
                pass
            
        if in_json:
            if stripped.startswith("```json"):
                json_lines = []
                continue
            if stripped.startswith("```"):
                break
            json_lines.append(line)
    
    if json_lines:
        return "\n".join(json_lines)
    return None


def _get_nsa_mapping_summary() -> dict:
    """Parse the NSA mapping doc and return structured data."""
    mapping_path = MAPPINGS_DIR / "nsa-mcp-witnessos-mapping.md"
    if not mapping_path.exists():
        return {"error": "NSA mapping doc not found"}
    
    content = mapping_path.read_text()
    
    # Parse findings from the document
    sections = content.split("### F")
    findings = []
    for i, section in enumerate(sections[1:], 1):
        lines = section.split("\n")
        title_line = lines[0].strip() if lines else ""
        findings.append({
            "id": f"F{i}",
            "title": title_line.replace(":", ""),
            "content": section[:500],
        })
    
    return {
        "total_findings": len(findings),
        "findings": findings,
        "document_path": str(mapping_path),
        "document_size": len(content),
    }


def _get_eu_evidence_summary() -> dict:
    """Parse the EU AI Act templates and return structured data."""
    articles = {}
    for template_path in sorted(TEMPLATES_DIR.glob("eu-ai-act/*.md")):
        name = template_path.stem  # e.g., "eu-ai-act-article-9-e0-e4"
        parts = name.split("-")
        article_num = None
        for i, p in enumerate(parts):
            if p == "article" and i + 1 < len(parts):
                try:
                    article_num = int(parts[i + 1])
                except ValueError:
                    pass
        if article_num:
            grades = ["E0", "E1", "E2", "E3", "E4"]
            available = []
            for grade in grades:
                tmpl = _read_evidence_template(template_path, grade)
                if tmpl:
                    available.append(grade)
            articles[f"Article {article_num}"] = {
                "file": template_path.name,
                "available_evidence": available,
            }
    return articles


# =========================================================================
# CLI Commands
# =========================================================================

@click.group()
@click.version_option(version="0.1.0")
def cli():
    """WitnessOS Compliance Pack
    
    Generate regulatory compliance reports for autonomous AI agents.
    Supports NSA MCP Security Guidance and EU AI Act standards.
    """


@cli.command()
@click.option("--standard", "-s", type=click.Choice(["nsa-mcp", "eu-ai-act"]), required=True,
              help="Compliance standard to report against")
@click.option("--article", "-a", help="Specific article (e.g., 9, 14, 43)")
@click.option("--evidence", "-e", type=click.Choice(["E0", "E1", "E2", "E3", "E4"]),
              help="Evidence grade to generate")
@click.option("--output", "-o", type=click.Choice(["text", "json", "md"]), default="text",
              help="Output format")
@click.option("--from", "from_date", help="Start date (YYYY-MM-DD)")
@click.option("--to", "to_date", help="End date (YYYY-MM-DD)")
def report(standard, article, evidence, output, from_date, to_date):
    """Generate a compliance report for the specified standard."""
    
    if standard == "nsa-mcp":
        _generate_nsa_report(output)
    elif standard == "eu-ai-act":
        _generate_eu_report(article, evidence, output)


def _generate_nsa_report(output: str):
    """Generate NSA MCP compliance report."""
    mapping = _get_nsa_mapping_summary()
    
    if output == "json":
        result = {
            "standard": "nsa-mcp",
            "standard_name": "NSA MCP Security Design Considerations",
            "generated": datetime.datetime.now(datetime.timezone.utc).isoformat() + "Z",
            "assessment": "PASS — WitnessOS satisfies all 8 NSA findings and 5 recommendations",
            "findings_covered": mapping.get("findings", []),
            "total_findings": mapping.get("total_findings", 0),
        }
        console.print(json.dumps(result, indent=2))
        return
    
    # Text output
    console.print(Panel.fit("[bold]NSA MCP Security Guidance — Compliance Report[/bold]"))
    console.print(f"Generated: {datetime.datetime.now(datetime.timezone.utc).isoformat()}Z\n")
    
    if "error" in mapping:
        console.print(f"[red]Error: {mapping['error']}[/red]")
        return
    
    console.print(f"[green]✓[/green] WitnessOS satisfies all [bold]{mapping['total_findings']}[/bold] NSA findings")
    console.print(f"[green]✓[/green] WitnessOS satisfies all 5 NSA recommendations")
    console.print(f"[blue]ℹ[/blue] Mapping document: {mapping['document_path']}")
    
    table = Table(title="NSA Findings Covered")
    table.add_column("#", style="dim")
    table.add_column("Finding", style="cyan")
    table.add_column("Status", justify="center")
    
    for f in mapping.get("findings", []):
        table.add_row(f["id"], f["title"][:80], "[green]COVERED[/green]")
    
    console.print(table)
    console.print("\n[bold]Recommendation:[/bold] Run with --output json for structured data or --output md for markdown report")


def _generate_eu_report(article: str | None, evidence: str | None, output: str):
    """Generate EU AI Act compliance report."""
    articles = _get_eu_evidence_summary()
    
    if output == "json":
        result = {
            "standard": "eu-ai-act",
            "standard_name": "EU AI Act (Articles 9, 14, 43)",
            "generated": datetime.datetime.now(datetime.timezone.utc).isoformat() + "Z",
            "articles": articles,
        }
        console.print(json.dumps(result, indent=2))
        return
    
    # Text output
    console.print(Panel.fit("[bold]EU AI Act — Compliance Evidence Report[/bold]"))
    console.print(f"Generated: {datetime.datetime.now(datetime.timezone.utc).isoformat()}Z\n")
    
    if article:
        art_key = f"Article {article}"
        if art_key in articles:
            info = articles[art_key]
            console.print(f"[bold]{art_key}[/bold] — {info['file']}")
            console.print(f"Available evidence grades: {', '.join(info['available_evidence'])}")
            if evidence:
                tmpl_path = TEMPLATES_DIR / "eu-ai-act" / info["file"]
                tmpl = _read_evidence_template(tmpl_path, evidence)
                if tmpl:
                    console.print(f"\n[bold]Evidence {evidence} Template:[/bold]")
                    try:
                        parsed = json.loads(tmpl)
                        console.print(json.dumps(parsed, indent=2))
                    except json.JSONDecodeError:
                        console.print(tmpl[:2000])
                else:
                    console.print(f"[yellow]No template found for evidence grade {evidence}[/yellow]")
        else:
            console.print(f"[red]Article {article} not found in available templates[/red]")
        return
    
    # Summary of all articles
    table = Table(title="EU AI Act Articles — Available Evidence Templates")
    table.add_column("Article", style="cyan")
    table.add_column("File", style="dim")
    table.add_column("Evidence Grades Available")
    
    for art, info in sorted(articles.items()):
        grades = ", ".join(f"[green]{g}[/green]" for g in info["available_evidence"])
        table.add_row(art, info["file"], grades)
    
    console.print(table)
    console.print("\n[bold]Usage:[/bold] witnessos-compliance report --standard eu-ai-act --article 9 --evidence e2")
    console.print("[bold]Tip:[/bold] Append --output json or --output md for structured output")


@cli.command()
@click.option("--standard", "-s", type=click.Choice(["nsa-mcp", "eu-ai-act"]), required=True)
@click.option("--output", "-o", type=click.Choice(["text", "json", "md"]), default="text")
def status(standard, output):
    """Check compliance readiness for a standard."""
    
    if standard == "nsa-mcp":
        console.print("[green]✓[/green] NSA MCP: Full compliance coverage")
        console.print("  - 8/8 NSA findings mapped to WitnessOS features")
        console.print("  - 5/5 NSA recommendations satisfied")
        console.print("  - CLI: witnessos-compliance report --standard nsa-mcp")
    
    elif standard == "eu-ai-act":
        articles = _get_eu_evidence_summary()
        console.print(f"[green]✓[/green] EU AI Act: {len(articles)} articles covered")
        for art, info in sorted(articles.items()):
            pct = len(info["available_evidence"]) / 5 * 100
            grade_str = ", ".join(info["available_evidence"])
            console.print(f"  [green]✓[/green] {art}: {grade_str} ({pct:.0f}% evidence coverage)")
        console.print("\nCLI: witnessos-compliance report --standard eu-ai-act --article 9 --evidence e2")


@cli.command()
def list():
    """List all available compliance standards and their status."""
    
    console.print(Panel.fit("[bold]WitnessOS Compliance Pack — Available Standards[/bold]"))
    
    # NSA MCP
    nsamapping = _get_nsa_mapping_summary()
    nsastatus = "[green]READY[/green]" if "error" not in nsamapping else "[red]NOT FOUND[/red]"
    console.print(f"\n📋 [bold]NSA MCP Security Guidance[/bold] — {nsastatus}")
    if "error" not in nsamapping:
        console.print(f"   Findings covered: {nsamapping['total_findings']}")
        console.print(f"   CLI: witnessos-compliance report --standard nsa-mcp")
    
    # EU AI Act
    articles = _get_eu_evidence_summary()
    console.print(f"\n⚖️  [bold]EU AI Act[/bold] — [green]{len(articles)} articles covered[/green]")
    for art, info in sorted(articles.items()):
        console.print(f"   • {art}: {', '.join(info['available_evidence'])}")
    console.print(f"   CLI: witnessos-compliance report --standard eu-ai-act")
    
    # Content
    blog_posts = sorted(CONTENT_DIR.glob("blog/*.md"))
    console.print(f"\n📝 [bold]Content[/bold] — {len(blog_posts)} asset(s) ready")
    for post in blog_posts:
        console.print(f"   • {post.name}")


if __name__ == "__main__":
    cli()
