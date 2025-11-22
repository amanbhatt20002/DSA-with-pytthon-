# 2786
n=222
def isPalindrome(n):
    res=0
    orignal=n

    while n>0:
        lastD=n%10
        res=res*10+lastD
        n=n//10
    return res==orignal

print(isPalindrome(n))