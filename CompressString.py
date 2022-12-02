from itertools import groupby
S = input()
for i,j in groupby(S):
    print(tuple([len(list(j)),int(i)]),end=" ")