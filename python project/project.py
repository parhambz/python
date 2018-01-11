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
def removeC(string):
    while True:
        k=0
        z=-2
        for x in string:
            if x=="/" and string[k+1]=="/":
                a=k
                z=2
                break
            k=k+1
            
        m=0
        for x in string[a+1:]:
            if x=="\n":
                b=m
                break
            m=m+1
        if z==-2:
            break
        return string[:a]+string[a+b+1:]
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
def createE():
    global errorFile
    error = errorFile
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
def graphMaker(mobject):#give an object and return graph for it
    g=graph(mobject.name)
    op=["&","|"]
    k=0
    for x in mobject.body:
        m=0
        for y in x :
            if y =="=":
                if len(x)==5 or len(x)==6:
                    n=g.addNode(x[m+2])
                    g.addVector(x[m-1],n)
                    g.addVector(x[m +3],n)
                    g.addVector(x[m +1],n)
                if len(x)==3 or len(x)==4:
                    n = g.addNode(x[m])
                    g.addVector(x[m - 1],n)
                    g.addVector(x[m + 1],n)

            m=m+1
        k=k+1
    k=0
    for x in g.vectors:
        if x.name[0]=="*":
            temp=x.node[0]
            no=g.addNode("~")
            x.node=x.node[1:]+[no]
            no.vector=no.vector+[x]
            v=g.addVector(x.name[1:],temp)
            v.node=v.node+[no]
            no.vector=no.vector+[v]
        k=k+1
    return g
'''def lineNumber(string):
    for x in string:
        if x=="\n":
            string=string[]+";+"+str(m)+";"+string[]'''
def setE(msg,line):
    global errorFile
    errorFile.write("Error : "+msg+" line :"+line+"\n")
def setW(msg):
    global errorFile
    errorFile.write("Warning : "+msg+"\n")
def findLine(xs,andis):
    for x in xs[andis:]:
        '''if x[0]=="+" :
            return x[1:]'''
        return "0"
def moduleCheckEW1(xs):
    sep=[" ", "(", ")", ":", ";", "=", ",", "&", "|", "~", "\n","input","output","wire","module","endmodule"]
    o=0
    global m
    if xs[0]!="module":
        setE("should start with 'module'",findLine(xs,0))
        return False
    if xs[-1]!="endmodule":
        setE("module should end with 'endmodule'",findLine(xs,-1))
    name=xs[1]
    if ord(name[0]) not in [x for x in range(97,123)]:
        setE("module should start with a-z only",findLine(xs,1))
        return False
    def nameChek(xs,name,andis):
        global errorFile
        if ord(name[0]) not in range(97,123):
            setE("invalid wire name: " + name, findLine(xs, andis))
            return False
        for x in name:
            if ord(x)>122 or ord(x)<65:
                if x=="_":
                    pass
                else:
                    if x in [str(y) for y in range(10)]:
                        pass
                    else:
                        setE("invalid wire name: "+name,findLine(xs,andis))
                        return False

    if xs[2]!="(":
        setE("unexpected-> '"+xs[2]+"'/ expect-> '('",findLine(xs,2))
        return False
    k=0
    '''for x in xs :
        if x==";":
            if xs[k-1]!=")":
                setE("unexpected :"+xs[k-1],findLine(xs,k))
                return False
        k=k+1'''
    k=0
    for x in xs:
        if x=="wire":
            nameChek(xs,xs[k+1],k+1)
        k=k+1
    k = 0
    for x in xs[2:]:
        if x == ":":
            a = k
        k = k + 1
    wirelist = []
    for x in xs[a + 1:]:
        if x not in sep:
            wirelist = wirelist + [x]
    for x in wirelist:
        if x not in [y.name for y in m.wires]:
            setE("wire " + x + " not defined", findLine(xs,0))
            return False
    for x in m.wires:
        if x.name not in wirelist:
            setW("wire " + x + " not used")
            o=2


    if o==0:
        errorFile.write("OK")
def writeGraph(g):
    global errorFile
    res="\n Vectors : \n"
    for x in g.vectors:
        res =res+x.name+" nodes : "
        for y in x.node:
            res=res+str(y.key)+"("+y.type+")"+","
        res=res[0:-1]+"\n"
    res=res+" Nodes : \n"
    for x in g.nodes:
        res=res+str(x.key)+"("+x.type+")"+ " Vectors : "
        for y in x.vector:
            res=res+y.name+","
        res=res[0:-1]+"\n"
    errorFile.write(res)
def createR():
    global errorFile
    error=errorFile
    l=["=" for x in range(125)]+["\n"]
    line=""
    for x in l:
        line=line+x
    error.write("\n")
    error.write(line)
    l=["*"]+[" " for x in range(55)]+["Circuit Graph"]+[" " for x in range(55)]+["*"]+["\n"]
    title=""
    for x in l:
        title=title+x
    error.write(title)
    error.write(line)
    return error


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
        return temp
    def addVector(self,name,n):
        if name not in [x.name for x in self.vectors]:
            v = vector(name,n,len(self.vectors))
            n.vector=n.vector+[v]
            self.vectors = self.vectors + [v]
            return v
        k = 0
        for x in self.vectors:
            if x.name == name:
                break
            k = k + 1
        v = self.vectors[k]
        n.vector = n.vector + [v]
        v.node=v.node+[n]
        return v
class node:
    def __init__(self,id,type):
        self.type=type[0]
        x=0
        x=x+id
        self.key=x
        self.vector=[]
class vector:
    def __init__(self,name,n,key):
        x=""
        x=x+name
        self.name=x
        x = 0
        x = x + key
        self.key = x
        self.node=[]
        self.node=self.node+[n]


fileName = input("Enter your file name please: ")
modules = modus()
errorFile=open("result.data","w")
createE()
lines = readFile(fileName)
string = joinLines(lines)
string=removeC(string)
code = sep(string)
code = sepModules(code)
m = lineOne(code[0])
if moduleCheckEW1(code[0])!=False:
    body(code[0], m)
    g=graphMaker(m)
    createR()
    writeGraph(g)
errorFile.close()


'''print(g.nodes)
#string=lineNumber(string)
print(code)
print(modules.modus)
print(m.out)
print(m.inp)
x = m.wires[1]
# wireContent([["mid1","=","a","|","b",";"]], m)
print(m.wires[0])
print(m.wires[1])
print(m.out)
print(m)'''


