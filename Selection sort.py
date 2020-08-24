def selection_sort(listy):
	for i in range(len(listy)):
		for j in range(i+1, len(listy)):
			if(listy[j]<listy[i]):
				listy[j],listy[i] = listy[i], listy[j]
	return(listy)

list1 = [input() for i in range(int(input("Enter no of elements: ")))]
print(*selection_sort(list1))