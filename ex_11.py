# -*- coding: utf-8 -*-

print("How old are you?",end='')
age = input()
print("How tall are you?",end="")
height = input()  #将输入全部当做字符串处理
print("How much do you weigh?",end='')
weight = input()

print("So, you're %r old, %s tall and %r heavy." % (age, height, weight))

