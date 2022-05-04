#Geometric sum using recursion
# 1+ 1/2+ 1/2^2 + 1/2^3+ ..... + 1/2^k

# first split the problem do 1/2^k then add and do recurison for geo(k-1)

def geo(n):
    if n==0:
        return 0
    return 1/2**(n)+ geo(n-1)
n = int(input())
print('%5f' %geo(n))
