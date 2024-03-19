with open('1stablematching/data/secret/2testmid.in', 'r') as file:
    # Read the file line by line
    students = []
    studentPref = []
    companies = []
    companyPref = []
    counter = 0
    def sortPref(prefList):
        tempList = [0] * (len(prefList))
        for i in range(len(prefList)):
            tempList[prefList[i] - 1] = i + 1
        return tempList
    def strtoint(strList):
        intNbrs = list(map(int, strList))
        return intNbrs
        




    for line in file:
        if counter == 0:
            counter += 1
        else :
            nbrs = line.split()
            nbrs = strtoint(nbrs)
            if nbrs[0] in companies:
                students.append(nbrs[0])
                nbrs.pop(0)
                studentPref.append(nbrs)
            else:
                companies.append(nbrs[0])
                nbrs.pop(0)
                nbrs = sortPref(nbrs)
                companyPref.append(nbrs)
print(companyPref)
print(companies)
print(studentPref)
print(students)


             