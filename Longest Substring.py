#This program prints length of the longest substring with unique characters.
def longestSubstring(s):
    maxi = -1
    stack = []
    for i in s:
        if(i not in stack):
            stack.append(i)
        else:
            maxi = max(maxi, len(stack))
            stack.clear()
            stack.append(i)
    return(max(maxi, len(stack)))


yo = input()
print(longestSubstring(yo))
