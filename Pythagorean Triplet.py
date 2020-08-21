for _ in range(int(input())):
    n = input()
    l = list(set(map(int, input().split())))
    n=len(l)
    lsquare = [i**2 for i in l]
    f=1
    for i in range(n-1):
        for j in range(i+1,n):
            if(l[i]**2 + l[j]**2 in lsquare):
                print("Yes")
                f=0
                break
        
    if(f):
        print("No")