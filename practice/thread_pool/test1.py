from concurrent.futures import ThreadPoolExecutor
import threading
import time


# ����һ��׼����Ϊ�߳�����ĺ���
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum


# ����һ������2���̵߳��̳߳�
pool = ThreadPoolExecutor(max_workers=2)
# ���̳߳��ύһ��task, 50����Ϊaction()�����Ĳ���
future1 = pool.submit(action, 50)
# ���̳߳����ύһ��task, 100����Ϊaction()�����Ĳ���
future2 = pool.submit(action, 100)
# �ж�future1����������Ƿ����
print(future1.done())
time.sleep(3)
# �ж�future2����������Ƿ����
print(future2.done())
# �鿴future1��������񷵻صĽ��
print(future1.result())
# �鿴future2��������񷵻صĽ��
print(future2.result())
# �ر��̳߳�
pool.shutdown()