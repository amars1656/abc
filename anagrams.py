from collections import counter
mylist=["bcda","abce","cdba","cbea","adcb"]
str="abcd"
result=list(filter(lambda a:counter(str)==counter(a),mylist))
print("anagrams abcd is:",result)