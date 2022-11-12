if __name__ == '__main__':
    N = int(input())
    numbers = []
    for n in range(N):
        cmd = input().split()
        if cmd[0] == "insert":
            numbers.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "print":
            print(numbers)    
        elif cmd[0] == "remove":
            numbers.remove(int(cmd[1]))
        elif cmd[0] == "append":
            numbers.append(int(cmd[1]))
        elif cmd[0] == "sort":
            numbers.sort()
        elif cmd[0] == "pop":
            numbers.pop()
        elif cmd[0] == "reverse":
            numbers.reverse()
        