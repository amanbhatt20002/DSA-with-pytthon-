# amstrong no.
# n= 153
# 1**3 +5**3+3**3=153

def isAmstrong(n):
    res=0
    orignal=n
    digit=str(n)
    power=len(digit)
    while orignal>0:
        lastD=orignal%10
        res+=lastD**power
        orignal=orignal//10
    return res==n
print(isAmstrong(153))