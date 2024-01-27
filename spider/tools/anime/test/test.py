import requests
import concurrent.futures

video_url1 = 'https://v16m-default.akamaized.net/1e9bb959922d2d3616c5e043a61ff680/65b4bce7/video/tos/alisg/tos-alisg-ve-0051c001-sg/osgGUhwPIe3qIqLALbeAUUKeuFYbClGa0QDB6V/?a=2011&ch=0&cr=0&dr=0&net=5&cd=0%7C0%7C0%7C0&br=3856&bt=1928&bti=MzhALjBg&cs=0&ds=4&ft=XE5bCqT0mmjPD12ZC..R3wU7C1JcMeF~O5&mime_type=video_mp4&qs=0&rc=NWc3O2RpaTUzaDw2ODRoZ0BpM3ludXA5cmY4cDMzODYzNEA0M2EtLzIyNV4xLjUxYDU1YSMyXmgyMmRrLm5gLS1kMC1zcw%3D%3D&l=2024012701570474980190403B691999D5&btag=e000a8000'


def download_video(video_url):
    response = requests.get(video_url, stream=True)

    with open('test.mp4', 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

    print(f"Download of test.mp4 completed")


# 视频链接列表
video_urls = [
    video_url1
]

# 创建 ThreadPoolExecutor 对象
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 使用 map 函数提交下载任务到线程池
    executor.map(download_video, video_urls)

print("All videos downloaded")