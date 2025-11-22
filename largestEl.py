# largest el in array
def largestEl(arr):
    l=arr[0]
    for i in arr:
        l=max(l,i)

    return l







# second Largest el in array
def secondLEl(arr):
    if len(arr) < 2:
        return None  # no second largest
    Sl=l=float('-inf')
    for i in arr:
        if i>l:
            Sl=l
            l=i
        elif i> Sl and i!=l:
            Sl=i
    return Sl

arr = [5, 1, 2, 3]
print(largestEl(arr))
print(secondLEl(arr))
   