str=input("enter a name:")
def caluplwletter(letter):
    u=0
    l=0
    for i in letter:
        if i.isupper():
            u=u+1
        elif i.islower():
            l=l+1  
        else:
            pass  
    print("lower",l)       
    print("upper",u)
    print("strs",letter)

caluplwletter(str)    