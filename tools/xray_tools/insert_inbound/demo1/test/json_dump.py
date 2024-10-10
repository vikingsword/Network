# !usr/bin/env python
# -*- coding:utf-8 _*-
import json

data = {
    "method": "aes-256-gcm",
    "password": "XqPQw6btNhy5DOMnP7+C+XfhowbIEYjPvuJGaCwxP/U=",
    "network": "tcp,udp",
    "clients": [
        {
            "method": "aes-256-gcm",
            "password": "IHX1AH3gj3YETQv9MY7NW0wmFW6HarZFpQXnnK9kSKs=",
            "email": "mwztdtxy",
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

json_str = json.dumps(data)
# json_str = json.dumps(data, indent=2)
print(json_str)
