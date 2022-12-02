from collections import defaultdict
n,m = map(int,input().split(" "))
D = defaultdict(list)

for i in range(n):
    S = input()
    D[S].append(i+1)
    
for i in range(m):
    S = input()  
    
    if S in D:
        print(' '.join(map(str,D[S])))
    else:
        print('-1')
        