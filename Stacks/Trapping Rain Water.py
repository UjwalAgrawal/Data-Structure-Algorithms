def trap(arr):
    new = arr.copy()
    left = []
    right = []
    n = len(arr)
    arr.insert(0, 0)
    arr.append(0)
    maxi = 0

    for i in range(1, n+1):
        maxi = max(maxi, arr[i-1])
        left.append(maxi)

    maxi = 0

    for i in range(n, 0, -1):
        maxi = max(maxi, arr[i+1])
        right.append(maxi)
    right.reverse()

    total = 0
    for i in range(n):
        mini = min(left[i], right[i])
        if (mini > new[i]):
            total += mini - new[i]
    return total


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f"Maximum water trapped is: {trap(height)}")
