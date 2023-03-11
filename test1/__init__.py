s='''bottle\nbag\nbig\napple'''
a=enumerate(s)
# for word in dict(a).values():
#     print(word)
for x in enumerate(s):
    if x[0] % 8 ==0:
        print()
    print(x,end=" ")
print('\n')