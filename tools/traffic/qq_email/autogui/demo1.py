# !usr/bin/env python
# -*- coding:utf-8 _*-
import pyautogui

pyautogui.moveTo(100, 100)  # 将鼠标移动到屏幕坐标 (100, 100)
pyautogui.click()  # 点击鼠标左键
pyautogui.typewrite('Hello, World!', interval=0.1)  # 模拟输入文本
