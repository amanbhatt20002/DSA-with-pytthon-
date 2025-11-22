# bubble sort 
def bubbleSort(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        swapped=False
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break


if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9]
    bubbleSort(arr)
    for i in arr:
        print(i,end="<->")
