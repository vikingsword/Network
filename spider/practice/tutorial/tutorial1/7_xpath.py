from lxml import etree

'''
- 如何实例化一个etree对象: from lxml import etree
    — 1．将本地的html文档中的源码数据加载到etree对象中: etree.parse(filePath)
    — 2．可以将从互联网上获取的源码数据加载到该对象中etree.HTML('page_text')
    
- xpath('xpath表达式') - xpath表达式: 
    — /: 表示的是从根节点开始定位。表示的是一个层级。
    — //: 表示的是多个层级。可以表示从任意位置开始定位。
    - 属性定位: //div[@class＝'song'] tag[@attrName＝"attrValue"]
    - 索引定位: //div[@class＝"song"]/p[3] 索引是从1开始的。 
    - 取文本: 
        — /text()获取的是标签中直系的文本内容
        — //text()标签中非直系的文本内容(所有的文本内容)
    - 取属性: 
        /@attrName => img/src/href ....
'''

# tree = etree.parse('test.html', etree.HTMLParser())
tree = etree.parse('test.html')
# res = tree.xpath('//p[@class="title"]/b')
res = tree.xpath('//p[@class="story"][1]//a[@id="link2"]/text()')
res2 = tree.xpath('//p[@class="story"][1]//text()')
res3 = tree.xpath('//p[@class="story"][1]//text()')
res4 = tree.xpath('//p[@class="story"][1]/a[@id="link1"]/@href')

print(res4)
# print(str(res[0]).strip())
# for item in res3:
#     print(str(item).strip())