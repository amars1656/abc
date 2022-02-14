pow2=[]
for x in range(10):
    pow2.append(2**x)
print(pow2)    
po2 = [2 ** x for x in range(10) if x > 5]
print(po2)
odd = [x for x in range(20) if x % 2 == 1]
print(odd)
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
print('p' in my_list)
print('a' in my_list)
print('c' not in my_list)