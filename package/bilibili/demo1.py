import requests  # 数据请求模块  pip install requests
import pprint  # 格式化输出的模块 内置模块
import re  # 正则表达式 内置模块
import random  # 随机模块 内置模块
import time  # 时间模块 内置模块 Python学习群872937351

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}


def get_response(html_url):
    """发送请求"""
    # headers请求头 作用?   把python代码伪装成浏览器
    # cookie: 主要是用检测是否有登录账号 用户信息
    # user-agent: 浏览器基本信息
    response = requests.get(url=html_url, headers=headers)
    return response


def get_video_bv(html_url):
    """获取视频BV号"""
    response = get_response(html_url)
    # 获取json字典数据
    json_data = response.json()
    # 解析数据 json直接解析提取 根据冒号左边的内容 提取冒号右边的内容
    v_list = json_data['data']['list']['vlist']
    # 列表推导式
    v_list = [i['bvid'] for i in v_list]
    # lis = []
    # v_list 是一个列表 列表里面每一个元素都是一个字典
    # 想要获取列表中的每个元素 通过遍历 for循环 i就是字典
    # for i in v_list:
    #     lis.append(i['bvid'])
    # print(v_list)
    # pprint.pprint(response.json())
    return v_list


def get_video_oid(video_bv_id):
    """获取视频的oid参数"""
    # f'{}' 字符串的格式化方法  '{page}'.format(page)
    # bv 号传入url地址当中
    video_url = f'https://www.bilibili.com/video/{video_bv_id}'
    response = get_response(video_url)
    # 函数返回值 \d+ 匹配\d 匹配一个数字 \d+ 是匹配多个数字
    # 正则表达式  oid
    # <script>window.__INITIAL_STATE__={"aid":(762391044),
    # () 精确匹配 表示我要的内容就是括号里面的内容 每一个视频的oid都不一样
    # \d 表示的匹配一个数字 \d+ 表示匹配多个数字 .*? 表示匹配任意字符
    # .*?
    oid = re.findall('<script>window\.__INITIAL_STATE__={"aid":(.*?)', response.text)[0]
    return oid


def comment(oid):
    """评论"""
    comment_list = ['6666', 'up主牛皮', 'python牛皮', '牛皮']
    content = random.choice(comment_list)
    comment_url = 'https://api.bilibili.com/x/v2/reply/add'
    data = {
        'oid': oid,
        'type': '1',
        'message': content,
        'plat': 1,
        'ordering': 'heat',
        'jsonp': 'jsonp',
        'csrf': '0f085ffe952fc8658bfae7a34de1b1d6'
    }
    response = requests.post(url=comment_url, data=data, headers=headers)
    status_code = response.status_code  # 获取状态码
    return status_code


def main(html_url):
    """主函数"""
    v_list = get_video_bv(html_url=html_url)
    for index in v_list:
        time.sleep(2)
        oid = get_video_oid(index)
        status_code = comment(oid)
        if status_code == 200:
            print(f'{index}评论成功')
        else:
            print(f'{index}评论失败')


if __name__ == '__main__':
    for page in range(1, 15):
        print('稍等五秒钟')
        time.sleep(5)
        url = f'https://api.bilibili.com/x/space/arc/search?mid=16682415&ps=30&tid=0&pn={page}&keyword=&order=pubdate&jsonp=jsonp'
        main(url)