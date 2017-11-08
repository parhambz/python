def f(xs,b,c):
    a=[xs[n][0:c]+xs[n][c+1:] for n in range(0,len(xs))]
    return a[0:b]+a[b+1:]
def det(xs):
    if (len(xs)==2):
        return xs[0][0]*xs[1][1]-xs[0][1]*xs[1][0]
    return sum([det(f(xs,0,n))*xs[0][n]*(-1)**(n) for n in range(0,len(xs[0]))])


