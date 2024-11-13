# !usr/bin/env python
# -*- coding:utf-8 _*-
# 单个成员qq号获取
import requests

qq_group = "104636254"
# url = "cgi.qqweb.qq.com/cgi.qqweb.qq.com/tempchatforgroup/api/get_single_info?tuin=2678077641&gcode=" + qq_group + "&t=173139085654"
url = "cgi.qqweb.qq.com/cgi.qqweb.qq.com/tempchatforgroup/api/get_single_info?gcode=" + qq_group + "&t=173139085654"
headers = {
    "Connection": "keep-alive",
    "Accept": "*/*",
    "Content-Type": "text/plain;charset=UTF-8",
    "Origin": "https://qqweb.qq.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) QQ/9.7.23.29391 Chrome/43.0.2357.134 Safari/537.36 QBCore/3.43.1298.400 QQBrowser/9.0.2524.400",
    "Referer": "https://qqweb.qq.com/tempchatforgroup/index.html?param=Z2lkPTIwNDc2MzYyNTQmZ3Vpbj0xMDQ2MzYyNTQmdG91aW49MjY3ODA3NzY0MSZub2FkPTAmb2ZmaWNlbW9kZT0wJmduYW1lPeWNjuWNl%2BWklui0uOS6pOa1gSZ0bmFtZT3mkI%2FmiJAmZXE9MA%3D%3D&sext=tJaehxcrY3qdvJphrcApHTkwcJDQr36OGaTb7kwMQOJmWFrzQvOjfFiD%2BFPheWnO5Rw9tKMJEvUtOxSZrwVUZr2QDhz1dJGS1SSaYRDnTN3BqQC5n3f%2BToydVuj8MamQGgGQNzNn7hM8AczdZc4f%2Bw%3D%3D&stkey=BF1056B54E413B459A1076B226ECFE0057313EF72DDB0182CB248CF7A6AFCEC463D7451223975A3FF203B02819C49A0DE8B4855463A6409325D434D96347A5CD793C1B415D099A321FBFF850E309A5E6A89F73796A050C91",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.8",
    "Cookie": "RK=cnP5LgfpHn; eas_sid=i1t7w201G8Y18401Q44317w766; pgv_pvid=9298128072; p_skey=BEYyTv-PhfqX1U6YorV6B3NlEddohkNzWcXMSJyk-hE_; p_uin=o1974392477; uin=o1974392477; skey=@hNtfz6PvJ; ptcz=3a025dc81c79ab761d21324f41e7dddba25da3fcb8dfbbf19b8acde858ebf019"
}

res = requests.get(url=url, headers=headers)

