import requests


def send_request_with_virtual_ip():
    proxy = {
        'http': 'http://your_virtual_ip:port',
        'https': 'http://your_virtual_ip:port'
    }

    url = 'http://example.com'  # 替换为您要访问的目标URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, proxies=proxy, headers=headers, timeout=10)
        # 或使用 requests.post() 进行 POST 请求
        # response = requests.post(url, proxies=proxy, headers=headers, data=data, timeout=10)

        if response.status_code == 200:
            print("请求成功！")
            print(response.text)
        else:
            print(f"请求失败，状态码：{response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"请求发生异常：{e}")


if __name__ == "__main__":
    send_request_with_virtual_ip()
