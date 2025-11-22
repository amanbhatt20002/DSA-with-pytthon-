# largest el in array
def largestEl(arr):
    l=arr[0]
    for i in arr:
        l=max(l,i)

    return l



arr=[1,2,3,4]
print(largestEl(arr))