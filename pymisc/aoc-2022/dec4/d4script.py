import sys
datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
#['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']

def data_print(datalist):
    print (datalist)
    return

def verifyoverlap(Lines):
    count = 0
    for i in Lines:
        obj1 = i.split(",")[0]
        obj2 = i.split(",")[1]
        d1_obj1 = int(obj1.split("-")[0]) #2
        d2_obj1 = int(obj1.split("-")[1]) #4
        d1_obj2 = int(obj2.split("-")[0]) #6
        d2_obj2 = int(obj2.split("-")[1]) #8
        #22 62 -- 22 63
        print (d1_obj1,d2_obj1,"--",d1_obj2,d2_obj2)
        if d1_obj2 >= d1_obj1 and d1_obj2 <= d2_obj1:
            if d2_obj2 <= d2_obj1:
                count = count + 1
                print ("counted")
                continue
        if d1_obj1 >= d1_obj2 and d1_obj1 <= d2_obj2:
            if d2_obj1 <= d2_obj2:
                count = count + 1
                print ("counted")
        #print (obj1,obj2)
    return (count)

def verifyoverlap2(Lines):
    count = 0
    for i in Lines:
        set1 = ()
        set2 = ()
        obj1 = i.split(",")[0]
        obj2 = i.split(",")[1]
        d1_obj1 = int(obj1.split("-")[0]) #2
        d2_obj1 = int(obj1.split("-")[1]) #4
        d1_obj2 = int(obj2.split("-")[0]) #6
        d2_obj2 = int(obj2.split("-")[1]) #8
        set1 = set(range(d1_obj1, d2_obj1 + 1))
        set2 = set(range(d1_obj2, d2_obj2 + 1))
        print(set1,"--",set2)
        if bool(set1 & set2):
           count = count + 1
    return(count)
        
def main():
    #data_print(Lines)
    #print(verifyoverlap(Lines))
    print(verifyoverlap2(Lines))

if __name__ == "__main__":
    main()
