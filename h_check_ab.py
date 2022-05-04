# a) the string begis with a
# b) each 'a' should followed by nothing or 'bb'
# c) each 'bb' should be followed by a or nothing

def check(s):
    l =len(s)
    if l == 0:
       return True
    if s[0] == 'a':
        if l>1 and s[1:3]=='bb':
            return check(s[3:])
        else:
            return check(s[1:])
    else:
        return False
print(check(input()))
        
