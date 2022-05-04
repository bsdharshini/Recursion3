# string to integer

# take first string using ASCII convert string to integer

# eg: 2134, take 1 -> ord(2)-48 -> 46 which is number 2 in ASCII

def convert(s):
    l = len(s)
    if l==0:
        return 0
    b = ord(s[0])-48
    return (b*(10**(l-1)))+convert(s[1:l])
print(convert(input()))