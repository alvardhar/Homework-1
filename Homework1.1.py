annual_salary = 60000.0
portion_saved = 0.10
total_cost = 400000.0
portion_down_payment = 0.25
r = 0.04

current_savings = 0.0
monthly_salary = annual_salary / 12
down_payment = total_cost * portion_down_payment
months = 0

while current_savings < down_payment:
    # Investment return is calculated on current savings before adding monthly savings
    current_savings += current_savings * r / 12  
    current_savings += portion_saved * monthly_salary  
    months += 1

print("Number of months:", months)






