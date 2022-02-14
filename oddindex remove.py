str=input("enter a string:")
a=""
for i in range(len(str)):
    if i%2==0:
        a=a+str[i]
print(a)        