secret = 7

guess = int(input("Guess a number from 1 to 10: "))

while guess != secret:
    print("Wrong guess!")
    guess = int(input("Try again: "))

print("Correct guess!")
