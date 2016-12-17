#coding=utf-8
import random

from Sort1 import Sort1

a = Sort1()

list = [1,2,3,4,5,6,7,8,9]

random.shuffle(list)
print '待排序列表:%s'%list

#x = a.quick_sort(list)
#x = a.bubble_sort(list)
#x = a.insert_sort(list)
x = a.selection_sort(list)
print x