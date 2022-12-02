from collections import namedtuple
N = int(input())
mark_list = []
Student = namedtuple('Student', input())

for i in range(N):
    mark = int(Student(*input().split()).MARKS)
    mark_list.append(mark)
    
print(sum(mark_list)/N)    