def build(ind: int, low: int, high: int) -> None:
    if low == high:
        seg[ind] = arr[low]
        return

    mid = (low + high) // 2
    build(2*ind + 1, low, mid)
    build(2*ind + 2, mid + 1, high)
    seg[ind] = max(seg[2*ind + 1], seg[2*ind + 2])


def query(ind: int, low: int, high: int, l: int, r: int) -> int:
    if low >= l and high <= r:
        return seg[ind]
    if high < l or low > r:
        return float('-inf')
    mid = (low + high)//2
    left = query(2 * ind + 1, low, mid, l, r)
    right = query(2 * ind + 2, mid+1, high, l, r)
    return max(left, right)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(arr)
seg = [0] * (3 * n)
build(0, 0, n-1)
print(seg)
queries = [[0, 3], [4, 10]]
res = []
for q in queries:
    res.append(query(0, 0, n-1, q[0], q[1]))
print(res)
