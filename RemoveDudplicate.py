# RemoveDudplicate.py
def removeD(arr):
    dict={}
    for i in arr:
        if i in dict:
            pass
        else:
            dict[i]=True

    keys=list(dict.keys())
    n=len(keys)
    for i in range(n):
        arr[i]=keys[i]
    
    return arr[:n]



# two pointer approach
def RDubplicate(arr):
    arr.sort()
    if len(arr)==1:
        return 1
    i=0
   

    for j in range(i+1,len(arr)):
       if arr[j]!=arr[i]:
          i+=1
          arr[i]=arr[j]
    return i+1

print(removeD([1,2,2,3,4,5,5,6,7,3,9,8,9]))
print(RDubplicate([1,2,2,3,4,5,5,6,7,3,9,8,9]))


