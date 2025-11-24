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


# optimise solution 
def reverse(arr,left,right):
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1

arr=[1,2,3,4,5]
n=len(arr)
k = 1
k = k % n 
print(arr)
reverse(arr,n-k,n-1)
reverse(arr,0,n-k-1)
reverse(arr,0,n-1)
print(arr)