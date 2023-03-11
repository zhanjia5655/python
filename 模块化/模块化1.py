print(dir())
print(dir(__name__))
import os
print(("-------------------------------"))
print(os.path)

import sys
import functools
print(dir())
print(__file__)
print(__name__)
print(("-------------------------------"))
print(sys.modules["__main__"])
print(("-------------------------------"))
import  sys
for a in sys.path:
    print(a)