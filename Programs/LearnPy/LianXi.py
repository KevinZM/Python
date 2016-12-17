# -*- coding:utf-8 -*-
import math
# print dir(math)
strCN = '春暖花开'
# print strCN
# print strCN[0:3]
# print strCN[-12:]
# print strCN[3:6]
# print len(strCN)
# print strCN*2
# print strCN.find('花')
# print strCN.replace('花','花不')
# print strCN[-12:]
# testList = ['独上高楼,望尽天涯路','衣带渐宽终不悔,为伊消得人憔悴','蓦然回首,那人却在灯火阑珊处']
# print len(testList)
# for i in testList:
#     print '%s'%i
#
# testDict = {'time':'时间','machine':'机器','timemachine':'时间机器'}
# print testDict['time']
# print True + 2#Trueis 1 and False is 0
# print bool(1)
# print bool(0)
# print bool(-1)
# L = [1,2,3]
# M = [1,2,3]
# print L == M
# print L is M
#等于检查两个变量是不是相等,而 is 检查两个变量是不是引用同一个对象。

uniStr = u'unicode 的字符串'
# print uniStr
# print len(uniStr)
# print uniStr[10]
# print str(u'should be ASCII')#convert a     unicode string to ASCII string print unicode('going to be unicode')
#slice a string #第七个字符到第十个字符
# print uniStr[7:11] #同上,但是只有偶数字符
# print uniStr[7:11:2]#only even char #从右向左
#
# print uniStr[::-1]#right to left #从右向左,每隔两个
# print uniStr[::-2]#and one every other #第一个是错误,第二个正确
# print uniStr[7:11:-1]#why doesn't it work? print uniStr[11:7:-1]#because...
# print uniStr[11:7:-1]
# testList = [1,5,3,4,2]
# testList1 = [0,8,9]
# print testList1 + testList
# print testList * 2
# testList.sort()
# print testList
#
# testFile = open('/Users/zhangmin/app.txt','w')
# testFile.write('I\'m leaenning Python!')
# testFile.write('\n\n')
# ll = ('jkagfkaf','jhfiffsj','afasfsf')
# lla = 'hjksfahsaofskfshlafsahfl'
# testFile.writelines(ll)
# testFile.write('\n\n')
# testFile.writelines(lla)
# testFile.close()
# #to read
# testFile = open('/Users/zhangmin/app.txt','r')
# #testStr = testFile.readline()
# #print testStr
# testStr = testFile.read()
# print testStr
# testFile.close()
# a,b,c,d = 'HTML'
# print a,b,c,d
# a = b = c = d = 'HTML'
# print a,b,c,d
# L = [1,2,3,4]
# print L[1:]
# while L:
#     front,L = L[0],L[1:]
#     print front,L
#
# from sys import stdout
# temp = stdout     #for later use
# outputFile = open('out.txt','a')
# stdout = outputFile
# stdout.write('just a test') #回复输出流
# stdout = temp     #restore the output stream
# print >> outputFile,'changed for a     little whie\n'
# from sys import stderr
# print >> stderr,'error!\n'
# x = [('XHTML', 'CSS'), ('JavaScript', 'Python')]
# for (a, b) in x:
#     print (a, b)
# for line in open('names.txt'):
#     print line.upper()
# testDict = {'name':'Chen Zhe','gender':'male'}
# for key in testDict:
#     print key + ':'+ testDict[key]
#iterator in list comprehension
#list comprehension 中的迭代器
# testList = [line for line in open('names.txt')]
# print testList
# print list(open('names.txt'))
# print ('').join(open('names.txt'))
# for i in range(5):
#     print str(i) + ' is the current value'
# else:
#     print '--------------finished----------------'
# for i in range(2,9,4):#for(i=0;i<5;i++)
#     print str(i) + ' is the current value'
# else:
#     print '--------------finished----------------'
L1 = [1,3,5,7]
L2 = [2,4,6,8]
#使用 zip 将两个列表合并 print zip(L1,L2)
for (a,b) in zip(L1,L2):
    print (a,b)
print zip(L1,L2)