#Calculate the toatl cost of a meal with data input at the keyboard
#6/10/2017
#CTI-110 M2HW2 - Tip Tax Total
#Thomas Hardin
#
meal_cost = float(input('Enter the cost of your meal:'))
tip = meal_cost * 0.18
tax = meal_cost * 0.07
total_amount = meal_cost + tip + tax 
print("The total tax for your meal is $", format(tip, ',.2f'))
print("The total tip for your meal is $", format(tax, ',.2f'))
print("The total cost of your meal is $", format(total_amount, ',.2f'))