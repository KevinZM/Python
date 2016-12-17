def gu_shen(n):

    if n < 3:
        return n
    temp = 1
    for i in range(2,n+1):
        temp = temp + i
        if temp > n:
            die_ci = i - 2
            break
    money = n - die_ci-die_ci
    return money

day = input()
print gu_shen(day)