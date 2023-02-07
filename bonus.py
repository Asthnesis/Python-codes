# Calculate the bonus of employees based on how long they have been in company

salary = int(input("Enter salary: "))
years_at_company = float(input("Years at company: "))

if(years_at_company < 6):
    net_bonus = salary *0.05
    print("Net bonus: ",net_bonus)
elif(years_at_company >=6 and years_at_company <=8):
    net_bonus = salary *0.08
    print("Net bonus: ",net_bonus)
elif(years_at_company >10):
    net_bonus = salary *0.1
    print("Net bonus: ",net_bonus)