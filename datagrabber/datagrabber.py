import asyncio
from pyppeteer import launch
import sys
import uuid
from urllib.parse import urlsplit, urlparse
import time

async def main():
    site_url = sys.argv[1]
    canary = "CANADIAN SLUT FUCKED HARD"
    browser = await launch()
    page = await browser.newPage()
    await page.goto(site_url)
    await page.focus("input[type=text]")
    await page.keyboard.type(canary)
    await page.screenshot({'path': urlparse(site_url).hostname + '-canary-typed.png'})
    await page.keyboard.press('Enter')
    await page.waitForNavigation()
    await page.screenshot({'path': urlparse(site_url).hostname + '-canary-searched.png'})
    print (site_url)
    print ("\t" + urlsplit(page.url).path + (("?" + urlsplit(page.url).query) if urlsplit(page.url).query.strip() != '' else ''))
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
