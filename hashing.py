#  hashing first store  then  ittrate

arr=[1,1,2,0,3,4,5,6,8,8,7,6,5,5,3,3,3,3,4,5,6,6,6,9,10]

def frequency(arr):
    hash_list=[0]*11
    for num in arr:
        hash_list[num]+=1
    for i in  range(len(hash_list)):
        print(f'{i} is {hash_list[i]} times ')




# hashing through  dict

def Frequency(arr):
    hash_dict={}
    for num in arr:
        if num in hash_dict:
            hash_dict[num]+=1
        else:
            hash_dict[num]=1

    for key,value in hash_dict.items():
        print(f'{key}is {value} times') 




print('with hashing')
frequency(arr)
print('with dictionary')
Frequency(arr)