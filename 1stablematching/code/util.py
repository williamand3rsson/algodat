from student import Student
from company import Company

class Util:

    def sortPref(prefList):
        tempList = [0] * (len(prefList))
        for i in range(len(prefList)):
            tempList[prefList[i] - 1] = i + 1
        return tempList

    def findMatches(companyList, studentList):
        matchMap = {}
        while len(studentList) != 0:
            curStudent = studentList.pop(0)
            favCompany = companyList[curStudent.prefList[0] - 1]
            stud = matchMap.get(favCompany)
            #print(favCompany)
            ## if there is no students applied to the company:
            if favCompany not in matchMap:
                curStudent.prefList.pop(0)
                matchMap[favCompany] = curStudent
            elif (favCompany.prefList[stud.id - 1] > favCompany.prefList[curStudent.id - 1]):
                tempStud = stud
                curStudent.prefList.pop(0)
                matchMap[favCompany] = curStudent
                studentList.append(tempStud)
            else:
                curStudent.prefList.pop(0)
                studentList.append(curStudent)

        ##sorts the matchMap after id of the key in acsending order
        sorted_matchMap = {k: matchMap[k] for k in sorted(matchMap.keys(), key=lambda x: x.id)}
        
        for comp, stud in sorted_matchMap.items():
            ##print(f"{obj.id} : {obj1.id}")
            print(f"{stud.id}")



