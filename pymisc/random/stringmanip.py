def merge_the_tools(string, k):
    end = k
    for i in range(0,len(string),k):
        substr = string[i:end]
        newsubstr = ""
        index = 1
        for char in substr:
            if char not in newsubstr:
                newsubstr = newsubstr + char
            index += 1
        #print ("".join(set(substr)))
        print (newsubstr)
        end = end + k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
