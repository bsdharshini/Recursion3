#b_sum_of_digit.py

#eg: 5372 o/p=17
def sum_digit(n):
    if n==0:
        return 0
    return (n%10)+ sum_digit(n//10)
print(sum_digit(int(input())))