# -*- coding: utf-8 -*-

a = "I am 6'2\" tall."
b = 'I am 6\'2" tall.'
print(a)
print(b)

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
# 三个单引号 和 三个双引号 一样的效果

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("\x38")  # 值为十六进制38 的字符
print("\450")  # 值为八进制450的 字符

while True:
    for i in ["/","-","|","\\","|"]:
        print("%s\r" % i, end='')  # \r 回车，只是回到本行的开头，并不换行！！