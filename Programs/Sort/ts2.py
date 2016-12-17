from Sort3 import Sort3
import random

a = Sort3()
list = []
T = True
while T:
    x = random.randint(1,10000)
    if x in list:
        continue
    else:
        list.append(x)
    l = len(list)
    if l == 10:
        break
    else:
        print l
print list
#x = a.bubble_sort(list)
x = a.quick_sort(list)
#x = a.selection_sort(list)
#x = a.insert_sort(list)
print x
print l