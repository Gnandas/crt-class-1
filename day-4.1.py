def prime():
    n=int(input("enter the number"))
    print(prime)
prime()
prime()
prime()

def prime():
    f=1
    n=int(input("enter the number"))
    for i in range(2,n):
        if n%i==0:
            f=0
        if f==0:
           print("prime")
    else:
        print("not prime")
prime()
