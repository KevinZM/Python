# -*- coding:utf-8 -*-

class SortClass(object):

    def __init__(self):
        pass

    #冒泡排序,列表中数据两两对比,对比一次之后,最大值被排到最后面,因此下次再排序就可以不排最后一个,效率比较高
    def bubble_sort(self, list):

        length = len(list)
        while length > 0:
            for j in range(length-1):
                if list[j] > list[j+1]:
                    list[j],list[j+1] = list[j+1],list[j]
                print '%s:%s'%(j,list)
            print list
            length -= 1
        return list

    #快速排序,将一个列表按照基准值分成两部分,分别是大于该基准值和小于该基准值,然后递归实现,注意递归的结束!!!
    def quick_sort(self, list):
        #递归结束判断!!!
        if list == []:
            return []

        key = list[0]
        big_list = []
        small_list = []

        #注意开始值,选取的基准值是第一个,所以从队列第二个开始!!!
        for i in list[1:]:
            if i > key:
                big_list.append(i)
            else:
                small_list.append(i)

        return self.quick_sort(small_list) + [key] + self.quick_sort(big_list)

    #插入排序,在队列中取第一个值作为基准,然后将后续的元素和之前的基准进行比较后插入基准队列
    def insert_sort(self, list):

        length = len(list)
        #判断队列长度
        if length < 2:
            return list

        for i in range(1,length):
            key = list[i]
            j = i - 1
            #找到一个比key值小的元素,然后将元素整体后移,最后将key放到比key小的元素后面
            while j >= 0 and key < list[j]:
                list[j+1] = list[j]
                j = j - 1
                #print '%s:%s:%s:%s'%(i,j,key,list)
            list[j+1] = key
            #print key,list[j+1]
        return list

    #选择排序,找到最小的放在第一位,然后找到第二小的放到第二位... ...
    def selection_sort(self, list):

        length = len(list)
        if length < 2:
            return list

        for i in range(length):
            index = i
            for j in range(i+1,length):
                if list[index] > list[j]:
                    index = j
            list[i], list[index] = list[index], list[i]
            print '%s:%s:%s'%(i, j, list)
        return list




