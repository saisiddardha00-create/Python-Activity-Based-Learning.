day = 1
total = 0

while day <= 7:
    units = int(input("Enter units used: "))
    total = total + units
    day = day + 1

print("Total weekly units =", total)
