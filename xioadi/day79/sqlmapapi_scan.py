import json

import requests

base_url = 'http://127.0.0.1:8775/'

# 1. create task id
task_new_url = base_url + 'task/new'
resp = requests.get(task_new_url)
task_id = resp.json()['taskid']

# 2. 设置任务id的配置信息(扫描信息)
task_set_scan = base_url + 'option/' + task_id + '/set'
data = {
    'url': 'http://127.0.0.1/sqli-labs/Less-1/?id=1'
}
headers = {
    # 'User-Agent:': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Content-Type': 'application/json'
}
resp2 = requests.post(url=task_set_scan, data=json.dumps(data), headers=headers)
print(resp2.content.decode('utf-8'))

# 3. 启动对应id的扫描任务
task_scan = base_url + '/scan/' + task_id + '/start'
resp3 = requests.post(url=task_scan, data=json.dumps(data), headers=headers)
print(resp3.content.decode('utf-8'))

# 4. 获取对应id的扫描状态
task_scan_status = base_url + '/scan/' + task_id + '/status'
resp4 = requests.get(url=task_scan)
print(resp4.content.decode('utf-8'))

# 5. 如果成功获取扫描结果
task_data = base_url + '/scan/' + task_id + '/data'
while True:
    if 'running' in resp4.content.decode('utf-8'):
        print('task is running ... ')
        pass
    else:
        resp5 = requests.get(url=task_data)
        print(resp5.content.decode('utf-8'))