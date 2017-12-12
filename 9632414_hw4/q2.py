red=open("rpic.txt","r")
blue=open("bpic.txt","r")
green=open("gpic.txt","r")
rgb=open("RGBpic.txt","w")
def ltol(string):
    string= string[:-1]
    def f(string):
        if len(string)==2:
            return [int(string)/100]
        return [int(string[:2])/100]+f(string[3:])
    return f(string)
def q():
    redd=ltol(red.readline())
    bluee=ltol(blue.readline())
    greenn=ltol(green.readline())
    line=[(redd[k],bluee[k],greenn[k]) for k in range(0,len(redd))]
    line2=[str(k)+" " for k in line]
    def f(x):
        if len(x)==1:
            return x[0]
        return x[0]+f(x[1:])
    string=f(line2)
    rgb.write(string)
    rgb.write("\n")
    return
#q()
#rgb.close()
def linecounter():
    x=0
    while red.readline()!="":
        x=x+1
    red.seek(0)
    return x

def q2(): 
    for line in range(0,linecounter()-1):
        q()
    return
q2()
rgb.close()
    
