def minJumps(arr, n):
    #code here
    if(n==1):
        return 0
    if(arr[0]==0):
        return -1
        
    jumps = [float('inf')] * (n)
    jumps[0] = 0
    for i in range(1,n):
        for j in range(i):
            if(i <= (j + arr[j])):
                jumps[i] = min(jumps[i], jumps[j] + 1)
    return jumps[-1] if jumps[-1] != float('inf') else -1

n = 6
arr = [1, 4, 3, 2, 6, 7]
print(minJumps(arr, n))
