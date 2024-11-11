# !usr/bin/env python
# -*- coding:utf-8 _*-
import yaml

with open('./config.yaml', 'r') as f:
    config = yaml.safe_load(f)
print(config['EMAIL']['SENDER'])
print(config['EMAIL']['KEY'])
