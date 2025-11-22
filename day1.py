# find min | max element in the array
# my approach
def min_element(arr):
    minE=arr[0]
    for i in range(len(arr)):
        if minE>arr[i]:
            minE=arr[i]
    
    return minE

def max_element(arr):
    maxE=arr[0]
    for i in range(len(arr)):
        if maxE<arr[i]:
            maxE=arr[i]
    
    return maxE

# arr=[1]
# print(min_element(arr))
# print(max_element(arr))

# 🔹 Things to Practice

# Try with negative numbers.

# Try with all equal numbers.

# Try with a single element array.

# Try with empty array (edge case).


# optimise solution

def min_max(arr):
    if not arr:
        return None,None
    
    minEL=maxEL=arr[0]
    for num in range(len(arr)):
        if arr[num]<minEL:
            minEL=arr[num]
        elif arr[num]>maxEL:
            maxEL=arr[num]
    return maxEL,minEL

arr=[]
print(min_max(arr))
