# !usr/bin/env python
# -*- coding:utf-8 _*-
import json
import tkinter as tk
from tkinter import messagebox

# 内置的 xray_config.json 数据，可以在此处修改或直接读取外部文件
xray_config = {
    "log": {
        "access": "none",
        "dnsLog": False,
        "error": "./error.log",
        "loglevel": "warning"
    },
    "api": {
        "services": [
            "HandlerService",
            "LoggerService",
            "StatsService"
        ],
        "tag": "api"
    },
    "inbounds": [
        {
            "listen": "127.0.0.1",
            "port": 62789,
            "protocol": "dokodemo-door",
            "settings": {
                "address": "127.0.0.1"
            },
            "tag": "api"
        }
    ],
    "outbounds": [],
    "policy": {
        "levels": {
            "0": {
                "statsUserDownlink": True,
                "statsUserUplink": True
            }
        },
        "system": {
            "statsInboundDownlink": True,
            "statsInboundUplink": True,
            "statsOutboundDownlink": True,
            "statsOutboundUplink": True
        }
    },
    "routing": {
        "rules": [
            {
                "type": "field",
                "inboundTag": [
                    "api"
                ],
                "outboundTag": "api"
            },
            {
                "type": "field",
                "outboundTag": "blocked",
                "ip": [
                    "geoip:private"
                ]
            },
            {
                "type": "field",
                "outboundTag": "blocked",
                "protocol": [
                    "bittorrent"
                ]
            }
        ]
    },
    "stats": {}
}


def generate_config():
    try:
        # 获取用户输入的参数
        ip_start = int(entry_ip_start.get())
        ip_end = int(entry_ip_end.get())
        base_ip = entry_base_ip.get()

        # 创建配置文件副本
        config = xray_config.copy()

        for i in range(ip_start, ip_end + 1):
            ip = base_ip + str(i)
            tag = f"ip{i}"

            new_outbound = {
                "tag": tag,
                "sendThrough": ip,
                "protocol": "freedom",
                "settings": {}
            }
            config["outbounds"].insert(0, new_outbound)

            for j in range(20000, 70000, 10000):
                new_routing_rule = {
                    "inboundTag": [f"inbound-" + str(j + i)],
                    "outboundTag": tag,
                    "type": "field"
                }
                config["routing"]["rules"].insert(0, new_routing_rule)

        # 将配置保存为新的JSON文件
        with open('xray_config_modified.json', 'w') as f:
            json.dump(config, f, indent=2)

        messagebox.showinfo("成功", "配置文件已生成: xray_config_modified.json")
    except Exception as e:
        messagebox.showerror("错误", str(e))


# 创建主窗口
root = tk.Tk()
root.title("Xray 配置生成器")

# IP起始输入框
tk.Label(root, text="IP Start:").grid(row=0, column=0)
entry_ip_start = tk.Entry(root)
entry_ip_start.grid(row=0, column=1)

# IP结束输入框
tk.Label(root, text="IP End:").grid(row=1, column=0)
entry_ip_end = tk.Entry(root)
entry_ip_end.grid(row=1, column=1)

# Base IP输入框
tk.Label(root, text="Base IP:").grid(row=2, column=0)
entry_base_ip = tk.Entry(root)
entry_base_ip.grid(row=2, column=1)

# 生成按钮
generate_button = tk.Button(root, text="生成配置文件", command=generate_config)
generate_button.grid(row=3, column=0, columnspan=2)

# 启动主循环
root.mainloop()
