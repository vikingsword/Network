import hashlib


def output_md5(input_string):
    # 创建一个MD5哈希对象
    md5_hash = hashlib.md5()

    # 将输入的字符串转换为字节类型，并更新哈希对象
    md5_hash.update(input_string.encode('utf-8'))

    # 获取加密后的十六进制表示
    cryption_string = md5_hash.hexdigest()

    return cryption_string


if __name__ == '__main__':
    input_string = input('输入想要加密的字符串： ')
    print(output_md5(input_string))
