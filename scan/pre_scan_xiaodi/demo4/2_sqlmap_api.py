import json
import time

import requests

# todo always running ?
def sqlmapApi(url):
    # set task basic information
    data = {
        # http://192.168.110.34/sqli-labs/Less-1/?id=1
        'url': url
    }
    headers = {
        'Content-Type': 'application/json'
    }

    # create taskid
    task_url = 'http://127.0.0.1:8775/task/new'
    res = requests.get(task_url)
    task_id = res.json()['taskid']
    if 'success' in res.content.decode('utf-8'):
        print('sqlmap task create successful! ')
        # set taskid scan info
        task_set_option_url = 'http://127.0.0.1:8775/option/' + task_id + '/set'
        res2 = requests.post(task_set_option_url, data=json.dumps(data), headers=headers)
        if 'success' in res2.content.decode('utf-8'):
            print('sqlmap task setting successful! ')
            # start scan task aim to taskid
            task_start_url = 'http://127.0.0.1:8775/scan/' + task_id + '/start'
            res3 = requests.post(task_start_url, data=json.dumps(data), headers=headers)
            if 'success' in res3.content.decode('utf-8'):
                print('sqlmap task start successful! ')
                while 1:
                    # loop read scan task status
                    task_result_url = 'http://127.0.0.1:8775/scan/' + task_id + '/status'
                    res4 = requests.get(task_result_url)
                    if 'running' in res4.content.decode('utf-8'):
                        print('task is running')
                        pass
                    else:
                        # get scan task data
                        try:
                            task_data_url = 'http://127.0.0.1.8775/scan/' + task_id + '/data'
                            res5 = requests.get(task_data_url)
                            # write on file after get result
                            with open(r'result.txt', 'a') as f:
                                f.write(task_data_url + '\n')
                                f.write(res5.content.decode('utf-8'))
                            break
                        except Exception as e:
                            pass
                    time.sleep(0.2)


if __name__ == '__main__':
    # read file and scan
    for url in open('target.txt'):
        url = url.replace('\n', '')
        sqlmapApi(url)
