from student import Student
from company import Company

class Util:

    def findMatches(companyList, studentList):
        matchMap = {}
        while len(studentList) != 0:
            curStudent = studentList.pop(0)
            favCompany = companyList[curStudent.prefList[0] - 1]
            stud = matchMap.get(favCompany)
            ## if there is no students applied to the company:
            if favCompany not in matchMap:
                curStudent.prefList.pop(0)
                matchMap[favCompany] = curStudent
            elif (favCompany.prefList[stud.id - 1] > favCompany.prefList[curStudent.id - 1]):
                tempStud = stud
                matchMap[favCompany] = curStudent
                tempStud.prefList.pop(0)
                studentList.append(tempStud)
            else:
                curStudent.prefList.pop(0)
                studentList.append(curStudent)
        
        for obj, obj1 in matchMap.items():
            ##print(f"{obj.id} : {obj1.id}")
            print(f"{obj.id}")



