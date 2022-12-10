import numpy as np 

def CheckForLess(list, val):
    return(min(list)<val)

with open("8/test.txt") as f:
    total = 0
    trees = np.array([list(map(int, line.strip())) for line in (f.readlines())])  

    for row in trees:
        for index in row:
            # print(row, index)
            if(CheckForLess(row, index)):
                total+=1
    
    print(total)