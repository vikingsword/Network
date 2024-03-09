# !usr/bin/env python
# -*- coding:utf-8 _*-
import requests
from tqdm import tqdm
from tqdm.gui import tqdm_gui


def download_video(url, output_file):
    # 发送GET请求获取文件大小
    response = requests.head(url)
    file_size = int(response.headers.get('content-length', 0))
    # print("file_size = ", file_size)


    # 打开文件准备写入
    with open(output_file, 'wb') as file, tqdm(
            desc=output_file,
            total=file_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            colour='#0396ff'
    ) as bar:
        # 发送GET请求下载文件并更新进度条
        response = requests.get(url, stream=True)
        for data in response.iter_content(chunk_size=1024):
            bar.update(len(data))
            file.write(data)


if __name__ == "__main__":
    video_url = "http://v16m-default.akamaized.net/401f0eaf5826b5ca9df2df05f34e5036/65ec2a16/video/tos/alisg/tos-alisg-ve-0051c001-sg/oot48XuXeAF5OhGtMO6N2CRAGL2femde9AIgGI/?a=2011&ch=0&cr=0&dr=0&net=5&cd=0%7C0%7C0%7C0&br=2722&bt=1361&bti=MzhALjBg&cs=0&ds=4&ft=XE5bCqT0mmjPD12Ex8kR3wU7C1JcMeF~O5&mime_type=video_mp4&qs=0&rc=OTdpNzszZTg5O2c8Ozw6NUBpM3U5ZHg5cm9pcTMzODYzNEBfYzU0YGNjX2AxLTIxNDUwYSM2ci8tMmRrYWdgLS1kMC1zcw%3D%3D&l=20240309025725A04A6CB872B5D11CCB87&btag=e000a8000"
    output_filename = "test.mp4"

    download_video(video_url, output_filename)
