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
    def __init__(self, name, key):
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
