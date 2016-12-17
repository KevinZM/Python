# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
import time


class Sort3(object):
    def __init__(self):
        pass

    def bubble_sort(self, list):
        l = len(list)
        if l < 2:
            return list
        j = l - 1
        while j > 0:
            for i in range(j):
                if list[i] > list[i+1]:
                    list[i],list[i+1] = list[i+1],list[i]
            j -= 1
        return list

    def quick_sort(self, list):
        l = len(list)
        if l < 2:
            return list
        key = list[0]
        big = []
        small = []
        for i in list[1:]:
            if i < key:
                small.append(i)
            else:
                big.append(i)
        print small
        print big
        return self.quick_sort(small) + [key] + self.quick_sort(big)

    def selection_sort(self, list):
        l = len(list)
        listx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if l < 2:
            return list

        for i in range(l):
            index = i
            for j in range(i+1,l):
                if list[index] > list[j]:
                    index = j
            list[i],list[index] = list[index],list[i]

        return list

    def insert_sort(self, list):
        l = len(list)
        if l < 2:
            return list
        for i in range(1,l):
            key = list[i]
            j = i - 1
            while j >= 0 and key < list[j]:
                list[j+1] = list[j]
                j -= 1
            list[j+1] = key
        return list