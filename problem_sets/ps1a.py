# Problem set 1a
# Alec Dewulf
# Time Spent: 1.5 hours


balance = int(input("Enter the outstanding balance on your credit card: "))
a_interest = float(input("Enter the annual credit card interest rate as a decimal: "))
min_month_r = float(input("Enter the minimum monthly payment rate as a decimal: "))


result = []

def find_bal(balance):
    
    min_pay = round(min_month_r * balance, 2)
    int_paid = round(a_interest/12 * balance, 2)
    prince_p = round(min_pay - int_paid, 2)
    remaining_bal = round(balance - prince_p, 2)

    result.append(round(min_pay, 2))

    print("Minimum monthly payment:", min_pay)
    print("Principal paid:", prince_p)
    print("Remaining balance: $", remaining_bal)

    return remaining_bal

m = 1

while m <= 12:
    print("Month", m)
    balance = find_bal(balance)

    m += 1
    
print("RESULT")    
print("Toal amount paid: ", round(sum(result), 2))
print("Remaining balance: $", balance)
