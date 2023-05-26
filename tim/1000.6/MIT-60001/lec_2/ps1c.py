'''
https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/mit6_0001f16_ps1/
'''

annual_salary = int(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
minimum_amount_needed = (total_cost * portion_down_payment)

def calculate_months(saving_rate,annual_salary,minimum_amount_needed):
    saving_rate = saving_rate / 10000
    total_saving = 0
    monthly_saving = 0
    total_money = 0
    for i in range(37):
        if i % 6 == 0:
            annual_salary = annual_salary + (annual_salary * semi_annual_raise)
        monthly_saving = (annual_salary * saving_rate) / 12
        total_saving = total_saving + monthly_saving
        if i % 12 == 0:
            investment_gain =  total_saving * 0.04
        total_money = total_saving + investment_gain
    if abs(minimum_amount_needed - total_money) <= 100:
        return ("INRANGE")
    elif total_money < minimum_amount_needed:
        return ("LESS")
    elif total_money > minimum_amount_needed:   
        return ("MORE")

saving_rates = [i for i in range(0,10001)]
def best_saving_rate(saving_rates,annual_salary,minimum_amount_needed):
    step = 0
    start = 0
    end = len(saving_rates) - 1
    while start <= end:
        step = step + 1
        middle = (start + end) // 2
        if calculate_months(saving_rates[middle],annual_salary,minimum_amount_needed) == "INRANGE":
            return (saving_rates[middle],step)
        elif calculate_months(saving_rates[middle],annual_salary,minimum_amount_needed) == "LESS":
            start = middle + 1
        elif calculate_months(saving_rates[middle],annual_salary,minimum_amount_needed) == "MORE":
            end = middle - 1
    return ("It is not possible to pay the down payment in three years",step)

reply,step = best_saving_rate(saving_rates,annual_salary,minimum_amount_needed)
if reply != "It is not possible to pay the down payment in three years":
   print("Best savings rate:", reply / 10000)
   print("Steps in bisection search:", step)
else:
   print("It is not possible to pay the down payment in three years")
