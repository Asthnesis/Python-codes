# Eligible voter
countries =["kenya","uganda","tanzania"] 

country = input("Enter country: ").lower()
age =int(input("Enter age: ")) 

if country in countries and age >=18:
  print("Legible to vote")
else:
  print("Ineligible to vote")