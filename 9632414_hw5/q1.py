class ShiraziDate:
    def __init__(self,year,month,day):
        c=0
        c=c+day
        self.day=c
        c=0
        c=c+month
        self.month=c
        c=0
        c=c+year
        self.year=c
    def add(self,other):
        x=self.datetoday()
        y=other.datetoday()
        res=x+y
        result=self.daytodate(res)
        return result
    def set(self,other):
        self.year=other.year
        self.month=other.month
        self.day=other.day
    def __add__(self,other):
        return self.add(other)
    def nextYear(self):
        self.year=self.year+1
    def nextMonth(self):
        return self.set(self.add(ShiraziDate(0,1,0)))
    def nextDay(self):
        x=ShiraziDate(0,0,1)
        self.set(self.add(x))
    def nextWeek(self):
        x=self.datetoday()
        x=x+7
        self.set(self.daytodate(x))
    def previousYear(self):
        self.year=self.year-1
    def previousMonth(self):
        x=self.datetoday()
        x=x-30
        self.set(self.daytodate(x))
    def previousDay(self):
        x=self.datetoday()
        x=x-1
        self.set(self.daytodate(x))
    def previousWeek(self):
        x=self.datetoday()
        x=x-7
        self.set(self.daytodate(x))
    def datetoday(self):
        return (self.year*360)+(self.month*30)+self.day
    def daytodate(self,day):
        d=day%30
        month=((day-(day%30))%360)//30
        year=day//360
        return ShiraziDate(year,month,d)
    def __str__(self):
        return str(self.year)+"/"+str(self.month)+"/"+str(self.day)
x=ShiraziDate(1396,9,25)
y=ShiraziDate(1396,10,4)

print(x+y)