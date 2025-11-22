# 2786
n=222
def reverseInt(n):
    res=0
    orignal=n
    count=0
    while n>0:
        lastD=n%10
        res=res*10+lastD
        count+=1
        n=n//10
    return res==orignal

print(reverseInt(n))