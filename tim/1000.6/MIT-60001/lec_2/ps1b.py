'''
Enter your annual salary: 120000
Enter the percent of your salary to save, as a decimal: .10
Enter the cost of your dream home: 1000000
Number of months: 183\
1. Call the cost of your dream home total_cost.
2. Call the portion of the cost needed for a down payment portion_down_payment. For
simplicity, assume that portion_down_payment = 0.25 (25%).
3. Call the amount that you have saved thus far current_savings. You start with a current
savings of $0.
4. Assume that you invest your current savings wisely, with an annual return of r (in other words,
at the end of each month, you receive an additional current_savings*r/12 funds to put into
your savings – the 12 is because r is an annual rate). Assume that your investments earn a
return of r = 0.04 (4%).
5. Assume your annual salary is annual_salary.
6. Assume you are going to dedicate a certain amount of your salary each month to saving for
the down payment. Call that portion_saved. This variable should be in decimal form (i.e. 0.1
for 10%).
7. At the end of each month, your savings will be increased by the return on your investment,
plus a percentage of your monthly salary (annual salary / 12).
'''

annual_salary = int(input("Enter your annual salary: "))
current_savings = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_raise = float(input("Enter the semiannual raise, as a decimal: "))

portion_down_payment = 0.25
monthly_saving = (annual_salary * current_savings) / 12
monthly_rate_inv = 0.04 / 12
down_payment_needed = total_cost * portion_down_payment
total_saving = 0
num_months = 0
total_money = 0 
total_investment_gain = 0
investment_gain = 0
while down_payment_needed > total_money:
    num_months += 1
    if num_months % 6 == 1 and num_months != 1:
        annual_salary = annual_salary + (annual_salary * semi_raise)
        monthly_saving = (annual_salary * current_savings) / 12
    total_saving = total_saving + monthly_saving
    total_money = total_saving + total_investment_gain
    total_investment_gain = total_investment_gain + (total_money * monthly_rate_inv)

print ("Number of months:", num_months)
