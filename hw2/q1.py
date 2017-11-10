def q1 (x,p,f):
    if p==0:
        return 1
    if p==1:
        return x
    return f(x,q1(x,p-1,f))

