# coding:utf-8

# NJOY99程序计算完成后，对计算生成的文件进行后处理

import os

files = os.listdir('C:\\Users\\Administrator\\Desktop\\RESULT1\\1200K\\')

files = [file for file in files if 'XSDIR' in file]
print(files)
print(len(files))

# 用于存储整块的文本信息，便于更新XSDIR文件
file_content = []

for each in files:
    filename = each.split('_1200')[0] +'_1200.ace'
    
    print(filename)
    
    # 文件内容只有一行
    content = []
    lines = []
    with open(each, 'r') as f:
        lines = f.readlines()
        content = [line.replace('filename', filename) for line in lines]
        print(content)
        file_content.append(content[0])
    
    with open(each, 'w') as f:
        f.writelines(content)


# 写整块信息文件
with open('FUCK.txt', 'w') as f:
    f.writelines(file_content)
