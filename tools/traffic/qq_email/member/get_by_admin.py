# !usr/bin/env python
# -*- coding:utf-8 _*-
# cookie 方式容易失效
import requests

# URL and parameters
qq_group_num = 561337274
url = "https://qinfo.clt.qq.com/cgi-bin/qun_info/get_members_info_v1?friends=1&gc="+str(qq_group_num)+"&bkn=1893223883&src=qinfo_v3&_ti=1730543186900"

# Headers
headers = {
    "Host": "qinfo.clt.qq.com",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) QQ/9.7.23.29391 Chrome/43.0.2357.134 Safari/537.36 QBCore/3.43.1298.400 QQBrowser/9.0.2524.400",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://qinfo.clt.qq.com/qinfo_v3/member.html?groupuin=561337274",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.8"
}

# Cookies
cookies = {
    "RK": "cnP5LgfpHn",
    "eas_sid": "i1t7w201G8Y18401Q44317w766",
    "pgv_pvid": "9298128072",
    "ts_uid": "483008590",
    "ptcz": "3a025dc81c79ab761d21324f41e7dddba25da3fcb8dfbbf19b8acde858ebf019",
    "traceid": "0c37df75e1",
    "p_skey": "pShku*lBUtPsKn6vJd6SsnqSGTMT5ydm1dh2nZjQxUY_",
    "p_uin": "o1974392477",
    "uin": "o1974392477",
    "skey": "doNCliSJZv"
}

# Making the GET request
response = requests.get(url, headers=headers, cookies=cookies)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # assuming the response is JSON
    print(data)
    # first_items = [member_id for member_id in data['members'].keys()]
    # print(first_items)
    # print(len(first_items))

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
