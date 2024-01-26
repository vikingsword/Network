# !usr/bin/env python
# -*- coding:utf-8 _*-
import concurrent.futures
import time


# 定义一个简单的函数，模拟需要在多个进程中执行的 CPU 密集型任务
def task_function(task_id):
    print(f"Task {task_id} started")
    result = 0
    for _ in range(1000000):
        result += 1
    print(f"Task {task_id} completed")
    return result


# 创建一个 ProcessPoolExecutor 对象
with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    # 使用 map 函数提交任务到进程池，这里提交了5个任务
    # map 会按顺序返回每个任务的结果
    results = list(executor.map(task_function, range(5)))

print("All tasks completed")
