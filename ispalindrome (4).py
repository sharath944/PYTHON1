def ispalindrome(s):
    rev=join(reversed(s))
    if(s==rev):
        return true
    return false
s=input("enter the word")
ans=ispalindrome(s)
if(ans):
    print("yes")
else:
        prient("no")
