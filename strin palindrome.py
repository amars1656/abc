str=input("enter a name:")
def palindrome(st):
    left=0
    right=len(st)-1
    while right>=left:
        if not st[right]==st[left]:
            print("not palindrome")
        right=right+1
        left=left-1
    print("palindrome")        

             
    

palindrome(str)    