# -*- coding:utf-8 -*-


def zhuanhuan(num):
    alabo = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    hanzi = ('壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', '零')
    conversion = []
    for i in num:
        for j in range(len(alabo)):
            if i == alabo[j]:
                conversion.append(hanzi[j])
    for element in conversion:
        print element

    size = len(conversion)
    if size == 1:
        return conversion[0]
    if size == 2:
        if conversion[1] == '零':
            return conversion[0] + '拾'
        return conversion[0] + '拾' + conversion[1]
    if size == 3:
        if conversion[2] == '零' and conversion[1] == '零':
            return conversion[0] + '佰'
        if conversion[2] == '零' and conversion[1] != '零':
            return conversion[0] + '佰' + conversion[1] + '拾'
        if conversion[2] != '零' and conversion[1] == '零':
            return conversion[0] + '佰' + conversion[1] + conversion[2]
        if conversion[2] != '零' and conversion[1] != '零':
            return conversion[0] + '佰' + conversion[1] + '拾' + conversion[2]



i = 0
while True:
    number = raw_input("请输入数字:")
    #number = int(number)
    print zhuanhuan(number)
    i += 1
    if i >5:
        break
