import turtle
wn=turtle.Screen()
def q3(a,b,c):
    t=turtle.Turtle()
    def bsortf(xs):
        for k in range(1,len(xs)):
            for n in range(0,len(xs)-1):
                if xs[n]>xs[n+1]:
                    xs=xs[:n]+[xs[n+1]]+[xs[n]]+xs[n+2:]
        return xs
    xs=[a]+[b]+[c]
    xs=bsortf(xs)
    t.forward(xs[0])
    t.right(90)
    t.forward(xs[1])
    t.home()
    
q3(300,500,400)