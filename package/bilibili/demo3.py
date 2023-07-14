import requests

def save_page(url, file_name):
    headers = {
        'Cookie': 'bili_jct=891b8ac0f24f16399518c0029f128846; sid=6r2cr7cr; PVID=1; browser_resolution=1920-936; buvid_fp=883684e9de05dafd54f80c1dfc2d6173; CURRENT_FNVAL=80; CURRENT_QUALITY=0; bp_video_offset_80080888=817691129546801156; b_lsid=967FFC87_1894E231D43'
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(resp.text)
        print('网页已保存')
    else:
        print('保存失败')


if __name__ == '__main__':
    url = 'https://www.bilibili.com/read/cv18169456/?from=readlist'
    file_name = '1.html'
    save_page(url, file_name)