const puppeteer = require('puppeteer');
require('dotenv').config();
(async () => {
  const url = 'https://facebook.com';
  const user = process.env.USER;
  const password = process.env.PASSWORD;
  const browserOptions = {
    headless: false,
    defaultViewport: null,
    args: ['--start-maximized'],
  };
  const browser = await puppeteer.launch(browserOptions);
  const page = await browser.newPage();
  await page.goto(url);
  await page.type('#email', user);
  await page.type('#pass', password);
  await page.$eval('#login_form', (form) => form.submit());
  await page.screenshot({ path: 'example.png' });
  // await browser.close();
})();
