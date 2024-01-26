import requests

count = 0
while True:
    proxypool_url = 'http://localhost:5555/random'
    proxy = requests.get(proxypool_url).text.strip()
    proxy_url = 'http://' + proxy
    with open('http.txt', 'a+') as f:
        f.write(proxy_url + '\n')
        count += 1
    if count > 1000:
        f.close()
        break
