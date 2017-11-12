#tarif matris injoorie ke ye list az satr haye matris darim yani har ozv az list ye satr az matrise

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

print(q3([[1,2,5],[3,4,5],[1,2,3]],[[3,2,5,6],[4,5,7,8],[1,2,6,4]]))
print(q3([[1,2],[3,4]],[[1,2],[3,4]]))