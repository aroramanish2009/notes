def swap_case(s):
    mylist = []
    for i in s:
        if i.isupper():
            i = i.lower()
        else:
            i = i.upper()
        mylist.append(i)
    return (''.join(mylist))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
