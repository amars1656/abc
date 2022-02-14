class book():
    def __init__(self,tittle,author,page):
        self.tittle=tittle
        self.author=author
        self.page=page

    def __str__(self):
        return (f"{self.tittle} by {self.author}")

    def __len__(self):
        return self.page
    
    def __delete__(self):
        return ("book deleted ")

b=book("python","jose",200)
print(len(b))
print(b.author)
print(b.tittle)
print(str(b))
print(delete())
