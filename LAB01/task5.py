def calculate_average(markslist):
    sum= markslist[0]+ markslist[1] + markslist[2]
    average = sum/3
    return average

marks = [70,80,90]
print("marks:", marks[0], marks[1], marks[2])
avg= calculate_average(marks)
print("average marks:", avg)
