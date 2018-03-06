# -*- coding: utf-8 -*-

print("."*10)
a1 = "C"
a2 = "h"
a3 = "e"
a4 = "e"
a5 = "s"
a6 = "e"
print(a1+a2+
      a3+a4+a5)

formatter = "%r %r %r %r"
print(formatter % (
    "I had this thing.",
    "That.",
    "But it didn't sing.", #注意此处字符串中有单引号，外面打印出的是双引号！！
    "So i said good night."
))
