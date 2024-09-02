def maxAreaHistogram(arr):
    left = []
    right = []
    stack = []
    n = len(arr)
    for i in range(n):
        if not stack:
            left.append(-1)
        elif(stack[-1][1] < arr[i]):
            left.append(stack[-1][0])
        else:
            while(stack and stack[-1][1] >= arr[i]):
                stack.pop()
            if not stack:
                left.append(-1)
            else:
                left.append(stack[-1][0])
        stack.append((i, arr[i]))

    stack.clear()
    for i in range(n-1,-1,-1):
        if not stack:
            right.append(n)
        elif(stack[-1][1] < arr[i]):
            right.append(stack[-1][0])
        else:
            while(stack and stack[-1][1] >= arr[i]):
                stack.pop()
            if not stack:
                right.append(n)
            else:
                right.append(stack[-1][0])
        stack.append((i, arr[i]))
    right.reverse()
    final = [(right[i] - left[i] - 1) * arr[i] for i in range(n)]
    return max(final)



arr = [6,2,5,4,5,1,6]
print(f"Maximum area is: {maxAreaHistogram(arr)}")