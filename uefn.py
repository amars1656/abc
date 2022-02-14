n=int(input("enter a number:"))
def fallinrange(num):
    for i in range(1,6):
        if i==num:
            print(num,"is their in range")
            break    
    else:
        print(num,"is not their in range")        
 
fallinrange(n)        