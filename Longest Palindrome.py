# Leetcode 5: Given a string S, find the longest palindromic substring in S.

def longestPalindrome(s):
    n = len(s)
    res = ""

    def findPalindrome(left, right):
        while left > -1 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1: right]

    for i in range(n):
        odd = findPalindrome(i, i)
        even = findPalindrome(i, i+1)

        t = odd if len(odd) > len(even) else even
        res = t if len(t) > len(res) else res
    
    return res

s = 'amalayalam'
# s = 'cbbd'
print("Longest palindromic substring is:", longestPalindrome(s))
