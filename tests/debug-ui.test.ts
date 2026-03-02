import { test, expect } from '@playwright/test';
import { RooDriver } from '../.gemini/skills/skill-roo-driver/driver';
import * as dotenv from 'dotenv';
import * as path from 'path';
import * as fs from 'fs';

dotenv.config();

test.describe('RooDriver Debugging', () => {
  let driver: RooDriver;

  test.beforeEach(async () => {
    driver = new RooDriver();
  });

  test.afterEach(async () => {
    await driver.close();
  });

  test('debug: capture current screen of VS Code Server', async () => {
    // We modify init slightly to capture steps
    // Manually executing driver steps here for visibility
    const browser = await (driver as any).chromium.launch({ headless: true });
    const context = await browser.newContext();
    const page = await context.newPage();
    
    const url = process.env.VSCODE_URL || 'http://localhost:8080';
    console.log(`Navigating to ${url}...`);
    
    await page.goto(url);
    await page.waitForTimeout(5000); // Wait for initial load
    
    const logDir = path.join(process.cwd(), '.ops/roo_driver_logs');
    if (!fs.existsSync(logDir)) fs.mkdirSync(logDir, { recursive: true });
    
    await page.screenshot({ path: path.join(logDir, 'debug-initial-load.png') });
    
    const content = await page.content();
    fs.writeFileSync(path.join(logDir, 'debug-page-content.html'), content);
    
    console.log('Saved initial screen capture and HTML to .ops/roo_driver_logs/');
    
    await browser.close();
  });
});
