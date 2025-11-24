# move zeroes to the end
def move(arr):
    r=len(arr)-1
    l=0
    while l<r:
        if arr[l]==0:
            arr[l],arr[r]=arr[r],arr[l]
            r-=1
        else:
            l+=1


arr = [0, 1, 0, 3,0, 12]
move(arr)
print(arr)
