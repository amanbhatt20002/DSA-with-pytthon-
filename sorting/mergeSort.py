count=0
call=0
def mergeSort(arr):
    global call
    call+=1
    
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergeSort(arr[:mid])
    right=mergeSort(arr[mid:])

    return merge(left,right)

def merge(left,right):
    i=j=0
    result=[]
    global count
    

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            count+=1
            print(f'merge step {count} :{result}')
            i+=1
        else:
            result.append(right[j])
            count+=1
            print(f'merge step {count} :{result}')
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [8, 3, 4, 9, 1]
mergeSort(arr)
print(f'call :{call} times')