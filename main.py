
# Online Python - IDE, Editor, Compiler, Interpreter

print("Welcome to the tip calculator!")
bill_total = input("How much was the total bill? (Enter amount without currency symbol) ")
bill_total_as_float = float(bill_total)
print(bill_total_as_float)
number_in_party = input("How many persons will split the bill? ")
number_in_party_as_int = int(number_in_party)
calculation = bill_total_as_float / number_in_party_as_int
calculation_with_tip = round(calculation * 1.12, 2)
print(f"Each person should pay: ${calculation_with_tip}")
