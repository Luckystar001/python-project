#  While Loops
# While loops xcutes codes while some conditions remain true

num = int(input("Enter a number from 1-10  "))
while num < 1 or num >10:
    print(f"Your {num} is not valid. Enter a number from 1-10")
    num = int(input("Enter a number from 1-10  "))
print(f"Your number is {num}")