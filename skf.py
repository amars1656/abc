a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
c=int(input("enter a number3:"))
def greater():
    if a>b:
        if a>c:
            print(a)
        else:
            print(c)
    elif b>c:
            print(b)
    else:
            print(c)
greater()                                     