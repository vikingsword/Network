import tkinter as tk
from tkinter import messagebox
import sqlite3
import json
import random
import string

# 插入记录的函数
def insert_records(node_name, start_range, end_range):
    try:
        # 将起始和结束范围转为整数
        start_range = int(start_range)
        end_range = int(end_range)

        # 连接到SQLite数据库
        conn = sqlite3.connect('x-ui.db')
        cursor = conn.cursor()

        # 测试插入
        for i in range(start_range, end_range + 1):
            sql = (
                'INSERT INTO inbounds (id, user_id, up, down, total, remark, enable, expiry_time, listen, port, protocol, settings, stream_settings, tag, sniffing) '
                'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
            characters = string.ascii_letters + string.digits
            random_password = ''.join(random.choices(characters, k=42))
            random_email = ''.join(random.choices(characters, k=4))
            random_subId = ''.join(random.choices(characters, k=16))
            setting_data = {
                "method": "aes-256-gcm",
                "password": random_password,
                "network": "tcp,udp",
                "clients": [
                    {
                        "method": "aes-256-gcm",
                        "password": random_password,
                        "email": random_email + "@gmail.com",
                        "limitIp": 0,
                        "totalGB": 0,
                        "expiryTime": 0,
                        "enable": True,
                        "tgId": "",
                        "subId": random_subId,
                        "reset": 0
                    }
                ]
            }
            stream_data = {
                "network": "tcp",
                "security": "none",
                "externalProxy": [],
                "tcpSettings": {
                    "acceptProxyProtocol": False,
                    "header": {
                        "type": "none"
                    }
                }
            }
            tag = "inbound-" + str(20000 + i)
            sniffing = {
                "enabled": True,
                "destOverride": [
                    "http",
                    "tls",
                    "quic",
                    "fakedns"
                ],
                "metadataOnly": False,
                "routeOnly": False
            }
            cursor.execute(sql, (
                i, 1, 0, 0, 0, node_name + str(i), 1, 0, "", 20000 + i, "shadowsocks", json.dumps(setting_data),
                json.dumps(stream_data, indent=2), tag, json.dumps(sniffing, indent=2),))

        # 提交事务并关闭连接
        conn.commit()
        conn.close()

        # 插入成功后显示消息
        messagebox.showinfo("Success", "Records inserted successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# 创建图形界面
def create_gui():
    # 创建主窗口
    window = tk.Tk()
    window.title("入站节点批量添加")

    # 标签和输入框
    label_node_name = tk.Label(window, text="节点前缀:")
    label_node_name.pack(pady=5)
    entry_node_name = tk.Entry(window, width=40)
    entry_node_name.pack(pady=5)

    label_start_range = tk.Label(window, text="起始端口:")
    label_start_range.pack(pady=5)
    entry_start_range = tk.Entry(window, width=40)
    entry_start_range.pack(pady=5)

    label_end_range = tk.Label(window, text="结束端口:")
    label_end_range.pack(pady=5)
    entry_end_range = tk.Entry(window, width=40)
    entry_end_range.pack(pady=5)

    # 按钮点击事件
    def on_click():
        node_name = entry_node_name.get()
        start_range = entry_start_range.get()
        end_range = entry_end_range.get()

        if node_name and start_range.isdigit() and end_range.isdigit():
            insert_records(node_name, start_range, end_range)
        else:
            messagebox.showwarning("Input Error", "Please enter valid node_name and range values.")

    # 提交按钮
    submit_button = tk.Button(window, text="执行添加", command=on_click)
    submit_button.pack(pady=10)

    # 运行窗口
    window.mainloop()

# 启动GUI
if __name__ == "__main__":
    create_gui()
