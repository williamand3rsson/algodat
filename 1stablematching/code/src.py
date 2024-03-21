import sys
from company import Company
from student import Student
from util import Util

# Read the file line by line
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
        splitLine = Util.sortPref(splitLine)
        companies.append(Company(splitLine1, splitLine))

sortCompanies = sorted(companies, key=lambda x: x.id)


Util.findMatches(sortCompanies, students)