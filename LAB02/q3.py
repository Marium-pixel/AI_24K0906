#q3:
class StudentMarks:
    def __init__(self,name):
        self.name=name
    
    def set_marks(self):
        print("marks are:", self.__marks)
         
    def get_marks(self,marks):
        self.__marks=marks
        
      
    def calculate_grade(self):
        if self.__marks >= 80:
            grade="A"
        elif self.__marks >=70:
            grade="B"
        elif self.__marks >= 60:
            grade= "C"
        else:
            grade= "D"
        
        print("grade accoridng to marks is:", grade)
        
S1 = StudentMarks("Alice")

S1.get_marks(76)
S1.set_marks()

S1.calculate_grade()

S2 = StudentMarks("BOBA")

S2.get_marks(90)
S2.set_marks()

S2.calculate_grade()
