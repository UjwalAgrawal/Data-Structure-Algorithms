# Print the maximum sum of the contiguous sub-array
# l = [-2,1,-3,4,-1,2,1,-5,4]
l = [5,4,-1,7,8]
maxi = float("-inf")
for _ in range(len(l)):
    summ = 0
    for x in l:
        summ = max(0, summ + x)
        maxi = max(maxi, summ)
print(maxi)
