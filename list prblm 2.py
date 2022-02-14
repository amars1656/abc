y=[1,2,3,3,3,4,5]
def list(L):
    x=[]
    for i in L:
        if i not in x:
            x.append(i)
    print(x)

list(y)