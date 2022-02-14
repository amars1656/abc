class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

blu=parrot("blu",10)        
woo=parrot("woo",15)
print("blu is a {}".format(blu.__class__.species))
print("woo is also a {}".format(woo.__class__.species))