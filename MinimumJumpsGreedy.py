def minimumJumps(arr, n):
    # To check if it is possible to reach at the end
    maxInd = 0
    for i in range(n):
        if(i > maxInd):
            return -1
        else:
            maxInd = max(maxInd, i + arr[i])
    # Now calculate the number of jumps required
    jumps, l, r = 0, 0, 0
    while(r < n-1):
        farthest = 0
        for i in range(l, r+1):
            farthest = max(farthest, i + arr[i])
        l = r+1
        r = farthest
        jumps+=1
    return jumps


n = 6
arr = [1, 4, 3, 2, 6, 7]
print(minimumJumps(arr, n))