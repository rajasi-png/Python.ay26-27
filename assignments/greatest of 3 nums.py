a=int(input("a input"))
b=int(input("b input"))
c=int(input("c input"))

#a is greatest
if a>b and a>c:
    print("a is the greatest")
#b is greatest
elif b>c and b>a:
    print("b is greatest")
#c is greatest
elif c>a and c>b:
    print("c is the greatest")
#a=b=c
elif a==b==c:
    print("a and b and c are all equal")
#a=b>c
elif a==b and a>c and b>c:
    print("a and b are the greatest")
#a=c>b
elif a==c and a>b and c>b:
    print("a and c are the greatest")
#b=c>a
elif b==c and b>a and c>a:
    print("b and c are the greatest")
else:
    print("invalid")
