def merge_sort(num_list):
    low=0
    high=len(num_list)-1
    if low==high:
        return num_list
    else:
        left_list=num_list[:(len(num_list)//2)]
        right_list=num_list[(len(num_list)//2):]
        list1=merge_sort(left_list)
        list2=merge_sort(right_list)
        sorted_list=merge(list1, list2)
        return sorted_list

def merge(left_list,right_list):
    i=j=0
    sorted_list=[]
    while(i<len(left_list) and j<len(right_list)):
        if left_list[i]<=right_list[j]:
            sorted_list.append(left_list[i])
            i+=1
        else:
            sorted_list.append(right_list[j])
            j+=1
    
    if i<len(left_list):
        sorted_list.extend(left_list[i::])
    if j<len(right_list):
        sorted_list.extend(right_list[j::])
    return sorted_list

n=int(input("Number of elements: "))
listy = list(map(int,input("Enter the elements: ").split()))
result = merge_sort(listy)
print(*result)