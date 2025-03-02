print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_to_pay = (tip * bill) + bill
tip_per_person = total_to_pay / people
print(f"total_to_pay ${total_to_pay} tip_per_person ${tip_per_person}")

