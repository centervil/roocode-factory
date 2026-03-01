const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  try {
    // Wait for code-server to be ready (it might take a few seconds)
    console.log('Navigating to code-server...');
    await page.goto('http://localhost:8080', { waitUntil: 'networkidle', timeout: 30000 });
    const title = await page.title();
    console.log(`Page Title: ${title}`);
    
    // code-server title is typically "code-server" or includes it
    if (title.toLowerCase().includes('code-server')) {
      console.log('SUCCESS: Playwright can access code-server UI');
    } else {
      console.log('FAILURE: Playwright cannot find code-server UI in title');
    }
  } catch (error) {
    console.error(`ERROR: ${error.message}`);
  } finally {
    await browser.close();
  }
})();
