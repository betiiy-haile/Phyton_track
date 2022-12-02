from itertools import permutations
S = list(input().split(" "))
ans = list(permutations(S[0],int(S[1])))
ans.sort()
for i in ans:
    print(''.join(i))