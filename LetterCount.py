# count occurences of letter in a word
# e.g. aaabbcccabaa = [['a', 3], ['b', 2], ['c', 3], ['a', 1], ['b', 1], ['a', 2]]

def letterCount(s):
    i = 0
    n=len(s)
    listy = []
    while(i<n):
        c = 0
        curr = i
        while(curr<n-1):
            curr+=1
            if(s[i]==s[curr]):
                c+=1
                continue
            break
        c+=1
        listy.append([s[i],c])
        if(curr!=i):
            i = curr
        else: 
            i+=1
    listy.pop(-1)
    return(listy)


if __name__ == "__main__":
    s = input()
    print(letterCount(s))
