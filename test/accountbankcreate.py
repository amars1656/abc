class account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposite(self,b):
        self.balance=b+self.balance
        return (f"deposit accepted {b}")

    def withdraw(self,x):
        if x>self.balance:
            return ("fund unavailable")
        else:
            self.balance=x-self.balance
            return ("withdraw accepted") 

g=int(input("enter a deposite money:"))
xe=int(input("enter a withdrwa aamount:"))
d=account("jose",100)
print(d.owner)
print(d.balance)
print(d.deposite(g))
print(d.withdraw(xe))