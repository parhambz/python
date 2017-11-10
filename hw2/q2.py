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

