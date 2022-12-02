from collections import Counter

X = input()
shoes = list(map(int,input().split(" ")))
myList = Counter(shoes)
money = 0
N = int(input())
for i in range(N):
    size,price = map(int,input().split(" "))
    if myList[size]:
        myList[size] -= 1
        money += price
            
        
print(money)