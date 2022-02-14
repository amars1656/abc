str="the quick brown for"
x=str.split()
lis=[]
for i in x:
    if len(i)>3:
        lis.append(i)
print(lis)        
