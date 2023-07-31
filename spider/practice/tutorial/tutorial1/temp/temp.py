import requests

url = 'https://pearvideo.com/videoStatus.jsp?contId=1530444'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Referer': 'https://pearvideo.com/video_1530444'
}
resp = requests.get(url=url, headers=headers)
# with open('../result/4.html', 'wb') as f:
#     f.write(resp)
resp.encoding = 'utf-8'
# res 为 json 对象
res = resp.json()
print(res['videoInfo']['videos']['srcUrl'])