def count_substring(string, sub_string):
    count = 0 
    start_subst = string.find(sub_string)
    while start_subst >= 0:
        count += 1
        string = string[start_subst + 1:]
        print (string)
        start_subst = string.find(sub_string)
    return (count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
