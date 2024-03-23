num=int(input("enter number"))
if num%3==0 and num%5==0:
    print("great")
elif num%3==0 and num%9:
    print("good")
elif num%3==0 and num%7==0:
    print("ok")
else:
    print("other wise not ok")

