mylist=[1,6,3,7,5]
x=tuple(mylist)
print(x)
print(type(x))
mytuple=(1,3,4,5)
y=list(mytuple)
print(y)
print(type(y))
myset={2,3,4,5}
z=list(myset)
print(z)
print(type(z))
w=set(mylist)
print(w)
print(type(w))
h={2,}
print(type(h))
mydict={"key1":2,"key2":3}
print(type(mydict))
j=list(mydict)
print(j)
print(mydict)
mydict.get("key1")
mydict.get("key3")