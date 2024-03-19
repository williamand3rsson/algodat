class Company:

    def __init__(self, id, prefList):
        self.id = id
        self.prefList = prefList

    def sortPref(self):
        tempList = [0] * (len(self.prefList))
        for i in range(len(self.prefList)):
            tempList[self.prefList[i] - 1] = i + 1
        self.prefList = tempList 

    def __str__(self):
        return f"Id: {self.id}, Pref: {self.prefList}"