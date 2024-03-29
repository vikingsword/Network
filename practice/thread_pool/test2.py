# !usr/bin/env python
# -*- coding:utf-8 _*-
from concurrent.futures import ThreadPoolExecutor
import time


# 参数times用来模拟下载的时间
def down_video(times):
    time.sleep(times)
    print("down video {}s finished".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞
task1 = executor.submit(down_video, (3))
task2 = executor.submit(down_video, (2))
# done方法用于判定某个任务是否完成
print("任务1是否已经完成：", task1.done())
# cancel方法用于取消某个任务,该任务没有放入线程池中才能取消成功
print("取消任务2：", task2.cancel())
time.sleep(4)
print("任务1是否已经完成：", task1.done())
# result方法可以获取task的执行结果
print(task1.result())
