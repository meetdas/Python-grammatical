print('Welcome to the tip calculator.')
total_bill = float(input("What is your total bill? $:"))
tip = float(input("How much tip do you want to give? $:"))
person = int(input("How many friends you are?:"))
result = (total_bill + tip) / person
print(result)