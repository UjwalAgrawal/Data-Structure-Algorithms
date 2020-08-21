for _ in range(int(input())):
    n = int(input())
    a = sorted(input().split())
    b = input().split()
    c = []
    for i in a:
        if i in b:
            c.append(i)
            b.remove(i)
    print(*c)
    print(*c)