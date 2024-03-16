# !usr/bin/env python
# -*- coding:utf-8 _*-
import os.path
import time
import requests
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'http://v16m-default.akamaized.net/3c836054ee9e04d288159cc8ec022d6e/65f54f24/video/tos/alisg/tos-alisg-ve-0051c001-sg/oEnwJ0NBA4zBI2oymLIAATI7PiEnIViyO3ZfvB/?a=2011&ch=0&cr=0&dr=0&net=5&cd=0%7C0%7C0%7C0&br=3982&bt=1991&bti=MzhALjBg&cs=0&ds=4&ft=XE5bCqT0mmjPD12jZTZR3wU7C1JcMeF~O5&mime_type=video_mp4&qs=0&rc=M2Y4OTdlMzo6PGc8NjdnOUBpM240NXA5cjQ2cTMzODYzNEBhYzQyM2IxNWExNjVhLjBjYSMxNDZwMmRrM21gLS1kMC1zcw%3D%3D&vvpl=1&l=202403160126160FED3AE048621B613E77&btag=e000a8000'

response = requests.head(url)
# 检查请求是否成功
response.raise_for_status()

bytes_size = int(response.headers.get('content-length', 0))
print(bytes_size)
file_size = float(round(bytes_size / 1024 / 1024))
print(file_size)


path = "1.mp4"
with open(path, 'wb') as file, tqdm(
        desc=path,
        total=bytes_size,
        unit='B',
        unit_scale=True,
        unit_divisor=8192,
        colour='#0396ff'
) as bar:
    response = requests.get(url, stream=True)
    for data in response.iter_content(chunk_size=8192):
        bar.update(len(data))
        file.write(data)
