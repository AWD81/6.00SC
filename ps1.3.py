balance = int(input("enter the outstanding balance on your credit card: "))
interest_rate = float(input("Enter the annual credit card interest rate as a decimal:"))

        
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

m_payment_l_bound = balance/ 12.0
m_payment_u_bound = (balance*(1 +(interest_rate/12.0)) **12)/12

print(m_payment_l_bound, m_payment_u_bound)

epsilon = 0.01
x = 0
guess = 0

ans = find_new_bal(x)
middle 

while (ans - balance) > epsilon:
    if (ans - balance) > m_payment_u_bound/2:
        guess = (m_payment_l_bound + m_payment_u_bound)/2
        m_payment_l_bound = guess
    elif (ans - balance) < m_payment_l_
