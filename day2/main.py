print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
person = int(input("How many people to split the bill? "))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? ")
)
tip = tip_percentage / 100
total_bill = bill + (bill * tip)
bill_per_person = "{:.2f}".format(total_bill / person)

print(f"Each person should pay: ${bill_per_person}")
