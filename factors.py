# find factors of given number
import math

n=24
def factors(n):
    res=[]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            # print(i,end=" ")
            res.append(i)
        if n//i!=i:
            # print(n//i,end=" ")
            res.append(n//i)
    res.sort()
    return res


print(factors(n))