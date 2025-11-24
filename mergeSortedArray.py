# merge two sorted array without dubploicate

def merge_unique(arr,arr1):
    n1=len(arr)
    n2=len(arr1)
    i=0
    j=0
    res=[]
    while i<n1 and i<n2:
        if arr[i]<=arr1[j]:
            if len(res)<=0 or res[-1]!=arr[i]:
                res.append(arr[i])
            i+=1
        else:
            if len(res)==0 or res[-1]!=arr1[j]:
                res.append(arr1[j])
            j+=1
    
    for k in range(i,n1):
        if res[-1]!=arr[k]:
            res.append(arr[k])

        
    for k in range(j,n2):
                if res[-1]!=arr1[k]:
                     res.append(arr1[k])
    return res

        
arr = [1, 2, 3, 5]
arr1 = [2, 3, 4, 6]
print(merge_unique(arr, arr1))