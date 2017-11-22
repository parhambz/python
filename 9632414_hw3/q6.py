def q6(a):
    def h(x):
        if x%2==0:
            return x//2
        return (x//2)+1
        #saghf gire x dar taghsim be 2
    
    def f(x):
        if x==2:
            return 1.5
        if x==1:
            return 1
        return 3*f(h(x))-2*(g(x-1))
        #tarif tabe f
    
    def g(x):
        if x==1 or x==2:
            return 0
        return x*(f(x-2))+a*(g(x-1))
        #tarif tabe g
    return f