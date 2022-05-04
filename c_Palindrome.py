#c_Palindrome.py

#appa is palindrome, abcba is also palindrome, abcde is not palindrome

# first and last should be same, first+1 and last-1 should be same, and goes on
def helper(t,s,e):
    if s==e:
        return True
    if t[s]!=t[e]:
        return False
    if s<e+1:
        return helper(t,s+1,e-1)
    return True

def palindrome(t):
    l =len(t)
    if l==0 or l==1:
        return True
    return helper(t,0,l-1)

print(palindrome('abccba'))