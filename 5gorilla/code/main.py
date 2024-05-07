import sys
from dp import Dp
from dp1 import Dp1

counter = 0
letters = []
matrix = []
dic = {}
memo = {}
sys.setrecursionlimit(10000) #kommer frya min dator men men hihi
for line in sys.stdin:
    lines = line.split()
    if counter == 0:
        for linan in lines:
            letters.append(linan)
        counter += 1
    elif counter <= len(letters):
        matrix.append(lines)
        counter += 1
    elif counter == len(letters) + 1:
        for i in range(len(letters)):
            for j in range(len(letters)):
                dic[(letters[i], letters[j])] = matrix[i][j]
        counter += 1
    elif counter == len(letters) + 1:
        counter += 1
    else:
        result = Dp.dprec(lines[0], lines[1], letters, dic, memo)
        memo = result[1]
        #result = Dp1.align(lines[0], lines[1], letters, matrix)
        print(result[0][0], result[0][1])

       
        


        

        


