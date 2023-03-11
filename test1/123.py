# print('1,2,3')

from pathlib import Path
import shutil
p=Path()
p=p/"a"/"b"
print(p.name,p.suffix)

# print(p.cwd(),p.is_dir())
# print(p.absolute().parents)
# for x in p.absolute().parents:
#     print(x)
# #shutil.copyfile('1.py',"111.py")
# shutil.move("111.py","a")

pp=Path("d:/123/aaa.txt")
print(pp.parent,pp.name)