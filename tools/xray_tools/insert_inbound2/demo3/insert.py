import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import json
import random
import string
import uuid


def generate_random_string(length):
    """生成指定长度的随机字符串，只包含小写字母和数字"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_uuid():
    """生成符合 8+4+4+4+12 格式的字符串"""
    parts = [
        generate_random_string(8),
        generate_random_string(4),
        generate_random_string(4),
        generate_random_string(4),
        generate_random_string(12)
    ]
    return "-".join(parts)

# 插入记录的函数
def insert_records(node_name, start_range, end_range):

    try:
        # 将起始和结束范围转为整数
        start_range = int(start_range)
        end_range = int(end_range)

        # 连接到SQLite数据库
        conn = sqlite3.connect('x-ui.db')
        cursor = conn.cursor()
        count = 1
        for i in range(start_range, end_range + 1):
            # 插入ss
            sql = (
                'INSERT INTO inbounds (id, user_id, up, down, total, remark, enable, expiry_time, port, protocol, settings, stream_settings, tag, sniffing, allocate) '
                'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)')
            characters = string.ascii_letters + string.digits
            random_password1 = ''.join(random.choices(characters, k=42))
            random_password11 = ''.join(random.choices(characters, k=44))
            random_email1 = ''.join(random.choices(characters, k=8))
            random_subId1 = ''.join(random.choices(characters, k=16))
            setting_data1 = {
                "method": "aes-256-gcm",
                "password": random_password1 + str("=="),
                "network": "tcp,udp",
                "clients": [
                    {
                        "method": "aes-256-gcm",
                        "password": random_password11 + str("="),
                        "email": random_email1 + "@gmail.com",
                        "limitIp": 0,
                        "totalGB": 0,
                        "expiryTime": 0,
                        "enable": True,
                        "tgId": "",
                        "subId": random_subId1,
                        "comment": "",
                        "reset": 0
                    }
                ],
                "ivCheck": False
            }
            stream_data1 = {
                "network": "tcp",
                "security": "none",
                "tcpSettings": {
                    "acceptProxyProtocol": False,
                    "header": {
                        "type": "none"
                    }
                }
            }
            tag1 = "inbound-" + str(20000 + i)
            sniffing1 = {
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
            allocate1 = {
                "strategy": "always",
                "refresh": 5,
                "concurrency": 3
            }
            cursor.execute(sql, (
                count, 1, 0, 0, 0, node_name + str(i) + str("-1"), 1, 0, 20000 + i, "shadowsocks", json.dumps(setting_data1),
                json.dumps(stream_data1), tag1, json.dumps(sniffing1), json.dumps(allocate1),))
            count += 1

            # 测试插入 vmess ------------------------------------------------------
            random_id2 = str(uuid.uuid4())
            random_email2 = ''.join(random.choices(characters, k=8))
            random_subId2 = ''.join(random.choices(characters, k=16))
            setting_data2 = {
                "clients": [
                    {
                        "id": random_id2,
                        "security": "auto",
                        "email": random_email2 + "@gmail.com",
                        "limitIp": 0,
                        "totalGB": 0,
                        "expiryTime": 0,
                        "enable": True,
                        "tgId": "",
                        "subId": random_subId2,
                        "comment": "",
                        "reset": 0
                    }
                ]
            }
            stream_data2 = {
                "network": "tcp",
                "security": "none",
                "tcpSettings": {
                    "acceptProxyProtocol": False,
                    "header": {
                        "type": "none"
                    }
                }
            }
            tag2 = "inbound-" + str(30000 + i)
            sniffing2 = {
                "enabled": False,
                "destOverride": [
                    "http",
                    "tls",
                    "quic",
                    "fakedns"
                ],
                "metadataOnly": False,
                "routeOnly": False
            }
            allocate2 = {
                "strategy": "always",
                "refresh": 5,
                "concurrency": 3
            }
            cursor.execute(sql, (
                count, 1, 0, 0, 0, node_name + str(i) + str("-2"), 1, 0, 30000 + i, "vmess", json.dumps(setting_data2),
                json.dumps(stream_data2), tag2, json.dumps(sniffing2), json.dumps(allocate2),))
            count += 1

            # 测试插入 socks5 ------------------------------------------------------------
            sql3 = (
                'INSERT INTO inbounds (id, user_id, up, down, total, remark, enable, expiry_time, port, protocol, settings, tag, sniffing, allocate) '
                'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
            random_pass3 = ''.join(random.choices(characters, k=10))
            setting_data3 = {
                "auth": "password",
                "accounts": [
                    {
                        "user": "tkidcsocks",
                        "pass": random_pass3
                    }
                ],
                "udp": False,
                "ip": "127.0.0.1"
            }
            tag3 = "inbound-" + str(40000 + i)
            sniffing3 = {
                "enabled": False,
                "destOverride": [
                    "http",
                    "tls",
                    "quic",
                    "fakedns"
                ],
                "metadataOnly": False,
                "routeOnly": False
            }
            allocate3 = {
                "strategy": "always",
                "refresh": 5,
                "concurrency": 3
            }
            cursor.execute(sql3, (
                count, 1, 0, 0, 0, node_name + str(i) + str("-3"), 1, 0, 40000 + i, "socks", json.dumps(setting_data3),
                tag3, json.dumps(sniffing3), json.dumps(allocate3),))
            count += 1
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
