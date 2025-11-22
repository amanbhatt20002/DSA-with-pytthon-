# quick sort
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in correct position
    return i + 1

def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr, low, high)  # Partitioning index
        quicksort(arr, low, pi - 1)   # Sort left subarray
        quicksort(arr, pi + 1, high)

# Example usage
arr = [3,1,2]
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)