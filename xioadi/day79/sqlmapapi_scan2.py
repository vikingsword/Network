import json
import time

import requests

base_url = 'http://127.0.0.1:8775/'


def sqlmapApi(url):
    data = {
        'url': url
    }
    headers = {
        'Content-Type': 'application/json'
    }

    task_new_url = base_url + 'task/new'
    resp = requests.get(task_new_url)
    task_id = resp.json()['taskid']
    res = resp.content.decode('utf-8')

    if 'success' in res:
        print('任务 ' + task_id + ' 创建成功 ')
        task_set_scan = base_url + 'option/' + task_id + '/set'
        resp2 = requests.post(url=task_set_scan, data=json.dumps(data), headers=headers)
        res2 = resp2.content.decode('utf-8')
        if 'success' in res2:
            print('任务 ' + task_id + ' 配置成功')
            task_scan = base_url + '/scan/' + task_id + '/start'
            resp3 = requests.post(url=task_scan, data=json.dumps(data), headers=headers)
            res3 = resp3.content.decode('utf-8')
            if 'success' in res3:
                print('任务 ' + task_id + ' 启动扫描')
                with open(r'sqlmapapi_scan_result.txt', 'a+') as f:
                    f.write('=========== python sqlmapapi task ' + task_id + ' start ===========' + '\n\n')
                while True:
                    task_scan_status = base_url + '/scan/' + task_id + '/status'
                    resp4 = requests.get(url=task_scan_status)
                    res4 = resp4.content.decode('utf-8')
                    if 'running' in res4:
                        print('任务 ' + task_id + ' 正在扫描....')
                        pass
                    else:
                        task_data_url = base_url + '/scan/' + task_id + '/data'
                        resp5 = requests.get(url=task_data_url)
                        res5 = resp5.content.decode('utf-8')
                        with open(r'sqlmapapi_scan_result.txt', 'a+') as f:
                            f.write('target: ' + url + "\n")
                            f.write(res5 + '\n\n')
                            f.write('=========== python sqlmapapi task ' + task_id + ' end ===========' + '\n\n')
                            f.close()
                        # 扫描结束 删除任务
                        break
                    time.sleep(1)


if __name__ == '__main__':
    for url in open('urls.txt', 'r'):
        url = url.strip()
        sqlmapApi(url)
