from company import Company
from student import Student

with open('1stablematching/data/secret/2testmid.in', 'r') as file:
    # Read the file line by line
    students = []
    companies = []
    counter = 0

    def strtoint(strList):
        intNbrs = list(map(int, strList))
        return intNbrs

    for line in file:
        if counter == 0:
            counter += 1
        else :
            nbrs = line.split()
            nbrs = strtoint(nbrs)
            nbr1 = nbrs.pop(0)
            if nbrs[0] in companies:
                students.append(Student(nbr1, nbrs))
            else:
                companies.append(Company(nbr1, nbrs))


print(str(companies))
print(str(students))



             