# timer countdown

import time

# time.sleep(5)
# print("Enter your Name")

my_time = int(input("Enter time in seconds "))

for x in range( my_time, 0, -1):
    print (x)
    time.sleep(1)
    
 
my_name = input("Enter your Name ")
print(f"Your Name is {my_name}")