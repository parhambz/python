import random
def readFile(name):  # read file from txt
    try:
        file = open(name, "r")
        lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("file not found")
def joinLines(xs):  # join lines and make a string
    res = ""
    for x in xs:
        res = res + x
    return res
def sep(string):  # seperate with seprators
    string = string + " "
    seps = [" ", "(", ")", ":", ";", "=", ",", "&", "|", "~", "\n"]
    res = []
    temp = ""
    for x in string:
        if x in seps:
            if x != " " and x != "\n":
                res = res + [temp] + [x]
                temp = ""
            else:
                res = res + [temp]
                temp = ""
        else:
            temp = temp + x

    return [x for x in res if x != ""]
def sepModules(xs):  # seprate modules from each other
    temp = []
    res = []
    for x in xs:
        if x == "module":
            temp = ["module"]
        else:
            if x != "endmodule":
                temp = temp + [x]
            else:
                temp = temp + ["endmodule"]
                res = res + [temp]
    return res
def lineOne(xs):  # code ye module ro migire objectesho misaze input output ro ham ezafe mikone tahesh objectesho mide
    modules.addModu(xs[1])
    temp = modules.modus[-1]
    k = 0
    for x in xs:
        if x == ":":
            break
        k = k + 1
    inout = xs[2:k]
    k = 0
    for x in inout:
        if x == "input":
            temp.input(inout[k + 1])
        if x == "output":
            temp.output(inout[k + 1])
            a = wire(inout[k + 1], len(temp.wires))
            temp.wires = temp.wires + [a]
        k = k + 1
    return temp
def removeP(ys):#remove () and seprate it to line
    xs=[]
    xs=xs+ys
    k=1
    for x in xs[1:]:
        m=0
        a=-1
        b=1
        for y in x:
           if y=="(":
               a=m
               break
           m=m+1
        m=-1
        for y in x[::-1]:
           if y==")":
               b=m
               break
           m=m-1
        if b!=1  and a!=-1:
            name=str(random.randrange(10000))
            p=xs[k][a+1:len(xs[k])+b]
            xs[k]=xs[k][:a]+[name]+xs[k][1+b+len(xs[k]):]
            xs=xs[:k]+[["wire",name,"="]+p]+xs[k:]
            k=k+1
        k=k+1
    return xs
def gnot(ys,mobject):
    x=[]
    x=x+ys
    xs=x
    k=0
    for x in xs:
        m=0
        for y in x:
            if y=="~":
                w=mobject.addWire("*"+x[m+1])
                w.content(["~",x[m+1]])
                xs[k]=xs[k][:m]+["*"+xs[k][m+1]]+xs[k][m+2:]
            m=m+1
        k=k+1
    return xs
def body(xs, mobject):
    k = 0
    for x in xs:
        if x == ":":
            xs[k] = ";"
        k = k + 1
    body = []
    temp = []
    for x in xs:
        if x == ";":
            body = body + [temp]
            temp = []
        else:
            temp = temp + [x]
    body=removeP(body)
    body=gnot(body,mobject)
    mobject.body(body)
    setWires(body, mobject)
    wireContent(body, mobject)
def setWires(xs, mobject):  # give body and add wires
    for y in xs:
        k = 0
        for x in y:
            if x == "wire":
                temp = wire(y[k + 1], len(mobject.wires))
                working = mobject
                working.wires = working.wires + [temp]
def wireContent(xs, mobject):  # give body and module object and set wire contents
    for x in xs:
        k = 0
        for y in x:
            '''if y=="~":
                wireContent=["~"]+[x[k+1]]
                wireName="~"+x[k+1]
                wireKey = mobject.wireNameToKey(wireName)
                wire=mobject.wires[wireKey]
                wire.content(wireContent)'''
            if y == "=":
                wireContent = x[k + 1:]
                wireName = x[k - 1]
                wireKey = mobject.wireNameToKey(wireName)
                wire = mobject.wires[wireKey]
                wire.content(wireContent)
            k = k + 1
        '''if len(x)!=3:
            for y in x:
                if y=="=":
                    wireContent=[x[k+1]]+[x[k+2]]+[x[k+3]]
                    wireName=x[k-1]
                    wireKey=mobject.wireNameToKey(wireName)
                    wire=mobject.wires[wireKey]
                    wire.content(wireContent)
                k=k+1
        if len(x)==3:
            for y in x:
                if y=="=":
                    wireContent=[x[k+1]]
                    wireName=x[k-1]
                    wireKey=mobject.wireNameToKey(wireName)
                    wire=mobject.wires[wireKey]
                    wire.content(wireContent)
                k = k + 1'''
def errorSet(enum,file):  # give error num and write in txt and exit
    if enum==1:
        file.write("error code : 1")
def createE():
    error=open("error.txt","w")
    l=["=" for x in range(125)]+["\n"]
    line=""
    for x in l:
        line=line+x
    error.write(line)
    l=["*"]+[" " for x in range(55)]+["Symtax result"]+[" " for x in range(55)]+["*"]+["\n"]
    title=""
    for x in l:
        title=title+x
    error.write(title)
    error.write(line)
    return error
def graphMaker(mobject):
    g=graph(mobject.name)
    op=["&","|"]
    k=0
    for x in mobject.body:
        m=0
        for y in x :
            if y =="=":
                if len(x)==5:
                    n=g.addNode(x[m+2])
                    n.addV(x[m-1])
                    n.addV(x[m +3])
                    n.addV(x[m +1])
                if len(x)==3:
                    n = g.addNode(x[m])
                    n.addV(x[m - 1])
                    n.addV(x[m + 1])

            m=m+1
        k=k+1



class modu:
    def __init__(self, name, key):
        x = ""
        x = x + name
        self.name = x
        x = 0
        x = x + key
        self.key = x
        self.wires = []
        self.inp = []
        self.out = []
    def body(self,body):
        x=[]
        x=x+body
        self.body=x
    def input(self, name):
        x = ""
        x = x + name
        self.inp += [x]

    def output(self, name):
        x = []
        x = x + [name]
        self.out = self.out + x

    def wireNameToKey(self, name):
        for x in self.wires:
            if x.name == name:
                return x.key

    def res(self):
        r = [[x.name] for x in self.wires if x.name in self.out]
        z = [x.name for x in self.wires]
        while True:
            k = 0
            m = 0
            for a in r:
                l = 0
                for x in a:
                    if x in z:
                        q = self.wireNameToKey(r[k][l])
                        q = self.wires[q]
                        # r[k][l]=q.con
                        r[k] = r[k][:l] + q.con + r[k][l + 1:]
                        m = 2
                    l = l + 1
                k = k + 1
            if m == 0:
                break
        return r
    def addWire(self,wname):
        w= wire(wname,len(self.wires))
        self.wires=self.wires+[w]
        return w
    def __str__(self):
        result = []
        for x in self.res():
            res = ""
            for y in x:
                res = res + y
            result = result + [res]
        return str(result)
class modus:
    def mnameToKey(self, name):
        for x in self.modus:
            if x.name == name:
                return x.key

    def __init__(self):
        self.modus = []

    def addModu(self, name):
        key = len(self.modus)
        a = modu(name, key)
        self.modus = self.modus + [a]
        return key
class wire:
    def __init__(self, name, key,ng=False):
        x = ""
        x = x + name
        self.name = x
        x = 0
        x = x + key
        self.key = x
        self.con = []

    def content(self, xs):
        x = []
        x = x + ["("] + xs + [")"]
        self.con = x

    def __str__(self):
        return str(self.con)
class graph:
    def __init__(self,mname):
        x=""
        x=x+mname
        self.name=x
        self.vectors=[]
        self.nodes=[]
    def addNode(self,type):
        temp=node(len(self.nodes),type)
        self.nodes=self.nodes+[temp]
    def addVector(self,name,begin,des):
        temp=vector(name,begin,des,len(self.vectors))
        self.vectors=self.vectors+[temp]
class node:
    def __init__(self,id,type):
        self.type=type[0]
        x=0
        x=x+id
        self.key=x
        self.vector=[]
    def addV(self,name):
        v=vector(name)
        self.vector=self.vector+[v]
        return v
class vector:
    def __init__(self,name):
        x=""
        x=x+name
        self.name=x
        x = 0
        x = x + id
        self.key = x
        self.node=[]


createE()
modules = modus()
fileName = input("Enter your file name please: ")
lines = readFile(fileName)
string = joinLines(lines)
code = sep(string)
code = sepModules(code)
print(code)
m = lineOne(code[0])
print(modules.modus)
print(m.out)
print(m.inp)
body(code[0], m)
x = m.wires[1]
# wireContent([["mid1","=","a","|","b",";"]], m)
print(m.wires[0])
print(m.wires[1])
print(m.out)
print(m)

