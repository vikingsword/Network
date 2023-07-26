def get_password(input_string):
    for md5_info in open('md5_dict.txt', 'r'):
        if input_string in md5_info.strip():
            password = md5_info.split('|')[0]
            print('密码为：' + password)


if __name__ == '__main__':
    your_input = input('输入md5进行解密： ')
    get_password(your_input)
