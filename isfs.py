n=int(input("enter a number:"))
def primeno(num):
    if num==1:
        print(num,"is not prime number")
    elif num==2:
        print(num,"is prime number")    
    else:
        for i in range(2,num):
            if (num%i==0):
                print(num,"is not prime number")
                break
            else:
                print(num,"is  prime number")  

primeno(n)

