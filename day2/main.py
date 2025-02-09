print("Welcome to Juan's Beer Tip Calculator !")

# Get the total bill amount, tip percentage, and number of people
bill = float(input("What is the total beer tab?\n$:"))
tip = int(input("How much tip would you like to give?\nPercent:"))
split = int(input("How many friends are splitting the tab?\nPeople:"))

# Calculate the total amount each person should pay
total = ("{:.2f}".format((((bill * (tip / 100)) + bill) / split)))

# Display the result
print(f"Each person should pitch in: ${total}")
