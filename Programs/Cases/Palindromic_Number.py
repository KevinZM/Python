#coding=utf-8
#sum为各位数之和
sum = 52
#we为位数,默认为5
we = 5

minimum = 0
d = sum/we
print d
if d > 9:
    we = 6
    start = 100000
end = 1000000
minimum = sum/we

for i in range(start,end):
    