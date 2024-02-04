# !usr/bin/env python
# -*- coding:utf-8 _*-

file_path = '/spider/tools/anime/new_anime_download/v01/anime_homepage.txt'
list = []
count = 0
for line in open(file_path, 'r'):
    for item in list:
        if item == line:
            print('有重复元素： ', line)
            break
    list.append(line.strip())
    count += 1

if list.__len__() == count:
    print('没有重复元素')