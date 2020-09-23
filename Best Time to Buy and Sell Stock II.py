def maxProfit(prices):
    profit = 0
    mini = 0
    maxi =0
    f=0
    stack = [prices[0]]
    for i in range(1,len(prices)):
        if(f==0):
            if(stack[-1]>prices[i]):
                stack.append(prices[i])
            else:
                mini = stack[-1]
                stack.append(prices[i])
                f=1
        else:
            if(stack[-1]>prices[i]):
                profit+= stack[-1] - mini
                stack.append(prices[i])
                f=0
            else:
                stack.append(prices[i])
    if(f==1):
        profit+= stack[-1] - mini
    return(profit)

if __name__ == "__main__":
    prices = list(map(int, input().split()))
    print(maxProfit(prices))