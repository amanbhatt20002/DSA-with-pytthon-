def findMean(arr):
    n=len(arr)
    if n==1:
        return float(findMean(arr[n-1]))
    else:
        return (findMean(arr[:n-1])*(n-1)+arr[n-1])/n


if __name__=="__main__":
    arr=[1,2,3,4]
    mean1= findMean(arr)
    print("Mean :",mean1)