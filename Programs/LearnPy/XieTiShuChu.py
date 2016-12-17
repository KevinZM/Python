a = 1
b = 2
for i in range(1,101):
    if i < 10:
        print i,"",
    else:
        print i,
    if i == a:
        print
        a = a + b
        b = b + 1