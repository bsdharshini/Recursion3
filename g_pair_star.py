# when we have same character together then add * in between 
# eg: hello -> hel*lo

def star(s):
    l = len(s)
    if l ==0 or l == 1:
        return s
    if s[0]==s[1]:
        return s[0]+'*'+star(s[1:])
    else:
        return s[0]+star(s[1:])

print(star('helllo'))