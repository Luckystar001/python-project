# 2d lists
#  it is a lits made up of lists 

meats =      ["beef","mutton","Chicken"]
vegetables = ["Tomatoes","Cabbage","Carrot"]
fruits =     ["Oranges", "Apples", "Bananas"]


food = [meats, vegetables, fruits]
print (food[0][2])

# using neseted loops
for collection in food:
    for items in collection:
        print(items, end=" ")
    print()
    