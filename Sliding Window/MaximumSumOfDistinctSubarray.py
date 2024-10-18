# Leetcode 2461. Maximum sum of distinct subarrays of size k
from typing import List

def maximumSubarraySum(nums: List[int], k: int) -> int:
    maxi = 0
    summ = 0
    d = {}
    for i in range(len(nums)):
        summ += nums[i]
        d[nums[i]] = 1 + d.get(nums[i], 0)
        if i >= k:
            summ -= nums[i - k]
            d[nums[i - k]] -= 1
            if d[nums[i - k]] == 0:
                del d[nums[i - k]]
        if len(d) == k:
            maxi = max(maxi, summ)
    return maxi

nums = [1,5,4,2,9,9,9]
k = 3
print("Maximum sum of distinct subarrays of size k is: ", maximumSubarraySum(nums, 3))
