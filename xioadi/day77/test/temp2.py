def remove_duplicate_lines(filename):
    lines_set = set()  # 用于存储唯一行的集合
    output_filename = "../glassfish_fofa_scan/output.txt"  # 输出文件名

    # 打开输入文件并读取内容
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # 去除行末尾的换行符和空格
            if line:
                lines_set.add(line)  # 添加非空行到集合中

    # 打开输出文件并写入内容
    with open(output_filename, 'w') as file:
        for line in lines_set:
            file.write(line + '\n')

    print("重复行已删除，结果保存在 " + output_filename + " 文件中。")


# 使用示例
filename = "../glassfish_fofa_scan/fofa_ips.txt"  # 输入文件名
remove_duplicate_lines(filename)
