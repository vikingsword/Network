import json

import requests

# create taskid
task_url = 'http://127.0.0.1:8775/task/new'
res = requests.get(task_url)
task_id = res.json()['taskid']

# set taskid scan info
data = {
    'url': 'http://192.168.110.34/sqli-labs/Less-2/?id=1'
}
headers = {
    'Content-Type': 'application/json'
}
task_set_option_url = 'http://127.0.0.1:8775/option/' + task_id + '/set'
print(task_set_option_url)
res2 = requests.post(task_set_option_url, data=json.dumps(data), headers=headers)
print(res2.content.decode('utf-8'))

# start scan task aim to taskid
task_start_url = 'http://127.0.0.1:8775/scan/' + task_id + '/start'
res3 = requests.post(task_start_url, data=json.dumps(data), headers=headers)
print(res3.content.decode('utf-8'))

# read scan task result
task_result_url = 'http://127.0.0.1:8775/scan/' + task_id + '/status'
res4 = requests.get(task_result_url)
print(res4.content.decode('utf-8'))

# read scan task data
task_data_url = 'http://127.0.0.1.8775/scan/' + task_id + '/data'
res5 = requests.get(task_data_url)
print(res5.content.decode('utf-8'))
