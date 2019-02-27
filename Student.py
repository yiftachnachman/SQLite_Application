class Student:
    def __init__(self, FirstName, LastName, GPA, Major, FacultyAdvisor):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Major = Major
        self.GPA = GPA
        self.FacultyAdvisor = FacultyAdvisor

    def getFirstName(self):
        return self.FirstName
    def getLastName(self):
        return self.LastName
    def getMajor(self):
        return self.Major
    def getGPA(self):
        return self.GPA
    def getFacultyAdvisor(self):
        return self.FacultyAdvisor
    def getStudentTuple(self):
        return (self.getFirstName(),self.getLastName(),self.getMajor(),self.getGPA(),self.getFacultyAdvisor())
