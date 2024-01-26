# !usr/bin/env python
# -*- coding:utf-8 _*-
import concurrent.futures
import time


# 定义一个简单的函数，模拟需要在多个线程中执行的任务
def task_function(task_id):
    print(f"Task {task_id} started")
    time.sleep(2)  # 模拟任务执行时间
    print(f"Task {task_id} completed")


# 创建一个 ThreadPoolExecutor 对象
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 提交任务到线程池，这里提交了5个任务
    # 每个任务都会被分配到可用的线程上执行
    futures = [executor.submit(task_function, i) for i in range(5)]

    # 等待所有任务完成
    concurrent.futures.wait(futures)

print("All tasks completed")
