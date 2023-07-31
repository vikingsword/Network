'''
异步爬虫的方式：
    —多线程，多进程（不建议）：
        好处：可以为相关阻塞的操作单独开启线程或者进程，阻塞操作就可以异步执行。
        弊端：无法无限制的开启多线程或者多进程。
    — 线程池、进程池（适当的使用）：
        好处：我们可以降低系统对进程或者线程创建和销毁的一个频率，
        从而很好的降低系统的开销。
        弊端：池中线程或进程的数量是有上限。
'''
import time
from multiprocessing.dummy import Pool

start_time = time.time()
name_list = ['a', 'b', 'c', 'd']


def get_page(str):
    print('download start ' + str + ' ')
    time.sleep(2)
    print('download end ' + str + ' ')

pool = Pool(4)
pool.map(get_page, name_list)

end_time = time.time()

print(end_time - start_time)
