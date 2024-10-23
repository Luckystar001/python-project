# Nested Loop

# for x in range(3):
#     for y in range (1, 10):
#         print(y, end=",")
#     print()
    
    
    
symbol = input("Enter symbol:" )
row = int(input("Enter your number of rows:" ))
column = int(input("Enter your number of columns:" ))

for x in range(row):
     for y in range (column):
         print(symbol, end=",")
     print()