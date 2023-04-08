import re
# s='''bottle\nbag\nbig\napple'''
# for i,c in enumerate(s,1):
#     print((i-1,c), end='\n' if i%8==0 else " ")
"""
(0, 'b') (1, 'o') (2, 't') (3, 't') (4, 'l') (5, 'e') (6, '\n') (7, 'b')
(8, 'a') (9, 'g') (10, '\n') (11, 'b') (12, 'i') (13, 'g') (14, '\n') (15, 'a')
(16, 'p') (17, 'p') (18, 'l') (19, 'e') """
#
# print('------match--------')#必须从行首开始匹配，单次匹配
# result=re.match('b',s)
# print(1,result)#<_sre.SRE_Match object; span=(0, 1), match='b'>
# result=re.match('a',s)
# print(2,result)
# result=re.match('[^a]',s,re.M)
# print(3,result)#3 <_sre.SRE_Match object; span=(0, 1), match='b'>
# result=re.match('[^a]',s,re.S)
# print(4,result)#4 <_sre.SRE_Match object; span=(0, 1), match='b'>
'''
正则表达式 '^a' 匹配以字母 "a" 开头的字符串，而 '[^a]' 匹配任何不是字母 "a" 的单个字符。
需要注意的是，'^a' 和 '[^a]' 的匹配结果是互斥的，即一个字符要么匹配 '^a'，要么匹配 '[^a]'。'''
# result=re.match('^a',s,re.M) #锚定行首
# print(5,result)#5 None
# result=re.match('^a',s,re.S)
# print(6,result)#6 None
# #先编译
# regex=re.compile('b')
# result=regex.match(s)
# print(7,result)
# result=regex.match(s,15) #从索引15开始匹配
# print(8,result) #None
#s='''bottle\nbag\nbig\napple'''
# print('------search--------')#，从任意位置匹配，单次匹配
# result=re.search('b',s)
# print(9,result)#9 <_sre.SRE_Match object; span=(0, 1), match='b'>
# regex=re.compile('b')
# result=regex.search(s,1)
# print(10,result)#10 <_sre.SRE_Match object; span=(7, 8), match='b'>
# regex=re.compile('^b',re.M)#找到一次就反馈
# result=regex.search(s)
# print(11,result)#11 <_sre.SRE_Match object; span=(0, 1), match='b'>
# print('------fullmatch--------')#，从头到未与s完全匹配
#s='''bottle\nbag\nbig\napple'''
# result=re.fullmatch('bag',s)
# print(12,result)#None
# regex=re.compile('bag')
# result=regex.fullmatch(s)
# print(13,result)#None
# regex=re.compile('bag')#找到一次就反馈
# # result=regex.fullmatch(s,7,10)
# # print(14,result)#<_sre.SRE_Match object; span=(7, 10), match='bag'>
# result=regex.fullmatch(s,7)
# print(15,result)#None
# print('------findall--------')#，范围所有的匹配项
# result=re.findall('b',s)
# print(1,result)#1 ['b', 'b', 'b']#默认多行模式
s='''bottle\nbag\nbig n\napple'''
# regex=re.compile('^b.*')# 不加 ['bottle'] re.S ['bottle\nbag\nbig\napple'] re.M ['bottle', 'bag', 'big']
# result=regex.findall(s)
# print(2,result)#2 ['b']#不是单行也不是多行模式，匹配到换行符就停止
# regex=re.compile('b')
# result=regex.findall(s,7)
# print(3,result)#3 ['b', 'b']不是行首 找到b全匹配
# regex=re.compile('^b',re.M)#regex=re.compile('^b\w*' 每行开始匹配
# result=regex.findall(s)
# print(4,result)#4 ['b', 'b', 'b']
# regex=re.compile('^b',re.S)
# result=regex.findall(s)
# print(5,result)#['b'] 匹配单个
'''多行默认^字符匹配每行行首 ，单行默认是^单行行首，回车按\n处理 ，不添加单行或者多行，匹配不超过回车，网页上测试是单行模式结果，有些不同'''
# print('------finditer--------')#，返回迭代器
# regex=re.compile('^b\w*',re.M)#regex=re.compile('^b\w*'
# result=regex.finditer(s)
# print(6,result,type(result))#6 <callable_iterator object at 0x000000356D12C518> <class 'callable_iterator'>
# print(7,next(result))#7 <_sre.SRE_Match object; span=(0, 6), match='bottle'>
# print(8,next(result))#8 <_sre.SRE_Match object; span=(7, 10), match='bag'>
s='''bottle\nbag\nbig n\napple'''
import re
"""
(0, 'b') (1, 'o') (2, 't') (3, 't') (4, 'l') (5, 'e') (6, '\n') (7, 'b')
(8, 'a') (9, 'g') (10, '\n') (11, 'b') (12, 'i') (13, 'g') (14, '\n') (15, 'a')
(16, 'p') (17, 'p') (18, 'l') (19, 'e') """
# print('------findall--------')#
# result=re.findall('b',s)
# print(result)#['b', 'b', 'b']
regex=re.compile('^b')
result=regex.findall(s)
print(result) #['b']
regex=re.compile('^b',re.M)
result=regex.findall(s,7)
print(result) #['b', 'b']
regex=re.compile('^b',re.S)
result=regex.findall(s)
print(result) #['b']
regex=re.compile('^b',re.M)
result=regex.findall(s,7,10)
print(result) #['b']
