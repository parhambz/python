class ShiraziSet():
    def __init__(self):
        self.xs=[]
    def add(self,z):
        if self.contains(z):
            return
        else:
            x=[]
            x=[z]+x
            self.xs=self.xs+x
    def contains(self,x):
        for i in self.xs:
            if x==i:
                return True
        return False
    def lenght(self):
        return len(self.xs)
    def __str__(self):
        res=""
        for  x in self.xs:
            res=res+" "+str(x)
        return res
    def __len__(self):
        return self.lenght()
