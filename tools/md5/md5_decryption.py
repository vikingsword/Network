def get_password(input_string):
    for md5_info in open('md5_dict.txt', 'r'):
        if input_string in md5_info.strip():
            password = md5_info.split('|')[0]
            return password


if __name__ == '__main__':
    print('解密开始，输入数字 0 退出 ')
    while True:
        your_input = input('输入md5进行解密： ')
        if your_input == '0':
            break
        value = get_password(your_input)
        if value is not None:
            print('密码为 ' + value)
        else:
            print('没有找到密码')
