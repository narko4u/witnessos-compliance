const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const W = 1920, H = 1080, FPS = 30;
const DURATION = 27; // seconds
const TOTAL_FRAMES = DURATION * FPS;
const HTML_PATH = 'file://' + path.resolve(__dirname, 'rogue-agent.html');
const FRAMES_DIR = path.resolve(__dirname, 'frames');

(async () => {
  // Ensure frames dir
  if (!fs.existsSync(FRAMES_DIR)) fs.mkdirSync(FRAMES_DIR, { recursive: true });

  const browser = await puppeteer.launch({ headless: 'new', args: [`--window-size=${W},${H}`] });
  const page = await browser.newPage();
  await page.setViewport({ width: W, height: H });

  console.log(`Loading: ${HTML_PATH}`);
  await page.goto(HTML_PATH, { waitUntil: 'networkidle0', timeout: 30000 });

  // Wait for canvas to be ready
  await page.waitForSelector('canvas', { timeout: 10000 });

  console.log(`Capturing ${TOTAL_FRAMES} frames at ${FPS}fps...`);

  for (let i = 0; i < TOTAL_FRAMES; i++) {
    // Advance the animation by one frame
    await page.evaluate(() => {
      // The HTML auto-runs requestAnimationFrame — we just screenshot
      return new Promise(resolve => setTimeout(resolve, 33)); // ~1/30 s wait per frame
    });

    const fname = `frame-${String(i).padStart(5, '0')}.png`;
    await page.screenshot({ path: path.join(FRAMES_DIR, fname) });

    if (i % 30 === 0) console.log(`Frame ${i}/${TOTAL_FRAMES}`);
  }

  await browser.close();
  console.log('Done! Frames in:', FRAMES_DIR);
  process.exit(0);
})();