import asyncio
import aiohttp
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}


async def get_detail_urls():
    url_main = 'https://www.biquge7.xyz/50416'

    async with aiohttp.ClientSession() as session:
        async with await session.get(url_main, headers=headers) as resp:
            resp_text = await resp.text()
            tree = etree.HTML(resp_text)
            a_link = tree.xpath('//div[@class="list"]//a/@href')
            url_list = ['https://www.biquge7.xyz' + item for item in a_link]
            return url_list


async def get_content(url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as resp:
            resp_text = await resp.text()
            title = parse_content(resp_text)
            print(title)


def parse_content(response):
    tree = etree.HTML(response)
    title = tree.xpath('//div[@class="list list_text"]/h1/text()')[0]
    return title


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    urls = loop.run_until_complete(get_detail_urls())

    tasks = [get_content(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
