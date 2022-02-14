str=input("enter a string:")
def char():
    if len(str)>=2:
        print( str[0:2]+str[-2:])

    else:
        print("empty string")  

char()          