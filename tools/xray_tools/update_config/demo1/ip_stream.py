# !usr/bin/env python
# -*- coding:utf-8 _*-

import json

with open('xray_config.json', 'r') as f:
    config = json.load(f)

ip_start = 2
ip_end = 10
base_ip = "149.52.113."

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

    new_routing_rule = {
        "inboundTag": [f"inbound-" + str(20000 + i)],
        "outboundTag": tag,
        "type": "field"
    }
    config["routing"]["rules"].insert(0, new_routing_rule)

with open('xray_config_modified.json', 'w') as f:
    json.dump(config, f, indent=2)

print("配置文件已生成: xray_config_modified.json")
