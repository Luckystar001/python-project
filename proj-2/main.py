# Mathematical operations
import math
x = -4
y = 3.2
z = 12

# result = abs(x)
# result = round(y)

# result = pow(z, 2)
result = math.sqrt(z)


print(result)

radius = float(input("Enter the radius of a circle:"))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)
area = round(area, 2)
print(f"The circumference of the circle is {circumference}")
print(f"The area of the circle is {area}")