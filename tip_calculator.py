print("Welcome to the tip calculator")

bill = input("What was the total bill? $")
bill = float(bill)

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
percentage = int(percentage)

people = input("How many people to split the bill? ")
people = int(people)

tip_percent = people / 100
total_tip_amount = bill * tip_percent
total_bill = bill + total_tip_amount
total_bill = round(total_bill, 2)

print(f"Each person should pay: ${total_bill}")