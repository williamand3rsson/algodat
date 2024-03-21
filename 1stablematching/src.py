import sys
from company import Company
from student import Student
from util import Util

with open('data/secret/2testmid.in', 'r') as file:

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

    # for line in sys.stdin:
    #     if counter == 0:
    #         counter += 1
    #     else :
    #         nbrs = line.split()
    #         nbrs = strtoint(nbrs)
    #         nbr1 = nbrs.pop(0)
    #         if containsID(nbr1):
    #             students.append(Student(nbr1, nbrs))
    #         else:
    #             companies.append(Company(nbr1, nbrs))

    for line in file:
        if counter == 0:
            nbrElem = int(line[0]) + 1
            counter += 1
        else : 
            nbrs = line.split()
            for nbr in nbrs:
                bigString.append(nbr)

    while len(bigString) != 0:
        splitLine = bigString[:nbrElem]
        bigString = bigString[nbrElem:]
        ##print(splitLine)
        ##splitLine = rightLine.split()
        ##splitLine = [char for char in rightLine]
        ##print(splitLine)
        splitLine = strtoint(splitLine)
        #print(splitLine)
        splitLine1 = splitLine.pop(0)
        #print(splitLine)
        if containsID(splitLine1):
            students.append(Student(splitLine1, splitLine))
        else:
            companies.append(Company(splitLine1, splitLine))
    #print(companies)
    #print(students)

    ##for comp in companies:
    ## comp.sortPref

    Util.findMatches(companies, students)



                