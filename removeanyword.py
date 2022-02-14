str="python"
lis=[]
st=""
n=int(input("enter a index:"))
for i in str:
    lis.append(i)
lis.pop(n)
for a in lis:
    st=st+a
print(st)        
