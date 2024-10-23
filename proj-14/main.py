# Creating a number pad
num_pad =((1, 2, 3),
         (4, 5, 6),
         (7, 8, 9),
         ("*", 0, "#"))
print(num_pad)

for num in num_pad:
    for items in num:
        print(items, end=" ")
    print()