from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

content = input('input message: ')
times = input('input times: ')
print('move your cursor to message box')
time.sleep(2)

for i in range(3):
    print(r'距离程序运行还有 %d 秒！' % (3 - i))
    time.sleep(1)

for i in range(int(times)):
    keyboard.type(content)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)

print('发送完成，请关闭窗口')
