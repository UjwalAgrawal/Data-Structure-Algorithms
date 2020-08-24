def selection_sort(listy):
	for i in range(len(listy)):
		for j in range(i+1, len(listy)):
			if(listy[j]<listy[i]):
				listy[j],listy[i] = listy[i], listy[j]
	return(listy)

n=int(input("Number of elements: "))
listy = list(map(int,input("Enter the elements: ").split()))
result = selection_sort(listy)
print(*result)