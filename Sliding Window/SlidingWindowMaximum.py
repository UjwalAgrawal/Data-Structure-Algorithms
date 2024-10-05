# Leetcode 239. Sliding Window Maximum
# You are given an array of integers 'nums', there is a sliding window of size 'k'
# which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.

# Return the max sliding window.

from typing import List
from collections import deque


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []
    q = deque()
    for idx, num in enumerate(nums):
        while q and q[-1] < num:
            q.pop()
        q.append(num)
        if idx >= k and nums[idx - k] == q[0]:
            q.popleft()

        if idx >= k - 1:
            res.append(q[0])
    return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print("The output array is: ", maxSlidingWindow(nums, k))
