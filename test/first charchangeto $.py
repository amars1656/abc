str="restart"
def string():
    a=str[0]
    for i in range(1,len(str)):
        if str[i]=="r":
            
            a=a+"$"
        else:
            a=a+str[i]
    print(a) 

string()           
