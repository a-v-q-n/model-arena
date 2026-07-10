import { chromium } from "playwright";

const [url, output] = process.argv.slice(2);
if (!url || !output) {
  console.error("Usage: node screenshot.mjs <url> <output.png>");
  process.exit(1);
}

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
await page.goto(url, { waitUntil: "networkidle", timeout: 15000 });
await page.screenshot({ path: output, fullPage: true });
await browser.close();
