
import math

# This is a Python program that allows a user to access different financial calculators
# The user inputs their amount of money to be deposited, interest rate, and number of 
# years of investment and whether they prefer simple or compound interest.
# The program outputs the total amount of interest earned and the amount of money to
# be repaid depending on the invested amount of money, interest rate, and number of years.

investment_calculator = "investment - to calculate the amount of interest you 'll earn on your investment"
bond_calculator = "bond - to calculate the amount of money you 'll have to pay on a home loan"

print(investment_calculator)
print(bond_calculator)

financial_calculator = str.casefold(input("Please enter either 'investment' or 'bond' from the menu above to proceed: "))
if financial_calculator == 'investment' or financial_calculator == 'bond':
    print("valid entry")
else:
    print("error message")

def get_input(check_whether_integer_or_not):
    while True:                                         

            try:
                return int(input(check_whether_integer_or_not))  # checking user input until it is not an integer and return it
            except ValueError:
                print("Please enter an integer")

if financial_calculator == "investment":

    p = get_input("P = amount of money that user deposits: ")
    r = get_input("r = interest rate: ")
    t = get_input("t = number of years: ")

    interest = str.casefold(input("Please enter either 'simple' or 'compound' interest: "))

    if interest == "simple":
        A = p * (1 + r/100 * t)
        print(f"£{A:.2f}")

    elif interest == "compound":
        A = p * math.pow((1 + r/100), t)
        print(f"£{A:.2f}")

elif financial_calculator == "bond":
    P = get_input("P = Present value of the house: ")
    n = get_input("n = number of months: ")
    i = get_input("i = monthly interest rate: ")

    repayment = (1 * P)/(1 - (1 + i/100/12)**(-n))
    print(f"£{repayment:.2f}")