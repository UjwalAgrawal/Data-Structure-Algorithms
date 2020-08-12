# This is just an example of how two pointer method works
summ = 70
a = list(range(30))
b = list(range(50))
print(a)
print(b)
i = 0
j = len(b)-1
while(i<len(a) and j>=0):
    if(a[i]+ b[j]< summ):
        i+=1
    elif(a[i]+ b[j] > summ):
        j-=1
    else:
        print(a[i], b[j])
        break

