import { test, expect } from '@playwright/test';
import { RooDriver } from '../.gemini/skills/skill-roo-driver/driver';
import * as dotenv from 'dotenv';

dotenv.config();

test.describe('RooDriver E2E Tests', () => {
  let driver: RooDriver;

  test.beforeEach(async () => {
    driver = new RooDriver();
  });

  test.afterEach(async () => {
    await driver.close();
  });

  test('should connect to VS Code Server and focus Roo Code', async () => {
    test.setTimeout(90000); // Extended timeout
    await driver.init();
    const status = await driver.fetchStatus();
    expect(status).toBeDefined();
    expect(status.screenshotPath).toContain('.ops/roo_driver_logs/');
  });

  test('should be able to get chat content', async () => {
    test.setTimeout(90000);
    await driver.init();
    const status = await driver.fetchStatus();
    expect(typeof status.chatContent).toBe('string');
  });

  test('should be able to change Roo Code mode', async () => {
    test.setTimeout(90000);
    await driver.init();
    await driver.changeMode('Architect');
    const status = await driver.fetchStatus();
    expect(status).toBeDefined();
  });

  test('should be able to send a prompt', async () => {
    test.setTimeout(90000);
    await driver.init();
    await driver.sendPrompt('Hello, this is a test from Playwright.');
    const status = await driver.fetchStatus();
    expect(status).toBeDefined();
  });
});
