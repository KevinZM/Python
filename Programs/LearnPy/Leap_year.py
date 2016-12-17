# -*- coding:utf-8 -*-
# 计算今年是闰年嘛?判断闰年条件, 满足年份模400为0, 或者模4为0但模100不为0.
import time

def leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        #print '今年%s是闰年!' % year
        return year
    #else:
        #print '今年%s不是闰年!' % year

thisyear = time.localtime()[0]
leap_year(thisyear)

lastyear = thisyear + 20

for i in range(thisyear,lastyear):
    if leap_year(i):
        print '%s是闰年!'%i