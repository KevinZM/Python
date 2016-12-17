# -*- coding:utf-8 -*-
from SortClass import SortClass
import random


a = SortClass()
list = [1,2,3,4,5,6,7,8,9]

random.shuffle(list)
print '待排序列表:%s'%list
#
# new_list = a.bubble_sort(list)
#
# print '排序后列表:%s'%new_list

#x = a.quick_sort(list)
#x = a.insert_sort(list)
x = a.selection_sort(list)
print x