import turtle
class ShiraziPath:
    def __init__(self):
        self.points=[]
    def addPoint(self,x,y):
        self.points=self.points+[[x,y]]
    def f(self,a,b):
        return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)
    def length(self):
        res=0
        for x in range(len(self.points)-1):
            res=res+self.f(self.points[x],self.points[x+1])
        return res
    def __len__(self):
        return int((self.length())//1)
    def __add__(self,other):
        newpoints=self.points+other.points
        res=ShiraziPath()
        for a in newpoints:
            res.addPoint(a[0],a[1])
        return res
    def draw(self):
        turtle.Screen()
        t=turtle.Turtle()
        t.up()
        t.goto(self.points[0][0],self.points[0][1])
        t.down()
        for a in self.points:
            t.stamp
            t.goto(a[0],a[1])
    def __str__(self):
        return str(self.points)
a=ShiraziPath()
a.addPoint(50,0)
a.addPoint(0,100)
a.addPoint(100,200)
print(len(a))
a.draw()
