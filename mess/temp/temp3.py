from pyecharts.charts import Line

# 得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["China", "America", "English"])
# 添加y轴数据
line.add_yaxis("GDP", [30, 20, 10])
# 生成图表
line.render()
