# -*- coding:utf-8 -*-
num = raw_input("请输入一个三位数字")
a = int(num[0])
b = int(num[1])
c = int(num[2])
if a*a*a+c*c*c==b*b*b:
	print '%s是水仙花数！'%num
else:
	print '%s不是水仙花数！'%num