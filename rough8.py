from typing import ValuesView


mydict={"key1":1,"key2":2,"key3":4,"key4":5}
dict={}
mydict["key4"]="9"
mydict["key5"]="0"
for i in mydict:
    x=mydict[i] 
    print(x)  
print("key1" in mydict)  
for x in mydict.items():
    print(x)  
x=list(mydict)
print(x)
print(x)  
c=tuple(mydict)
print(c)