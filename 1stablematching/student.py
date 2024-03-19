class Student:
    
    def __init__(self, id, prefList):
        self.id = id
        self.prefList = prefList

    def __str__(self):
        return f"Id: {self.id}, Pref: {self.prefList}"
