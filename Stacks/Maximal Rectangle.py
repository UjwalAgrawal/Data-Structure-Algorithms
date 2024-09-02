from typing import List
def maxArea(arr: List[int], n:int) -> int:
    stack = []
    left = []
    right = []
    # Next left smaller
    for i in range(n):
        if not stack:
            left.append(-1)
        elif(stack[-1][1] < arr[i]):
            left.append(stack[-1][0])
        else:
            while(stack and stack[-1][1] >= arr[i]):
                stack.pop()
            if not stack:
                left.append(-1)
            else:
                left.append(stack[-1][0])
        stack.append((i, arr[i]))
    stack.clear()

    # Next right smaller
    for i in range(n-1, -1, -1):
        if not stack:
            right.append(n)
        elif(stack[-1][1] < arr[i]):
            right.append(stack[-1][0])
        else:
            while(stack and stack[-1][1] >= arr[i]):
                stack.pop()
            if not stack:
                right.append(n)
            else:
                right.append(stack[-1][0])
        stack.append((i, arr[i]))
    right.reverse()
    return max([(right[i] - left[i] -1) * arr[i] for i in range(n)])


def maxRectangle(matrix: List[List[int]]) -> int:
    n = len(matrix[0])
    h = [0] * n
    maxi = 0
    for row in matrix:
        for i in range(n):
            if(row[i] == '1'):
                h[i] += 1
            else:
                h[i] = 0
        maxi = max(maxi, maxArea(h, n))
    return maxi


matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
print(f"Maximum rectangle area of 1's of the binary matrix is: {maxRectangle(matrix)}")
