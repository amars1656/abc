a=0
b=1
c=0
while c<50:
    c=a+b
    a=b
    b=c
    print(c)

for i in range(50):
    c=a+b
    a=b
    b=c
    print(c) 
    if c>50:
        break;       