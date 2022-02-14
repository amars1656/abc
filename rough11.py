str=input("enter a string:")
x=list(map(lambda a:a.isdigit(),str))
print(x)
mylist=[1,2,3,4,5,6,7,8,9,10]
y=list(filter(lambda a: (a%2==0),mylist))
print("even number:",len(y))
mylist=[1,2,3]
lst=[4,5,6]
x=[]
a=0
for i in mylist:
for u in lst:
    a=i+u
    x.append(a)
print(x)        