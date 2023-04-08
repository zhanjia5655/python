
'''
match函数：
match函数尝试从字符串的起始位置匹配正则表达式，如果匹配成功则返回匹配对象，否则返回None。它只匹配字符串的开头，因此如果你想匹配整个字符串，你需要使用'^'和'$'字符来指定开头和结尾。例如：
'''
import re
string = "hello world"
pattern = "hello"
match_obj = re.match(pattern, string)
if match_obj:
    print("match_obj.group():", match_obj.group()) #hello
else:
    print("No match!")
'''
search函数：
search函数在整个字符串中搜索正则表达式，如果匹配成功则返回匹配对象，否则返回None。它搜索整个字符串，因此你不需要使用'^'和'$'字符来指定开头和结尾。例如：
'''
import re
string = "hello world"
pattern = "world"
search_obj = re.search(pattern, string)
if search_obj:
    print("search_obj.group():", search_obj.group()) #world
else:
    print("No match!")
'''
findall函数：
findall函数返回字符串中所有与正则表达式匹配的子串，以列表形式返回。如果没有匹配到任何子串，则返回一个空列表。例如：
'''
import re
string = "hello world, hello python"
pattern = "hello"
findall_obj = re.findall(pattern, string)
if findall_obj:
    # print("findall_obj:", findall_obj) #['hello', 'hello']
    for _ in findall_obj:
        print(_,type(_)) #hello <class 'str'>
else:
    print("No match!")
'''
总结：
match()函数从字符串开头开始匹配，如果匹配成功就返回匹配对象；否则返回None。
search()函数会扫描整个字符串查找匹配，如果找到就返回匹配对象；否则返回None。
findall()函数会查找整个字符串中符合正则表达式的所有子串，并以列表形式返回。

'''