# !usr/bin/env python
# -*- coding:utf-8 _*-
import sqlite3
import json

# 连接到SQLite数据库
conn = sqlite3.connect('x-ui.db')
cursor = conn.cursor()
node_name = "US_ISP_"

# 测试插入
for i in range(2, 256):
    sql = (
        'INSERT INTO inbounds (id, user_id, up, down, total, remark, enable, expiry_time, listen, port, protocol, settings, stream_settings, tag, sniffing) '
        'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
    setting_data = {
        "method": "aes-256-gcm",
        "password": "XqPQw6btNhy5DOMnP7+C+XfhowbIEYjPvuJGaCwxP/U=",
        "network": "tcp,udp",
        "clients": [
            {
                "method": "aes-256-gcm",
                "password": "IHX1AH3gj3YETQv9MY7NW0wmFW6HarZFpQXnnK9kSKs=",
                "email": str(i) + "@gmail.com",
                "limitIp": 0,
                "totalGB": 0,
                "expiryTime": 0,
                "enable": True,
                "tgId": "",
                "subId": "m3d8q15122oqytxd",
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
