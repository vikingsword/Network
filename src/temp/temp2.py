# for i in range(0, 101, 10):
#     print(i)

key_list = ['学校', '公司', '大学', '学院', '医院', '中学']
with open('key.txt', 'a+', encoding='utf-8') as f:
    list(map(lambda key: f.write(key + '\n'), key_list))


url = "http://www.jnjzgy.org/Aboutjj/id=1"

# 使用rsplit()方法分割URL，并替换最后一个斜杠为问号
modified_url = url.rsplit('/', 1)[0] + '?' + url.rsplit('/', 1)[1]

print(modified_url)