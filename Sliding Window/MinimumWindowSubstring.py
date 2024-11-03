from collections import Counter


def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""
    countT = Counter(t)
    window = Counter()
    have = 0
    need = len(countT)
    mini, miniLen = [-1, -1], float("inf")
    l = 0
    for r in range(len(s)):
        ch = s[r]
        window[ch] += 1

        if ch in countT and window[ch] == countT[ch]:
            have += 1

        while have == need:
            if r - l + 1 < miniLen:
                mini = [l, r]
                miniLen = r - l + 1

            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    return s[mini[0]: mini[1] + 1] if mini != [-1, -1] else ""


s = "ADOBECODEBANC"
t = "ABC"
res = minWindow(s, t)
print(f"The minimum window substring is '{res}'")
