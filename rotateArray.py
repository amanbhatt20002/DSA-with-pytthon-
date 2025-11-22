# rotateArray.py
# brute force approach
def rotateBrute(arr):
    pos=2
    n=len(arr)
    temp=arr[n-pos:]
    for i in range(n-1, pos-1, -1):
        arr[i] = arr[i-pos]
    
    for j in range(pos):
        arr[j]=temp[j]
    return arr

print(rotateBrute([1,2,3,4]))