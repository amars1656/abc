num=int(input("enter a number:"))
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
         print(x * factorial(x-1))
         
factorial(num)
