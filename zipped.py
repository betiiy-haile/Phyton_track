N,X = map(int,input().split(" "))
marks = []
for i in range(X):
    marks.append(list(map(float,input().split(" "))))
    
    
total_mark = zip(*marks)  
for i in total_mark:
    print(sum(i)/X)  