def deleteDupLine(input_file, output_file):
    ip_set = set()
    with open(input_file, 'r') as f:
        line = f.readline()
        while line:
            line = line.strip()
            if line not in ip_set:
                ip_set.add(line)
            line = f.readline()


    with open(output_file, 'w') as f:
        for item in ip_set:
            f.write(item + '\n')
    f.close()


if __name__ == '__main__':
    input_file = '../input.txt'
    output_file = '../output.txt'
    deleteDupLine(input_file, output_file)
