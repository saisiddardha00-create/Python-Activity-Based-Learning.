salary = int(input("Enter basic salary: "))

if salary >= 20000:
    allowance = 5000
else:
    allowance = 2000

total = salary + allowance

print("Allowance =", allowance)
print("Total salary =", total)
