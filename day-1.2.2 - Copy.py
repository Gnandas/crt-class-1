m=int(input(81))
c=int(input(81))
p=int(input(81))

if m>80 and c>80 and p>80:
    print("a+")
elif m>60 and m<80 and c>60 and c<80 and p>60 and p<80:
    print("b+")
else:
    print("other wise pass")