# Ask the user for temperature value
temp = float(input("Enter the temperature value: "))

# Ask user for the scale
scale = input("Enter the scale (C for Celsius, F for Fahrenheit): ").upper()

# Convert and print the result
if scale == "C":
    # Convert Celsius to Fahrenheit
    converted = (temp * 9/5) + 32
    print(f"{temp:.1f}°C is {converted:.1f}°F")
elif scale == "F":
    # Convert Fahrenheit to Celsius
    converted = (temp - 32) * 5/9
    print(f"{temp:.1f}°F is {converted:.1f}°C")
else:
    print("Invalid scale.")