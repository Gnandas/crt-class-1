a=0
b=1
print(a)
print(b)
for i in range(3,11):
    c=a+b
    print(c)
    a=b
    b=c

    for i in range(1,6):
        for j in range(1,5):
            print(i,j)