with open('1stablematching/data/sample/1.in', 'r') as file:
    # Read the file line by line
    students = []
    studentPref = []
    companies = []
    companyPref = []
    counter = 0
    for line in file:
        if counter == 0:
            counter += 1
        else :
            nbrs = line.split()
            if nbrs[0] in companies:
                students.append(nbrs[0])
                nbrs.pop(0)
                studentPref.append(nbrs)
            else:
                companies.append(nbrs[0])
                nbrs.pop(0)
                companyPref.append(nbrs)