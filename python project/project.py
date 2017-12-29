def readFile(name):#read file from txt
    try:
        file=open(name,"r")
        lines=file.readlines()
        return lines
    except FileNotFoundError :
        print("file not found")
def joinLines(xs): #join lines and make a string
    res=""
    for x in xs :
        res=res+x
    return res
def sep(string): #seperate with seprators
    string=string+" "
    seps=[" ","(",")",":",";","=",",","&","|","~","\n"]
    res=[]
    temp=""
    for x in string:
        if x in seps:
            if x!=" " and x!="\n":
                res=res+[temp]+[x]
                temp=""
            else:
                res = res  + [temp]
                temp = ""
        else:
            temp=temp+x

    return [x for x in res if x!=""]
def sepModules(xs): #seprate modules from each other
    for x in xs:
        res=[]
        temp=[]
        if x=="module":
            temp=["module"]
        else:
            if x=="endmodule":
                temp=temp+["endmodule"]
                res=res+[temp]
            else:
                temp=temp+[x]
    return res
def lineOne(xs): #code ye module ro migire objectesho misaze input output ro ham ezafe mikone tahesh objectesho mide
    modules.addModu(xs[1])
    temp=modules.modus[-1]
    k=0
    for x in xs:
        if x==":":
            break
        k=k+1
    inout=xs[2:k]
    k=0
    for x in inout:
        if x=="input":
            temp.input(inout[k+1])
        if x=="output":
            temp.output(inout[k+1])
        k=k+1
    return temp



class modu:
    def __init__(self,name,key):
        x=""
        x=x+name
        self.name=x
        x = 0
        x = x + key
        self.key = x
        self.inp=[]
        self.out=[]
    def input(self,name):
        x = ""
        x = x + name
        self.inp += [x]
    def output(self,name):
        x = ""
        x = x + name
        self.out = x
class modus:
    def __init__(self):
        self.modus=[]
    def addModu(self,name):
        key=len(self.modus())
        a=modu(name,key)
        self.modus=self.modus+[a]
        return key



fileName=input("Enter your file name please: ")
lines=readFile(fileName)
string=joinLines(lines)
code=sep(string)
code=sepModules(code)
modules=modus()
