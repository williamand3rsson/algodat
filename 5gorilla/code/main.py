import sys
from dp import Dp

counter = 0
letters = []
matrix = []
dic = {}
for line in sys.stdin:
    lines = line.split()
    if counter == 0:
        for linan in lines:
            letters.append(linan)
        counter += 1
    elif counter <= len(letters):
        matrix.append(lines)
        counter += 1
    elif counter == len(letters):
        for i in range(len(letters)):
            for j in range(len(letters)):
                dic[(letters[i], letters[j])] = matrix[i][j]
        counter += 1
    elif counter == len(letters) + 1:
        counter += 1
    else:
        print(Dp.dprec(line[0], line[1], letters, matrix))
       
        


        

        

