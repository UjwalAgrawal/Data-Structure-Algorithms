#Print the maximum sum of the contiguous sub-array
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    maxi = -1
    s = 0
    #check if all the numbers are negative
    ll = list(filter(lambda q:q>=0, l))
    if(ll): #we can have minimum one number which will have value more than -1
        for x in l:
            s = max(0, s + x)
            maxi = max(maxi, s)
        print(maxi)
    else:   #since all negative take the maximum number
        print(max(l))