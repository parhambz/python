def jam(n):
    if n//10==0:
        return n
    return n%10+jam(n//10)

def q6(n):
    return [b for b in range (1,n+1) if b== jam(b)]
print(q6(17))