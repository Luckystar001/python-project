# For Loop
# execute a block of code a fixed number of times...You can iterate over a range, string, sequence

# for x in range(10, 50):
#     print(x)

# Reversed counting
# for x in reversed(range(1, 6)) :
#     print(x)
# print("Happy new year")


# Counting with step
# for x in reversed(range(1, 6, 2)) :
#     print(x)
# print("Happy new year")

for x in range(1, 21):
    if x == 12:
        continue
    else:
     print(x)
    #  using break
for x in range(1, 21):
    if x == 12:
        break
    else:
     print(x)
