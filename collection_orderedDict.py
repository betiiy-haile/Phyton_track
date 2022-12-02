from collections import OrderedDict
items = OrderedDict()
N = int(input())

for i in range(N):
    item,blank,price = input().rpartition(' ')
    if item not in items:
        items[item] = int(price)
    else:
        items[item] += int(price)   
    
        
for i in items.items():
    print(*i) 