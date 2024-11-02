# !usr/bin/env python
# -*- coding:utf-8 _*-
import json
import requests

# 提取qq群：聚集地 561337274 的群成员
qq_group_num = 561337274
url = 'https://qinfo.clt.qq.com/cgi-bin/qun_info/get_members_info_v1?friends=1&gc=' + str(qq_group_num)+'&bkn=1893223883&src=qinfo_v3&_ti=1730543186900'
headers = {
    "Host": "tooltt.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Google Chrome\";v=\"98\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
cookies = {

}
res = requests.get(url=url, headers=headers)
res = res.text
print(res)