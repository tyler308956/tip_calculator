print("Welcome to the tip calculator!")
bill_total = float(input("How much was the total bill? $"))
tip = int(input("How much tip would you like to give? 12, 15, or 20 (Do not add percentage sign)"))
number_in_party = int(input("How many persons will split the bill? If you are not splitting the bill, input the number 1. Otherwise, enter the number of persons splitting the bill. "))
tip_as_percent = tip / 100
total_tip_amount = bill_total * tip_as_percent
bill_total_with_tip = bill_total + total_tip_amount
bill_total_per_person = bill_total_with_tip / number_in_party
final_amount = round(bill_total_per_person, 2)
final_amount = "{:.2f}".format(bill_total_per_person)
print(f"Each person should pay: ${final_amount}")
