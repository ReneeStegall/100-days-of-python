from xml.sax.handler import property_lexical_handler

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

result = round((bill/people) * (tip/100),2)
print(f"Each person should pay: ${result}")

# Tutorial she added a variable or there are other methods to however way works for you
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)
print(f"Each person should pay ${final_amount}")

# noticed with mines it will produce incorrectly as its only considering the tip added
# goal is the entire bill amount per person, not just the tip part
# my corrected would be
tip_percentage = tip/100
split_bill= round(bill/people,2)
bill_total_person = result+split_bill
print(f"Each person should pay ${bill_total_person}")