mylist=[1,2,3,4,5,6,7,8]
def even(L):
    x=[]
    for i in L:
        if i%2==0:
            x.append(i)
    print(x)        

even(mylist)    