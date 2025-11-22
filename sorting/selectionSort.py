# selection sort 

def selectionSort(arr):
    n=len(arr)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]


if __name__=="__main__":
    arr=[7,4,5,8,1,3,9,0]
    selectionSort(arr)
    for i in arr:
        print(i,end="<->")
