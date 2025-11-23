# CREATE (Insert)

arr=[1,2,3,4,5]


# 👉 A. Insert at END → append()
# time complexity O(1)
arr.append(2)
print(arr)

# ✔ B. Insert at BEGINNING → insert(0, value)
# 👉 Internally, Python shifts all elements right → O(n)
arr.insert(0,12)
print(arr)

# ✔ C. Insert at ANY INDEX → insert(index, value)
# 👉 Internally, Python shifts all elements right → O(n)

arr.insert(2,4)
print(arr)


#  insert  Operation witout built in methods

arr1=[None]*10
arr1[0]=1
arr1[1]=3
arr1[2]=4
size=3

# insert at the end
def insert_end(arr,size,value):
    
    arr[size]=value
    return size+1

size=insert_end(arr1,size,50)
size=insert_end(arr1,size,51)
size=insert_end(arr1,size,52)
size=insert_end(arr1,size,53)
print(arr1)
    
# ✔ B. Insert at BEGINNING
def insert_beg(arr,value,size):
    for i in range(size,0,-1):
        arr[i]=arr[i-1]
    arr[0]=value
    return size+1

# ✔ C. Insert at ANY INDEX
def insert_index(arr,index,size,value):
    for i in range(size,index,-1):
        arr[i]=arr[i-1]
    arr[index]=value
    return size+1




