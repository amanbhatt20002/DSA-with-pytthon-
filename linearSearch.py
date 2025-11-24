# linearSearch
# we have to return  the index  and  if the target valuse not found return  -1

def returnIndex(arr,value):
    res=-1
    for i in range(len(arr)):
        if arr[i]== value:
            return i
    return res

arr=[1,2,3,4,99,6]
value=99
result=returnIndex(arr,value)+1
if result:
    print(f"target {value} found at position {result}")
else:
    print("not found")


