bill = int(input("Enter hospital bill: "))

if bill >= 5000:
    discount = bill * 10 / 100
else:
    discount = 0

total = bill - discount

print("Discount =", discount)
print("Final bill =", total)
