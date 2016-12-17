# -*- coding: iso-8859-15 -*-
# a = 'cagy'
# b = 3
# print ord('x')
# x = []
# for i in range(0,len(a)):
#     if ord(a[i]) < 121:
#         x.append(chr(ord(a[i])+b))
#     if ord(a[i]) > 120:
#         x.append(chr(ord(a[i]) + b - 26))
#
# print x
#
#
# ch = []
# for m in a:
#     if ord(m) + b > ord('z'):
#         ch.append(chr((ord(m) + b - 26)))
#     else:
#         ch.append(chr((ord(m) + b)))
# print ("".join(ch))
#
#
# currency = u"€"
# print ord(currency)
#
# print currency
# a = 3
# b = 2
# print a+b,a-b
# ??????????????A,B,C,D,F(????E),??????????4,3,2,1,0???.
# ????????????????L???????????????????
# ?L?????????????-1.
# ??
# L = ["A", "B", "C", "D", "F"]
# ???2.00
L = ['A','B','C','D']
M = ['F','D','C','B','A']
y = 0
x = 0
for i in L:
    z = 0
    for j in range(len(M)):
        if i == M[j]:
            y = y + j
            z = z + 1
    if z == 0:
        x = x + 1
if x > 0:
    y = -1
    print y
else:
    y = y/(len(L))
    print "%.2f" %y
