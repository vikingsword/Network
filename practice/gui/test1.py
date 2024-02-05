# !usr/bin/env python
# -*- coding:utf-8 _*-
import tkinter as tk


def on_button_click():
    label.config(text="Hello, " + entry.get())


# 创建主窗口
root = tk.Tk()
root.title("简单GUI示例")

# 创建标签
label = tk.Label(root, text="请输入你的名字:")
label.pack(pady=10)

# 创建文本输入框
entry = tk.Entry(root)
entry.pack(pady=10)

# 创建按钮
button = tk.Button(root, text="点击我", command=on_button_click)
button.pack(pady=10)

# 运行主循环
root.mainloop()
