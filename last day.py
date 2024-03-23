def p(n):
    if n%2==0:
        print(n**2)
    else:
        print(n**3)
j=[2,5,8,6]
b=map(p,j)
print(list(b))