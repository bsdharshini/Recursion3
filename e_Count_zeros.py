count =0
def count_zeros(n):
    global count
    if n == 0:
        return 0
    if n%10 == 0:
        count+=1
    count_zeros(n//10)
    return count
n = int(input("Enter the number: "))
if n==0:
    print(1)
else:
    print(count_zeros(n))