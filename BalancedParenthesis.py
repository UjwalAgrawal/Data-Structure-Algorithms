#This solution deals with a problem where one has to 
#find balance parenthesis in minimum number of modificatiopns in ascending order.
import queue
def isBalanced(s):
    cnt= 0
    for i in s:
        if(i=='('): cnt+=1
        elif(i==')'): cnt-=1
        if(cnt<0): return(False)
    return(cnt==0)

def solution(s):
    vis = {}
    q = queue.SimpleQueue()
    answers = []
    q.put(s)
    while(not q.empty()):
        f = q.get()
        try:
            if(vis[f]==1):
                continue
        except:
            vis[f]=1
        if(isBalanced(f)):
            answers.append(f)
        else:
            for i in range(len(f)):
                if(f[i]=='(' or f[i]==')'):
                    q.put(f[:i]+f[i+1:])
    return(answers)

yo = input()
print(solution(yo))


