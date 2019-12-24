balance = int(input("enter the outstanding balance on your credit card: "))
interest_rate = float(input("Enter the annual credit card interest rate as a decimal:"))

# a function that finds a total payment. Really useful to check ans        
def find_yearly_payment(monthly_payment, interest_rate, balance):

    total_payment = 0
    
    m = 0
    while m < 12:
        interest_paid = round(((interest_rate / 12) * balance), 2)
        principal_paid = monthly_payment - interest_paid
        balance = balance - principal_paid
        total_payment += principal_paid
        m += 1
             
    return round(total_payment, 2)

# defining the bounds with the help of the instructions
low = balance/ 12.0
high = (balance*(1 +(interest_rate/12.0)) **12)/12
epsilon = 0.01
ans = (high + low)/2

# a bisection search to find ans
while abs(find_yearly_payment(ans, interest_rate, balance) - balance) >= epsilon:
    if find_yearly_payment(ans, interest_rate, balance) > balance:
        high = ans
    elif find_yearly_payment(ans, interest_rate, balance) < balance:
        low = ans
    ans = (high + low) /2

# defining these outside to make calculating months_needed possible
interest_paid = round(((interest_rate / 12) * balance), 2)
principal_paid = ans - interest_paid

# calculating months needed
months_needed = 0
if find_yearly_payment(ans, interest_rate, balance) - principal_paid >= balance:
    months_needed = 11
else:
    months_needed = 12

# calculating the final balance 
final_bal = balance - find_yearly_payment(ans, interest_rate, balance)

# printing results
print("RESULT")
print("Monthly payment to pay off debt in 1 year", round(ans, 2))
print("Number of months needed:", months_needed)
print("Balance:", final_bal)
