const { Builder, By, Key, util } = require("selenium-webdriver");

const fs = require('fs');

let rawData = fs.readFileSync('details.JSON');

let data = JSON.parse(rawData);
console.log(data)

for (var key in data) {
    if(data.hasOwnProperty(key)) {
        var val = data[key];
        console.log(val);
    }
}

async function example() {
    let driver = await new Builder().forBrowser("firefox").build();
    await driver.get('https://www.google.com');
    await driver.findElement(By.name("q")).sendKeys("Selenium", Key.RETURN);
}

example();
// let data;

// fs.readFile('details.JSON', (err, res) => {
//     if (err) throw err;
//     data = JSON.parse(res);
//     console.log(data)
// });

// console.log(data)