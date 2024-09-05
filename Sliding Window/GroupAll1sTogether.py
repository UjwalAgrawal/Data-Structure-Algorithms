# Minimum Swaps required to group all 1s together
# Given an array of 0s and 1s, we need to write a program to find the minimum number of swaps 
# required to group all 1s present in the array, if no 1s are present print -1.

def minSwaps(arr):
    #Complete the function
    c = sum(arr)
    n = len(arr)
    if c==n:
        return 0
    if c==0:
        return -1
    s = sum(arr[:c])
    start = 0
    maxi = s
    for i in range(c,n):
        s = s - arr[start] + arr[i]
        start+=1
        maxi = max(maxi, s)
    return c - maxi
        

# arr = [1, 0, 1, 0, 1]
arr = [1, 0, 1, 0, 1, 1] 
print(f"Minimum number of swaps required is: {minSwaps(arr)}")

