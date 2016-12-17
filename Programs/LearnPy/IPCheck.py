# -*- coding:utf-8 -*-
#s = "202.001.32.24"
m = "."
a =[]
num = 0
x = True
while x:
    s = raw_input("请输入IP:")
    #number = int(number)
    a = s.split(m)
    for i in a:
        if (i.isdigit() == True and 0 <= int(i) <= 255):
            num = num + 1
    if num == 4:
        print 'Yes,your IP is right!'
    else:
        print 'No,your IP is wrong!'
    y = raw_input("Continue or Stop?(Y/N)")
    if(y == 'y' or y == 'Y'):
        x = True
    else:
        x = False