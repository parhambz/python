import time
def bsortf(xs):
    for k in range(1,len(xs)):
        for n in range(0,len(xs)-1):
            if xs[n]>xs[n+1]:
                xs=xs[:n]+[xs[n+1]]+[xs[n]]+xs[n+2:]
    return xs

def bsortr(xs):
    def f(xs):
        if len(xs)==1:
            return xs
        if xs[0]>xs[1]:
            xs[0],xs[1]=xs[1],xs[0]
        return f(xs[1:])
    return f(xs)
def bsortb(xs):
    if len(xs)==1:
        return xs
    x=bsortr(xs)
    return bsortb([k for k in xs if x[0]!=k])+x
    print(time.time())
    #bazgashti-->bsortb()
    #gheyre bazgashti -->bsortf()
    
    #function time() kar nakard ama vase andaze giri zaman ye bar ghabl az seda zadane tabe time ro check mikonim
    #ye bar ham badesh az ham kam mikonim mishe zaman ejra shodane tabe . vase har 2 anjam midim in karo bad
    #zaman ha ro ba ham moghayese mikonim