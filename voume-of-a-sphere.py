# Program to calculate the volume of a sphere while using a functions
def volume_of_a_sphere(pie = 3.14):
    radius = int(input("Input radius: "))
    volume = 4/3*pie*radius**3
    print(volume,"cm3")
volume_of_a_sphere()
