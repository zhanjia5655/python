# s='''bottle\nbag\nbig\napple'''
#sub 匹配替换  # #split 字符串分隔 #分组
import re
"""
(0, 'b') (1, 'o') (2, 't') (3, 't') (4, 'l') (5, 'e') (6, '\n') (7, 'b')
(8, 'a') (9, 'g') (10, '\n') (11, 'b') (12, 'i') (13, 'g') (14, '\n') (15, 'a')
(16, 'p') (17, 'p') (18, 'l') (19, 'e') """
# #sub 匹配替换
# # print(s)
# # '''bottle
# # bag
# # big
# # apple
# # '''
# # regex=re.compile('b\wg')
# # result=regex.sub('magedu',s)
# # print(1,result)
# # '''
# # 1 bottle
# # magedu
# # magedu
# # apple
# # '''
# # regex=re.compile('b\wg')
# # result=regex.sub('magedu',s,1)
# # print(1,result) #'''bottle\nmagedu\nbig\napple'''
# # regex=re.compile('\s+')
# # result=regex.subn('\t',s)
# # print(3,result) #3 ('bottle\tbag\tbig\tapple', 3)
#
# #split 字符串分隔
# s='''01  bottle
# 02  bag
# 03  big1
# 100     able'''
# for i,c in enumerate(s,1):
#     print((i-1,c),end='\n' if i%8==0  else ' ')
'''
(0, '0') (1, '1') (2, ' ') (3, ' ') (4, 'b') (5, 'o') (6, 't') (7, 't')
(8, 'l') (9, 'e') (10, '\n') (11, '0') (12, '2') (13, ' ') (14, ' ') (15, 'b')
(16, 'a') (17, 'g') (18, '\n') (19, '0') (20, '3') (21, ' ') (22, ' ') (23, 'b')
(24, 'i') (25, 'g') (26, '1') (27, '\n') (28, '1') (29, '0') (30, '0') (31, ' ')
(32, ' ') (33, ' ') (34, ' ') (35, ' ') (36, 'a') (37, 'b') (38, 'l') (39, 'e')
'''
# print(s.split())#['01', 'bottle', '02', 'bag', '03', 'big1', '100', 'able']
# result=re.split('[\s\d]+',s)#\s可以匹配空白字符，换行符，制表符
# print(1,result)#1 ['', 'bottle', 'bag', 'big', 'able']
# result=re.split('[\n]+',s)#1 ['01  bottle', '02  bag', '03  big1', '100     able']
# result=re.split('^[\s\d]+',s)
# print(2,result)#2 ['', 'bottle\n02  bag\n03  big1\n100     able']
# result=re.split('^[\s\d]+',s,re.M)#不能出结果，不清楚原因
# print(2,result)#2 ['', 'bottle\n02  bag\n03  big1\n100     able']
# regex=re.compile('^[\s\d]+',re.M)
# result=regex.split(s)
# print(3,result)#3 ['', 'bottle\n', 'bag\n', 'big1\n', 'able']
# regex=re.compile('\s+\d+\s+',re.M)
# result=regex.split(s)
# print(3,result)# 3 ['01  bottle', 'bag', 'big1', 'able']
#分组
s='''bottle\nbag\nbig\napple'''
# regex=re.compile('(b\w+)')
# result=regex.match(s)
# print(type(result))
# print(1,'match',result.groups())#1 match ('bottle',) match使用group ，分组用groups
# result=regex.search(s,1)
# print(2,'search',result.groups()) #2 search ('bag',)
#命名分组 group()方法用于返回整个匹配的字符串或指定分组的子串，而groups()方法用于返回一个包含所有分组匹配子串的元组。通常在需要处理分组时使用group()方法，而在需要获取所有分组匹配结果时使用groups()方法。
regex=re.compile('(b\w+)\n(?P<name2>b\w+)\n(?P<name3>b\w+)')
result=regex.match(s)
print(3,result)#3 <_sre.SRE_Match object; span=(0, 14), match='bottle\nbag\nbig'>
print(4,result.group(3),result.group(2),result.group(1))#4 big bag bottle
print(5,result.group(0).encode())#b'bottle\nbag\nbig'
print(6,result.group('name2'),result.group('name3'))#6 bag big
print(7,result.groups())#('bottle', 'bag', 'big')#返回元组，并没有kv对
print(7,result.groupdict())#{'name2': 'bag', 'name3': 'big'} 只返回命名分组
result=regex.findall(s)
# for x in result:
#     print(type(x),x)#<class 'tuple'> ('bottle', 'bag', 'big')
regex=re.compile('(?P<head>b\w+)')
result=regex.findall(s)
# print(result)#['bottle', 'bag', 'big'] 迭代findall，里元素没有group  finditem里元素有group
result=regex.finditer(s)
for x in result:
    print(type(x),x,x.group(),x.group('head'),x.groupdict(),x.groups())
# <class '_sre.SRE_Match'> <_sre.SRE_Match object; span=(0, 6), match='bottle'> bottle bottle {'head': 'bottle'} ('bottle',)
# <class '_sre.SRE_Match'> <_sre.SRE_Match object; span=(7, 10), match='bag'> bag bag {'head': 'bag'} ('bag',)
# <class '_sre.SRE_Match'> <_sre.SRE_Match object; span=(11, 14), match='big'> big big {'head': 'big'} ('big',)
'''
findall  finditer  匹配多次，每一次都是单次匹配类似（match search），可以用 group  groups  groupdic
'''
'''
match 才有 group  groups  groupdic 方法

在Python的re模块中，group()和groups()都是用于匹配对象的方法，但它们的用途不同。

group()方法：
group()方法返回整个匹配的字符串，或者指定分组的子串。如果正则表达式中没有分组，则只返回整个匹配的字符串。例如：
python
Copy code
import re
string = "hello world"
pattern = "hello (w.*)"
match_obj = re.match(pattern, string)
if match_obj:
    print("match_obj.group():", match_obj.group())
    print("match_obj.group(1):", match_obj.group(1))
else:
    print("No match!")
输出结果为：

csharp
Copy code
match_obj.group(): hello world
match_obj.group(1): world
在上面的例子中，group()方法返回了整个匹配的字符串"hello world"，而group(1)返回了第一个分组的子串"world"。

groups()方法：
groups()方法返回一个包含所有分组匹配子串的元组，如果正则表达式中没有分组，则返回一个空元组。例如：
python
Copy code
import re
string = "hello world"
pattern = "hello (w.*)"
match_obj = re.match(pattern, string)
if match_obj:
    print("match_obj.groups():", match_obj.groups())
else:
    print("No match!")
输出结果为：

scss
Copy code
match_obj.groups(): ('world',)
在上面的例子中，groups()方法返回了一个元组，包含了所有分组的匹配子串，即('world',)。

综上所述，group()方法用于返回整个匹配的字符串或指定分组的子串，而groups()方法用于返回一个包含所有分组匹配子串的元组。通常在需要处理分组时使用group()方法，而在需要获取所有分组匹配结果时使用groups()方法。'''