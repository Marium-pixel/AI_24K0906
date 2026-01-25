students = {}
for i in range(3):
    name=input("enter your name")
    marks=int(input("enter your marks"))
    students[name]=marks

for name,marks in students.items():
    print(name , ":" , marks)
