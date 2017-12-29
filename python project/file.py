def read(name):
    try:
        file=open(name,"r")
        lines=file.readlines()
        return lines
    except FileNotFoundError :
        print("file not found")

def joinLines(xs):
    res=""
    for x in xs :
        res=res+x
    return res

def sep(string):
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
