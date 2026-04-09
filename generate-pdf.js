const { chromium } = require('playwright');
const path = require('path');

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    const filePath = 'file://' + path.resolve(__dirname, 'index.html');
    
    await page.goto(filePath, { waitUntil: 'networkidle' });
    
    await page.evaluate(() => {
        document.documentElement.setAttribute('data-theme', 'light');
    });

    await page.pdf({
        path: path.join(__dirname, 'MathewFleischResume.pdf'),
        format: 'Letter',
        printBackground: true,
        margin: {
            top: '0.4in',
            right: '0.4in',
            bottom: '0.4in',
            left: '0.4in'
        }
    });

    await browser.close();
    console.log('PDF generated successfully as MathewFleischResume.pdf');
})();
