def knapsack(weights, values, maxWeight, n):
    if(n==0 or maxWeight==0):
        return(0)
    if(weights[n-1]<=maxWeight):
        return max(values[n-1] + knapsack(weights, values, maxWeight-weights[n-1], n-1), knapsack(weights, values, maxWeight, n-1))
    else:
        return(knapsack(weights, values, maxWeight, n-1))


if __name__ == "__main__":
    weights = list(map(int, input("Enter weights: ").split()))
    values = list(map(int, input("Enter values: ").split()))
    maxWeight = int(input("Enter maximum weight/capacity: "))
    maxValue = knapsack(weights, values, maxWeight, len(weights))
    print(maxValue)