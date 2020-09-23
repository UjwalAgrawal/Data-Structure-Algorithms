# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/

def maxProfit(prices):
    profit = 0
    mini = 0
    maxi =0
    f=0  #flag 0:buy 1:sell
    stack = [prices[0]]
    for i in range(1,len(prices)):
        if(f==0):
            if(stack[-1]>prices[i]):
                stack.append(prices[i])
            else:
                mini = stack[-1]
                stack.append(prices[i])
                f=1 #change it to selling now
        else:
            if(stack[-1]>prices[i]):
                profit+= stack[-1] - mini
                stack.append(prices[i])
                f=0 #sold the stock. ready to buy again
            else:
                stack.append(prices[i])
    if(f==1):       #if bought but did not sell then sell the last stock bought
        profit+= stack[-1] - mini
    return(profit)

if __name__ == "__main__":
    prices = list(map(int, input().split()))
    print(maxProfit(prices))