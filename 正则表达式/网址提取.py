import re
s='''
ftp://ftp.astron.com/pub/file/file-5.14.tar.gz
ftp://ftpgmplib.org/pub/gmp-5.1.2/gmp-5.1.2.tar.xz
ftp://ftp.vim.org/pub/vim/unix/vim-7.3.tar.bz2
http://anduin.linuxfromscratch.org/sources/LFS/1fs-packages/conglomeration//iana-etc/iana-etc-2.30.tar.bz2
http://anduin.linuxfromscratch.org/sources/other/udev-1fs-205-1.tar.bz2
http://download.savannah.gnu.org/releases/1ibpipeline/libpipeline-1.2.4.targz
http://download.savannah.gnu.org/releases/man-db/man-db-2.6.5.tar.z
http://download.savannahgnuorg/releases/sysvinit/sysvinit-2.88dsftar.bz2
http://ftp.altlinux.org/pub/people/legion/kbd/kbd-115.5.targz
http://mirror.hust.edu.cn/gnu/autoconf/autoconf-2.69.tar.xz
http://mirror.hust.edu.cn/gnu/automake/automake-1.14.tar.xz
'''
'''
.*ftp.*\.(?:gz|xz) #
ftp.*/(.*(?:gz|xz))
.*ftp.*/([^/]*\.(?:gz|xz))#捕获文件名分组
(?<=.*ftp.*/)[^/]*\.(?:gz|xz)#断言文件名前一定还有ftp'''

# regex=re.compile('^ftp.*\.(?:gz|xz)',re.M)
# result=regex.finditer(s)
# for aa in result:
#     print(aa.group())
#ftp://ftp.astron.com/pub/file/file-5.14.tar.gz
# ftp://ftpgmplib.org/pub/gmp-5.1.2/gmp-5.1.2.tar.xz
# regex=re.compile('.*ftp.*/([^/]*\.(?:gz|xz))',re.M)
# result=regex.finditer(s)
# for aa in result:
#     print(aa.group())

# s='''
# test@hot-mail.com 123123
# v-ip@magedu.com  12515
# web.manager@magedu.com.cn 152
# super.user@google.com
# a@w-a-com'''
# regex=re.compile('\w+[-.\w]*@[\w-]+(\.[\w-]+)+',re.M)
# result=regex.finditer(s)
# for i in result:
#     print(i.group())
#---------------------------------
s='''<a href=http://www.magedu.com/indexhtmltarget=blank>马哥教育</a>'''
regex=re.compile('<[^<>]+>(.*)<[^<>]+>',re.M)
result=regex.search(s)
print(result.group())
#-------------------------------------
'''
身份证验证
身份证验证需要使用公式计算，最严格的应该实名验证。'''
# s='''321105700101003
# 321105197001010030
# 11210020170101054X
# sdsdf
# 153456454154
# '''
# regex=re.compile('\d{17}[0-9xX] |\d{15}')
# result=regex.search(s)
# print(result.group())
#-------------------------
'''
# 强密码'''
# ^[a-zA-Z0-9_]{10,15}$