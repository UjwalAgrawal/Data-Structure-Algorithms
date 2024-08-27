def nextGreater(arr, n):
    stack = []
    res = []
    for i in range(n-1, -1, -1):
        if(not stack):
            res.insert(0, -1)
        elif(stack[-1] > arr[i]):
            res.insert(0, stack[-1])
        else:
            while(stack and stack[-1] <= arr[i]):
                stack.pop()
            if(stack):
                res.insert(0, stack[-1])
            else:
                res.insert(0, -1)
        stack.append(arr[i])
    return res


n = 5
arr = [6, 8, 0, 1, 3]
print(nextGreater(arr, n))