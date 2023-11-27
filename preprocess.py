'''加逗号分隔符，并且使json文件变为列表形式'''
def add_delimiter(input_data, real_input):
    '''
    :param input_data: 原始输入json文件
    :param new_input: 加完分隔符的实际输入json文件
    :return: 无
    '''
    with open(input_data, 'r', encoding="utf-8") as fr:
     with open(real_input, 'w', encoding="utf-8") as fw:
        for line in fr:       #读取input_data中每一行
            if line == "}\n":  #观察结构可得，判断行内容为"}"以及换行符"\n"时
                fw.writelines(line.strip("\n") + ',' + "\n")   #变为"},"
            else:                            #其余不变
                fw.writelines(line)
    with open(real_input, 'r+', encoding="utf-8") as fs:
        content = fs.read()    #读取real_input中的所有内容
        fs.seek(0)              #指针指到文件开头
        fs.write("{\"data\":")
        fs.write("[")           
        fs.write(content)      
        fs.seek(0,2)            #指针指到末尾，偏移量为0
        fs.write("]")
        fs.write("}")
        print("加完分隔符的json文件已写入完毕！")