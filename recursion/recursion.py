# today i learn two type of recursion  ** head recursion and *** tail recursion **
# this  head recursion 
count=0
def headRecursion():
    global count
    if count==4:
        return
    print(f'hi aman {count}')
    count+=1
    headRecursion()




# this is tail recursion
def tailRecursion():
    global count
    if count==8:
        return
   
    count+=1
    tailRecursion()
    print(f'hi aman {count}')




headRecursion()
tailRecursion()
print(count)
# print 1 to n using tail (backtracking)
def recurr(n):
    if n==0:
        return
    print(n)
    recurr(n-1)
   

recurr(5)
