# if array is sorted or not

def checkSortedArray(arr):
    asc=True
    des=True

    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            asc=False
        if arr[i]<arr[i+1]:
            des=False
    if asc:
        return True
    elif des:
        return True
    else:
        return False
    
print(checkSortedArray([1, 2, 3, 4]))     # True (ascending)
print(checkSortedArray([5, 4, 2, 1]))     # True (descending)
print(checkSortedArray([1, 3, 2]))   