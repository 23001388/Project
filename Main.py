import random
warning_message = [
  "You are doing well!You can save or invevest!",
  "You should be careful with your spending",
  "You are over spending and need to reduce"
  ]
def show_message(message):
   return message[random.randint(0,(len(message)-1))]
   



#Budget =
# Ask user for their income
income = input ("Enter your income: " )

#Ask user for their expenses 
print ("Enter your expenses:" )

food =float(input("please enter your food bill"))
Bills =float(input("please enter your electricity bill"))
Clothing =float(input("please enter your clothing bill"))

# List of expenses
expenses = [food, Bills, Clothing]

# Loop to calculate total expenses
Total_expenses = 0
for item in expenses:
  Total_expenses = Total_expenses + item
#Remaining_income =

# Output section
print("Budget Report")
print("Income: £", income)
print("Food: £", food)
print("Bills: £", Bills)
print("Clothing: £", Clothing)
print("Total expenses: £", Total_expenses)
remaining_money =float(income) - float (Total_expenses)
print("remaining_money: £", )
print("suggested investment (20%): £", remaining_money)

# If/elif/else advice section
if remaining_money > 300:
  print(f"{show_message(warning_message)}")
elif remaining_money > 0:
  print(f"You should be careful with your sprnding.")
else:
  print(f"You are overspending and need to reduce ")





