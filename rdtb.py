num=int(input("enter a number:"))
def factorial(n):
    fact=1
    if n<=0:
        print(n)
    else:
        for i in range (1,n+1):
            fact=fact*i
        print(fact)    

factorial(num)
