# python Temperature Converter

unit = input("Enter your Temperature (C or F)  ")
temp = float(input("Enter your Temperature  "))

if unit == "C":
    temp = round((9 * temp)/5 + 32, 1)
    unit = "Fahrenheit"
    print(f"Your Temperatue is {temp} {unit}")
elif unit == "F":
    temp = round(((temp - 32) * 5) /9 , 1)
    unit = "Celsius"
    print(f"Your Temperatue is {temp} {unit}")
else:
    print(f"{unit} is not valid")