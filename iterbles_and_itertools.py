from itertools import combinations
N = input()
S = list(input().split())
K = int(input())
count = 0

for i in combinations(S,K):
    if 'a' in i:
        count += 1
        
print(count/len(list(combinations(S,K))))        