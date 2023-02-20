# Program that prints out the grade of a student after computing the average

def grading_system(*grades):
    average = (sum(grades)/len(grades))
    if average >=70 and average <=100:
        print("A")
    elif average >=60 and average <=70:
        print("B")
    elif average >=50 and average <=59:
        print("C")
    elif average >=40 and average <=49:
        print("D")
    elif average >=30 and average <=39:
        print("E")
grading_system(20,30,40,50)