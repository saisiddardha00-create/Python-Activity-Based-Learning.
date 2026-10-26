marks = int(input("Enter marks: "))
income = int(input("Enter family income: "))

if marks >= 90 and income <= 200000:
    print("Full scholarship")
elif marks >= 75 and income <= 300000:
    print("Half scholarship")
else:
    print("No scholarship")
