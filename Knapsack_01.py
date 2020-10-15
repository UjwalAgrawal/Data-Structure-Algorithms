dp = {}

def knapsack(weights, values, maxWeight, n):
    if(n==0 or maxWeight==0):
        return(0)
    if((maxWeight, n) in dp):
        # print("found it")
        # It is a hit
        return(dp[(maxWeight, n)])
    if(weights[n-1]<=maxWeight):
        dp[(maxWeight, n)] = max(values[n-1] + knapsack(weights, values, maxWeight-weights[n-1], n-1), knapsack(weights, values, maxWeight, n-1))
        return(dp[(maxWeight, n)])
    else:
        dp[(maxWeight, n)] = knapsack(weights, values, maxWeight, n-1)
        return(dp[(maxWeight, n)])


if __name__ == "__main__":
    weights = list(map(int, input("Enter weights: ").split()))
    values = list(map(int, input("Enter values: ").split()))
    maxWeight = int(input("Enter maximum weight/capacity: "))
    maxValue = knapsack(weights, values, maxWeight, len(weights))
    print(maxValue)