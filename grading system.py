#  Grading using average of user prompted marks

unit1 = int(input("Enter the marks for the first unit: "))
unit2 = int(input("Enter the marks for the second unit: "))
unit3 = int(input("Enter the marks for the third unit: "))

average = ((unit1+unit2+unit3)/3)

if(average>= 70 and average <=100):
    print("A")
elif(average>= 60 and average <= 69):
    print("B")
elif(average>= 50 and average <= 59):
    print("C")    
elif(average>= 40 and average <= 49):
    print("D")
elif(average>= 0 and average <= 39):
    print("Fail")
if(unit1 <1 or unit2 < 1 or unit3 <1):
    print("Mark must be a positive value")