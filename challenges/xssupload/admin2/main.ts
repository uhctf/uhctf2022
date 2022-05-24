import puppeteer from "puppeteer";
import { createClient } from "redis";
import { ModifierFlags, sys } from "typescript";

const FLAGS = ['uhctf{axe-the-security-with-two-xes-aka-xss-5fd9a0}', 'uhctf{f1r3-7h47-4dm1n-r16h7-n0w-46480a}'];

(async () => {

    const server_connection = createClient({
        "url": "redis://redis:6379"
    });

    await server_connection.connect();

    server_connection.on('disconnect', async () => sys.exit(1));

    interface RedisMessage {
        level: string,
        base_url: string,
        uuid: string,
    };

    server_connection.subscribe("dmca", async (msg_str: string) => {
        try {

            const msg: RedisMessage = JSON.parse(msg_str);

            const browser = await puppeteer.launch({
                args: ['--disable-dev-shm-usage', '--no-sandbox'],
            });
            const page = await browser.newPage();
            await page.goto(msg.base_url, {
                waitUntil: 'networkidle2',
                timeout: 15000
            });
            await page.setCookie({ name: "FLAG", value: FLAGS[Number.parseInt(msg.level) - 1], url: msg.base_url });
            const url = msg.base_url + "/file/" + msg.uuid;
            console.log("looking at " + url);
            await page.goto(url, {
                waitUntil: 'networkidle2',
                timeout: 15000
            });
        } catch (exception) {
            console.error("exception on dmca:");
            console.error(exception);
        }
    });

})();