import json

from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

# 读取文件中的数据
f = open("E:\\Dev\\Python\\Project\\Network\\mess\\pyechars\\疫情.txt", "r", encoding="UTF-8")
data_json = f.read()
# 将json的数据转化为数据字典
data_dict = json.loads(data_json)
# 取出2辽宁省的信息
province_data_list = data_dict["areaTree"][0]["children"][17]["children"]
# 定义一个空列表用于存储辽宁省的信息
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))
print(data_list)

# 创建地图实例化对象
map = Map()
# 添加数据到map对象中
map.add("辽宁确诊人数", data_list, "辽宁")
# 设置全局变量
map.set_global_opts(
    title_opts=TitleOpts(is_show=True, title="辽宁确诊人数"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#5470c6"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#91cc75"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#fac858"},
            {"min": 1000, "max": 9999, "label": "1000-9999", "color": "#73c0de"},
            {"min": 10000, "label": "10000以上", "color": "#ea7ccc"}
        ]

    )
)
# 绘制地图
map.render("辽宁确诊人数.html")
