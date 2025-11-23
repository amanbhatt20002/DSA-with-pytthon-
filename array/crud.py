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

# Create an array manually
arr = [None] * 10    # capacity
size = 4

arr[0], arr[1], arr[2], arr[3] = 10, 20, 30, 40

# insert at the end
def insert_end(arr,size,value):
    arr[size]=value
    return size+1

    
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



# 2️⃣ READ Operation (Index Based)

def read(arr, index):
    return arr[index]


# 3️⃣ UPDATE Operation

def update(arr, index, value):
    arr[index] = value

# 4️⃣ DELETE Operation — NO BUILT-INS
def delete_end(arr,size):
    arr[size-1]=None
    return size-1

def delete_beg(arr,size):
    for i in range(size-1):
        arr[i]=arr[i+1]
    arr[size-1]=None
    return size-1


# delete at any index

def delete_index(arr,index,size):

    for i in range(index,size):
        arr[i]=arr[i+1]
    arr[size-1]=None
    return size-1




# ----------- TEST -------------

size = insert_end(arr, size, 50)
size = insert_beg(arr, size, 5)
size = insert_index(arr, size, 2, 25)
update(arr, 3, 200)
size = delete_end(arr, size)
size = delete_beg(arr, size)
size = delete_index(arr, size, 2)

print(arr[:size])
