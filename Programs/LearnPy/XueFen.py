# -*- coding:utf-8 -*-
# 每门课程的成绩分为五个等级：A,B,C,D,F(注意没有E),它们分别代表可以获得4,3,2,1,0个绩点.
# 现在给你一个由大写字母构成的列表L，请你计算平均绩点，保留小数点后两位。
# 若L中包含非法成绩等级，则输出-1.
# 如：
# L = ["A", "B", "C", "D", "F"]
# 则输出2.00
L = ['A','B','C','D']
M = ['F','D','C','B','A']
y = 0.00
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