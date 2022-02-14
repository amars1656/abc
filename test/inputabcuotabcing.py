str=input("enter a number:")
if len(str)>=3:
    if str[-3:]=="ing":
        str=str+"ly"
        print(str)
    else:
        str=str+"ing"
        print(str)
else:
    print(str)            