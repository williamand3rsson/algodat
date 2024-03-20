from company import Company
from student import Student
from util import Util

with open('1stablematching/data/secret/3testlarge.in', 'r') as file:
    # Read the file line by line
    students = []
    companies = []
    counter = 0

    def strtoint(strList):
        intNbrs = list(map(int, strList))
        return intNbrs
    
    def containsID(id):
        idExists = False
        for comp in companies:
            if comp.id == id:
                idExists = True
        return idExists


    for line in file:
        if counter == 0:
            counter += 1
        else :
            nbrs = line.split()
            nbrs = strtoint(nbrs)
            nbr1 = nbrs.pop(0)
            if containsID(nbr1):
                students.append(Student(nbr1, nbrs))
            else:
                companies.append(Company(nbr1, nbrs))

    Util.findMatches(companies, students)



             