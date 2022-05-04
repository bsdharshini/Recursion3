#multiplication using addition 

# 5 * 4 -> 5+5+5+5

def mul(n,x):
    if x == 0:
        return 0

    return n+mul(n,x-1)
print(mul(5,4))