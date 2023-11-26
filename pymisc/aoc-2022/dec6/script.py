import sys
datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")

def data_print(datalist):
    print (datalist)
    return
        
def main():
    data_print(Lines)

if __name__ == "__main__":
    main()
