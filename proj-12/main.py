# Shopping cart program
foods =[]
prices = []
total = 0
while True:
    food = input("Enter any food of your choice.. (press q to quit)  ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}  "))
        foods.append(food)
        prices.append(price)
         
for food in foods:
    print(food, end=" ")
for price in prices:
    total += price
print()   
print(f"your total is ${total}" )