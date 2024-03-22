import time

from student import Student
from company import Company

class StableMatching:

    """
    sorts the compaines preferencelist, to optimize the algorithm
    """
    def sortPref(prefList):
        tempList = [0] * (len(prefList))
        for i in range(len(prefList)):
            tempList[prefList[i] - 1] = i + 1
        return tempList

    """
    the algoritm making the most optimal pairs out of the students preferencelist and 
    printing it to the console
    """
    def algoritm(companyList, studentList):
        matchMap = {}
        while len(studentList) != 0:
            newStudent = studentList.pop(0)
            favCompany = companyList[newStudent.prefList[0] - 1]
            curStudent = matchMap.get(favCompany)
            if favCompany not in matchMap:  #if there is no students applied to the company:
                newStudent.prefList.pop(0)
                matchMap[favCompany] = newStudent
            elif (favCompany.prefList[curStudent.id - 1] > favCompany.prefList[newStudent.id - 1]): #if the company already has a pair but want to change
                tempStud = curStudent
                newStudent.prefList.pop(0)
                matchMap[favCompany] = newStudent
                studentList.append(tempStud)
            else:
                newStudent.prefList.pop(0)
                studentList.append(newStudent)

        #sorts the matchMap after id of the key in acsending order
        sorted_matchMap = {k: matchMap[k] for k in sorted(matchMap.keys(), key=lambda x: x.id)}
        
        #print results to the console
        for comp, stud in sorted_matchMap.items():
            print(f"{stud.id}")



