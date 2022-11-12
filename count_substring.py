def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if string[i] == sub_string[0]:
            is_equal = True
            for x in range(0, len(sub_string)):
                if string[i + x] != sub_string[x]:
                    is_equal = False
            if is_equal:
                count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    