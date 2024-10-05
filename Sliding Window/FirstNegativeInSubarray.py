# Given an array A[] of size N and a positive integer K,
# find the first negative integer for each and every window(contiguous subarray) of size K.

from collections import deque


def printFirstNegativeInteger(A: list[int], K: int) -> list[int]:
    q = deque()
    res = []
    for idx, num in enumerate(A):
        # store all the negative numbers in the queue
        if num < 0:
            q.append(num)

        # if window is smaller than the given window size
        if idx < K-1:
            continue
        # if there is atleast one number in the queue
        if q:
            # append first number in the queue to the result
            res.append(q[0])
            # if the number going out of the window is the first number in the queue, remove it from the queue
            if q[0] == A[idx-K+1]:
                q.popleft()
        else:
            # when queue is empty, which means all the numbers in the current window is positive. so, append 0 in the result
            res.append(0)

    return res


A = [-8, 2, 3, -6, 10]
K = 2
print("The output array is: ", printFirstNegativeInteger(A, K))
