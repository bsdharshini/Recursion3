#move to stair n by taking 1/2/3 steps at a time. print all possible ways
#eg:n=4 then possible ways are: 1111, 112, 121, 13, 22,211, 31-> 7
def stair(n):
    if n ==0:
        return 1
    elif n<0:
        return 0
    return stair(n-1)+stair(n-2)+stair(n-3)
print(stair(4))