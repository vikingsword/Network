import requests

headers = {
    'origin': 'https://www.bilibili.com',
    'refer': 'https://www.bilibili.com/video/BV1P3411Z7UQ/?spm_id_from=444.41.list.card_archive.click&vd_source=98d30662a8389fe59d43b514c9d673a1',
    'cookie_uuid': 'bili_jct=ebe2a4c28ca8e5d6c7529849568f81c1; PVID=1; b_lsid=317BC8410_185E6B15281; sid=55j9jpfr; bp_video_offset_80080888=754943135018123300; innersign=1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
data = {
    'csrf': 'ebe2a4c28ca8e5d6c7529849568f81c1',
    'message': 'test2',
    'oid': '435276803',
    'plat': '1',
    'type': '1'
}
url = 'https://api.bilibili.com/x/v2/reply/add'

res = requests.post(url=url, headers=headers, data=data)

print(res.text)
