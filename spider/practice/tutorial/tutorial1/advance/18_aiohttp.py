import asyncio
import time

import aiohttp
import requests

urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/vikingar'
]

start = time.time()


async def get_page(url):
    print('正在下载 ' + url)
    async with aiohttp.ClientSession() as session:
        # 与 requests 模块同理，也可以使用 .post() 请求
        # 同理可以使用 headers  params/data  proxy='http://ip:port'(这里不是proxies)
        async with await session.get(url) as resp:
            # text(): return string; read(): return bytes; json(): return json
            # 在获取响应数据操作之前一定要使用 await 进行手动挂起
            page_text = await resp.text()
            print(page_text)
    print('下载完毕 ' + url)


tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()

print('time: ', end - start)
