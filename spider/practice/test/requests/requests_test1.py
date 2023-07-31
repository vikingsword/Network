import requests


# resp = requests.post(url=url, data=data).content.decode('utf-8')

resp = requests.get('https://api.github.com/events')
# print(resp.status_code)

# print(resp.content)
# print(resp.text)

resp2 = requests.post('https://httpbin.org/post', data={'key': 'value'})
# print(resp2.text)

# set value from dict also can test weak passwd
payload = {'key1': 'value1', 'key2': 'value2'}
resp3 = requests.get('https://api.github.com/events', params=payload)
# print(resp3.url)
# print(resp3.headers)
r = requests.get('https://api.github.com/events', stream=True)

with open('test.txt', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

print(resp.json())




