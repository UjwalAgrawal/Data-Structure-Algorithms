def partition(arr,low,high):
	i=low-1
	pivot=arr[high]
	for j in range(low,high):
		if(arr[j]<=pivot):
			i+=1
			arr[i],arr[j]=arr[j],arr[i]
	arr[i+1],arr[high]=arr[high],arr[i+1]
	return(i+1)


def quicksort(arr,low,high):
	if(low<high):
		pi=partition(arr,low,high) #final position of pivoted element
		quicksort(arr,low,pi-1) #elements before pivot
		quicksort(arr,pi+1,high) #elements after pivot
	return(arr)

n=int(input())
listy=list(map(int,input().split()))
result=quicksort(listy,0,n-1)
print(*result)