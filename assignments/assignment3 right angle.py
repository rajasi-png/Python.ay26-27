#right angle triangle

def pyth(a,b,c):
    return a^2 + b^2 == c^2

a=int(input("base side:"))
b=int(input("base side:"))
c=int(input("hypotenuse side:"))

if pyth(a,b,c)== True:
    print("is right angled triangle")
elif pyth(a,b,c)== False:
    print("not a right angled triangle")
    