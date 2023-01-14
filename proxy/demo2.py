# from github repo ProxyPool https://github.com/Python3WebSpider/ProxyPool
import requests

target_url = 'http://httpbin.org/get'

# cd /home/vikingar/Sec/Tool/DDos/Proxy/ProxyPool type docker-compose up to start
# copy this proxy function if you want to use
def getRandomProxy():
    proxypool_url = 'http://localhost:5555/random'
    proxy = requests.get(proxypool_url).text.strip()
    proxies = {
        'http': 'http://' + proxy
    }
    return proxies


def getInfo(url):
    return requests.get(url, proxies=getRandomProxy()).text


def main():
    html = getInfo(target_url)
    # print('current proxy is ' + str(getRandomProxy().get('http')))
    print(html)


if __name__ == '__main__':
    main()
