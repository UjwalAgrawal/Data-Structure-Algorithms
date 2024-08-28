# Given an integer array arr of integers, the task is to find the maximum absolute difference between 
# the nearest left smaller element and the nearest right smaller element of every element in array arr. 
# If for any component of the arr, the nearest smaller element doesn't exist then consider it as 0.

def findMaxDiff(arr):
    rightSmaller = []
    stack = []
    n = len(arr)
    for i in range(n-1, -1, -1):
        if(not stack):
            rightSmaller.append(0)
        elif(stack[-1] < arr[i]):
            rightSmaller.append(stack[-1])
        else:
            while(stack and stack[-1]>=arr[i]):
                stack.pop()
            if(stack):
                rightSmaller.append(stack[-1])
            else:
                rightSmaller.append(0)
            
        stack.append(arr[i])
    rightSmaller.reverse()
    stack.clear()
    
    leftSmaller = []
    for i in range(n):
        if(not stack):
            leftSmaller.append(0)
        elif(stack[-1] < arr[i]):
            leftSmaller.append(stack[-1])
        else:
            while(stack and stack[-1] >= arr[i]):
                stack.pop()
            if(stack):
                leftSmaller.append(stack[-1])
            else:
                leftSmaller.append(0)
        stack.append(arr[i])
    maxi = -1
    for i in range(n):
        maxi = max(maxi, abs(leftSmaller[i] - rightSmaller[i]))
    return maxi

arr = [2, 4, 8, 7, 7, 9, 3]
print(f"The maximum difference is {findMaxDiff(arr)}")

