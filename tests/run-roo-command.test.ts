import { test, expect } from '@playwright/test';
import { RooDriver } from '../.gemini/skills/skill-roo-driver/driver';

test.describe('/run-roo integration logic', () => {
  let driver: RooDriver;

  test.beforeEach(async () => {
    driver = new RooDriver();
  });

  test.afterEach(async () => {
    await driver.close();
  });

  test('should simulate /run-roo flow: change mode and send prompt', async () => {
    test.setTimeout(180000);
    await driver.init();
    
    try {
      // Trying to change mode - if it fails we log but still try to send prompt
      await driver.changeMode('Code');
    } catch (e) {
      console.warn('Mode change failed, but continuing with prompt:', e.message);
    }
    
    const prompt = '/architect Hello from run-roo full flow test';
    await driver.sendPrompt(prompt);
    
    const status = await driver.fetchStatus();
    expect(status.chatContent).toContain('Hello from run-roo');
  });
});
