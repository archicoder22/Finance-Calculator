import math

# this program allows the user to access two financial calculators:
# an investment calculator and a home loan repayment calculator

# request the user to select which type of calculator they want to use
calculator_type = input("""Choose either \"investment\" or \"bond\" from the menu below to proceed:

investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan""")

# ensure that user's input is recognizable name by correct capitalization
calculator_type = calculator_type.lower()

# request data, calculate the amounts of interest or repayment and print the answer
if calculator_type == "investment":

    return_amount = float()
    amount_of_deposit = float(input("Please enter the amount you want to deposit:"))
    interest_rate = float(input("Please enter the interest rate (number only)."))
    years_of_investment = int(input("Please enter the number of years you plan on investing."))
    interest_type = input("Please enter interest type you want. Type \"simple\" or \"compound\".")

    if interest_type == "simple":
        return_amount = amount_of_deposit * (1 + interest_rate / 100 * years_of_investment)

    elif interest_type == "compound":
        return_amount = amount_of_deposit * math.pow((1 + interest_rate / 100), years_of_investment)

    print(f"The return amount on your investment is: {round(return_amount, 2)}")

elif calculator_type == "bond":

    house_value = float(input("Please give the present value of the house."))
    interest_rate = float(input("Please type the interest rate."))
    no_of_months = int(input("Please give the number of months you plan to take to repay the loan."))
    interest_rate_percentage = interest_rate / 100
    monthly_interest_rate = interest_rate_percentage / 12

    repayment_per_month = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** (-no_of_months))

    print(f"Your monthly repayment is: {round(repayment_per_month, 2)}.")
