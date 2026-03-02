import { test, expect } from '@playwright/test';
import * as path from 'path';
import * as fs from 'fs';

test('debug: scan iframes in VS Code Server', async () => {
  const browser = await require('playwright').chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();
  
  const url = process.env.VSCODE_URL || 'http://localhost:8080';
  const password = process.env.VSCODE_PASSWORD || 'password';

  await page.goto(url);
  
  // Login
  const passwordInput = page.locator('input[type="password"]');
  if (await passwordInput.isVisible({ timeout: 5000 }).catch(() => false)) {
    await passwordInput.fill(password);
    await page.press('input[type="password"]', 'Enter');
  }

  await page.waitForSelector('.monaco-workbench', { timeout: 30000 });
  
  // Try to open Roo Code
  await page.keyboard.press('Control+Shift+P');
  await page.fill('.quick-input-filter input', 'Roo Code: Focus on Chat View');
  await page.keyboard.press('Enter');
  await page.waitForTimeout(5000);

  // Scan all frames
  const frames = page.frames();
  console.log(`Found ${frames.length} frames.`);
  
  const logDir = path.join(process.cwd(), '.ops/roo_driver_logs');
  if (!fs.existsSync(logDir)) fs.mkdirSync(logDir, { recursive: true });

  for (let i = 0; i < frames.length; i++) {
    const frame = frames[i];
    const name = frame.name() || `frame-${i}`;
    const url = frame.url();
    console.log(`Frame ${i}: name=${name}, url=${url}`);
    
    // Save frame content if it looks like Roo Code
    const content = await frame.content().catch(() => '');
    if (content.includes('roo') || content.includes('chat')) {
      fs.writeFileSync(path.join(logDir, `frame-${i}-content.html`), content);
      console.log(`Saved frame ${i} content.`);
    }
  }

  await page.screenshot({ path: path.join(logDir, 'debug-frames-state.png') });
  await browser.close();
});
