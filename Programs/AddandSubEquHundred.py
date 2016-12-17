# -*- coding:utf-8 -*-
import itertools

# 设计程序求123456789之间添加'+','-',''之后的表达式等于100

'''我的解题思路:
   首先找到123456789数字和+-运算符之间的所有表达式,然后使用eval函数进行计算表达式的值
'''
# 数字队列
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 运算符
operator_list = ['+', '-', ' ']
# 最终表达式队列
last_list = [1, '', 2, '', 3, '', 4, '', 5, '', 6, '', 7, '', 8, '', 9]
# 生成运算符的表达式
ll = [''.join(x) for x in itertools.product(*[operator_list] * 8)]
# 存放所有最终表达式队列
lll = []
#print ll
# 将ll表达式插入num_list生成新的last_list最终表达式
for i in ll:
    x = 0  #

    # 使用运算符替换last_list元素中的''
    for j in range(len(last_list)):
        if j % 2 == 0:  # 过滤队列中奇数位(即数字)
            pass
        else:  # 将''全部替换成运算符
            last_list[j] = i[x]
            x += 1
    # print last_list
    mm = ''  # 最终表达式的字符串
    # 提取表达式中的字符
    for i in last_list:
        if i == ' ':  # ' '字符不再提取
            pass
        else:
            mm = mm + str(i)

    lll.append(mm)
#pint lll
# 计算表达式的值,等于100的打印出来
for i in lll:
    if eval(i) == 100:
        print '100 =', i
