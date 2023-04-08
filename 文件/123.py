# print('1,2,3')

from pathlib import Path
import shutil
# p=Path()
# p=p/"a"/"b"
# print(p.name,p.suffix)
#
# # print(p.cwd(),p.is_dir())
# # print(p.absolute().parents)
# # for x in p.absolute().parents:
# #     print(x)
# # #shutil.copyfile('1.py',"111.py")
# # shutil.move("111.py","a")
#
# pp=Path("d:/123/aaa.txt")
# # print(pp.parent,pp.name)
# import os

"""
读取文件，字符串拼接 ，列表解析式
"""
list=[]
list2=[]
with open('d:/456.txt') as f:
    for line in f.readlines():
        list.append(line)
print(list)
with open('d:/123.txt','w+') as f:
    for ls in list:
        str1=ls[0:12]
        result = '-'.join([str1[i:i + 2] for i in range(0, len(str1), 2)])
        f.write('{}\n'.format(result))
    # list2.append(result)
print(list2)

# import re
# path1=os.path
#
# pattern = r'\w{12}'
# match = re.findall(pattern,'d:/456.txt')
#
# if match:
#     print('匹配到的字符串为:', match.group())
# else:
#     print('未匹配到字符串')
