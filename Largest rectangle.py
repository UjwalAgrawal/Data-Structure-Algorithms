def LargestRectangle(arr):
    stack = []
    maxArea = -1
    i, l=0, len(arr)
    while(i<l):
        if(not stack or arr[stack[-1]]<=arr[i]):
            stack.append(i)
            i+=1
        else:
            t = stack.pop()
            if(stack):
                area = arr[t] * (i-stack[-1]-1)
            else:
                area = arr[t]* i
            maxArea = max(area, maxArea)
    while(stack):
        t = stack.pop()
        if(stack):
            area = arr[t] * (i-stack[-1]-1)
        else:
            area = arr[t]* i
        maxArea = max(area, maxArea)
    return(maxArea)


n = int(input("Number of bars: "))
arr = list(map(int, input().split()))
print("Maximum area is",LargestRectangle(arr))