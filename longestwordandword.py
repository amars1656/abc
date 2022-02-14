li=["a","ab","abc","abcd"]
max=len(li[0])
word=li[0]
for i in li:
    if len(i)>max:
        max=len(i)
        word=i
print("logest word:",word,",","no.of word:",max)        