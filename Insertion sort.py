def insertionSort(arr,n):
    for i in range(1,n):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
    return(arr)


n=int(input())
listy=list(map(int,input().split()))
result=insertionSort(listy,n)
print("Sorted array is:", *result)