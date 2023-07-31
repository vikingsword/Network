'''
—3．单线程＋异步协程（推荐）：
event＿loop：事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，
当满足某些条件的时候，函数就会被循环执行。
coroutine：协程对象，我们可以将协程对象注册到事件循环中，它会被事件循环调用。
我们可以使用 async 关键字来定义一个方法，这个方法在调用时不会立即被执行，而是返回一个协程对象。
task：任务，它是对协程对象的进一步封装，包含了任务的各个状态。
future：代表将来执行或还没有执行的任务，实际上和 task 没有本质区别。async 定义一个协程.｜
await 用来挂起阻塞方法的执行。
'''
import asyncio


async def request(url):
    print('正在请求的url是： ', url)
    print('请求成功 ', url)
    return url


c = request('www.baidu.com')


# # 创建事件循环对象
# loop = asyncio.get_event_loop()
# # 将协程对象注册到loop中， 然后启动 loop
# loop.run_until_complete(c)

# # task 的使用
# loop2 = asyncio.get_event_loop()
# task = loop2.create_task(c)
# print(task)
# loop2.run_until_complete(task)
# print(task)

# # future 的使用
# loop3 = asyncio.get_event_loop()
# task2 = asyncio.ensure_future(c)
# print(task2)
# loop3.run_until_complete(task2)
# print(task2)


# 回调绑定
def callback_fun(task):
    # result 返回的就是任务对象中封装的协程对象对应函数的返回值
    print(task.result)


loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
# 将回调函数绑定到任务对象中
task.add_done_callback(callback_fun)
loop.run_until_complete(task)
