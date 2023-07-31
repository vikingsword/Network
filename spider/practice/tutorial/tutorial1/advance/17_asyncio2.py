import asyncio
import time


async def request(url):
    print('正在下载', url)
    # 在异步协程中出现了同步模块相关的代码，那么就无法实现异步
    # time.sleep(2)
    # 在 asyncio 中遇到阻塞操作必须手动挂起
    await asyncio.sleep(2)
    print('下载完毕', url)

start = time.time()

urls = [
    'www.baidu.com',
    'www.google.com',
    'www.sogou.com'
]

tasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
# 需要将任务列表封装到 wait 中
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()

print(end - start)