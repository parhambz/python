import turtle
turtle.Screen
turtle.tracer(10)
def q5(f):
    t=turtle.Turtle()
    v=[x for x in range (101)]
    def draw(xs):
        t.left(90)
        t.up()
        t.goto(-200,-200)
        t.down()
        t.forward(500)
        t.right(135)
        t.forward(20)
        t.right(180)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.up()
        t.goto(-200,-200)
        t.down()
        t.left(135)
        t.forward(500)
        t.right(135)
        t.forward(20)
        t.right(180)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.up()
        t.goto(-200,-200)
        t.down()
        turtle.tracer(10)
        for x in v :
            t.goto(x-200,f(x/10)*10-200)
    draw(v)
q5(lambda x:x*x)