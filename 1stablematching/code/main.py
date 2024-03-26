import sys
import time

from company import Company
from student import Student
from stableMatching import StableMatching

students = []
companies = []
counter = 0
nbrElem = 0
bigString = []

def strtoint(strList):
    intNbrs = list(map(int, strList))
    return intNbrs

def containsID(id):
    idExists = False
    for comp in companies:
        if comp.id == id:
            idExists = True
    return idExists

"""
Read the file line by line and parses the input 
"""
for line in sys.stdin:
    if counter == 0:
        nbrElem = int(line) + 1
        counter += 1
    else : 
        nbrs = line.split()
        for nbr in nbrs:
            bigString.append(nbr)

while len(bigString) != 0:
    splitLine = bigString[:nbrElem]
    bigString = bigString[nbrElem:]
    splitLine = strtoint(splitLine)
    splitLine1 = splitLine.pop(0)
    if containsID(splitLine1):
        students.append(Student(splitLine1, splitLine))
    else:
        splitLine = StableMatching.sortPref(splitLine)
        companies.append(Company(splitLine1, splitLine))

sortCompanies = sorted(companies, key=lambda x: x.id)

#measures the time of the algorithm
start_time = time.time()
StableMatching.algoritm(sortCompanies, students)
end_time = time.time()
execution_time = (end_time - start_time) 
print("Total time was: ", execution_time, "s")
    
"""
0testsmall: 20-33 ns
1testsmallmessy: 20-31 ns
2testmid: 29-61 ns
3testlarge: 296-523 ns
4testhuge: 0.83 s
5testhugemessy: 0.83 s
"""