# The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and 
# we need to calculate the span of stocks price for all n days. 
# The span Si of the stocks price on a given day i is defined as the maximum number of consecutive days 
# just before the given day, for which the price of the stock on the given day is less than or equal to its price on the current day.

def stockSpan(arr):
    stack = []
    n  = len(arr)
    res = []
    for i in range(n):
        if(not stack):
            res.append(-1)
        elif(stack[-1][1] > arr[i]):
            res.append(stack[-1][0])
        else:
            while(stack and stack[-1][1]<= arr[i]):
                stack.pop()
            if(not stack):
                res.append(-1)
            else:
                res.append(stack[-1][0])
        stack.append((i, arr[i]))
    return [(i - res[i]) for i in range(n)]


arr = [100, 80, 60, 70, 60, 75, 85]
print(stockSpan(arr))