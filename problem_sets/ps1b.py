# Problem set 1.2
# Alec Dewulf
# Time Spent 1.5 hours

o_balance = int(input("Enter the outstanding balance on your credit card: "))
a_int_rate = float(input("Enter the annual credit card interest rate as a decimal"))

month_int_r = a_int_rate / 12

# function that finds the new balance based on the minium payment
def find_new_bal(min_payment):
    new_bal = o_balance * (1 + month_int_r) - min_payment

    m = 0
    while m < 11:
        # the newer balance is the new balance + initerst- the payment
        new_bal = new_bal * (1 + month_int_r) - min_payment

        # when all the debt has been payed
        if new_bal <= 0:
            break
        
        m += 1
        
    new_bal = round(new_bal, 2)

    return new_bal


# use x (multiple of ten) as the min_payment and the right x is found when
# the new_bal returned by find_new_bal is 0 or less than 0
for x in range(1, 1000):
    x = x * 10
    find_new_bal(x)

    if find_new_bal(x) <= 0:
        break

# checking whether the last month's payment was actually needed
if find_new_bal(x) + x >= 0:
    m_needed = 11
elif find_new_bal(x) + x < 0:
    m_needed = 12


print("RESULT")
print("Monthly payment to pay off debt in 1 year:", x)
print("Number of months needed:", m_needed)
print("Balance:", find_new_bal(x))
