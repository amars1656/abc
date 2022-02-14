def count():
    dict={}
    for n in str1:
        if n in dict:
            dict[n]=dict[n]+1
        else:
            dict[n]=1
    print(dict)

count()               
    