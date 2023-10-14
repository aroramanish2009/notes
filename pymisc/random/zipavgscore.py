'''
Input:
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

Output:
90.0 
91.0 
82.0 
90.0 
85.5
'''

def findavgscore(tup):
    return (sum(tup) / len(tup))

def main():
    NX = input()
    stud = NX.split(" ")[0]
    subj = NX.split(" ")[1]
    studscorelist = []
    for i in range(int(subj)):
        strscorelist = input().split(" ")
        scorelist = [float(i) for i in strscorelist]
        studscorelist.append(scorelist)
    for item in zip(*studscorelist):
        print (findavgscore(item))

if __name__ == "__main__":
    main()
