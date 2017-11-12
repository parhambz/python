def q2 (x,p,f):
    def q1 (x,p,f):
        if p==0:
            return 1
        if p==1:
            return x
        return f(x,q1(x,p-1,f))    
    if p%2==0:
        return f(q1(x,p/2,f),x)
    return f(q1(x,p//2,f),x)

def q3(xs,ys):
    def setoon(xs,b):
        return [xs[n][b] for n in range (0,len(xs))]
    def satr(xs,a):
        return xs[a]    
    def deraye(xs,ys,m,n):
        return sum([satr(xs,m)[q]*setoon(ys,n)[q] for q in range(0,len(xs[0]))])
    def zarb(xs,ys):
        return[deraye (xs,ys,m,n) for m in range (0,len(ys)) for n in range (0,len(ys[0]))]
    e=zarb(xs,ys)
    def moratab(e,g):
        if (len(e)==g):
            return [e]
        return [e[0:g]]+moratab(e[g:],g)
    return moratab(e,len(ys[0]))

def q4(xs,p):
    return q2(xs,p,q3)

#print(q4([[1,2],[4,5]],5))
    