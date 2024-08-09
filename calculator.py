loan_amount = 31523
annual_interest_rate = 6.49 / 100
loan_term_years = 7
payments_per_year = 26  # Bi-weekly payments

# Calculate the number of total payments
total_payments = loan_term_years * payments_per_year

# Calculate the bi-weekly interest rate
bi_weekly_interest_rate = (annual_interest_rate / payments_per_year)

# Calculate the bi-weekly payment using the amortization formula
bi_weekly_payment = loan_amount * (bi_weekly_interest_rate * (1 + bi_weekly_interest_rate) ** total_payments) / ((1 + bi_weekly_interest_rate) ** total_payments - 1)

print("Initial bi-weekly payment at start of loan is ", str(round(bi_weekly_payment,2)))

# Recalculating after 12 months with a $1,000 extra payment

# Initial calculation parameters
months_passed = 12
bi_weekly_periods_passed = months_passed * payments_per_year / 12

# Calculate the remaining balance after 12 months without the $1,000 payment
remaining_balance = loan_amount * (1 + bi_weekly_interest_rate) ** bi_weekly_periods_passed - \
                    (bi_weekly_payment * ((1 + bi_weekly_interest_rate) ** bi_weekly_periods_passed - 1) / bi_weekly_interest_rate)
                    
print("The remaining balance is:", str(round(remaining_balance,2)) ,"after",months_passed,"months" )                  

# Apply the $1,000 extra payment
new_balance = remaining_balance - 1000

total_balance_with_interest = 182*215.73


# Calculate the new number of remaining payments
new_remaining_payments = total_payments - bi_weekly_periods_passed

# Recalculate the new bi-weekly payment with the updated balance
new_bi_weekly_payment = new_balance * (bi_weekly_interest_rate * (1 + bi_weekly_interest_rate) ** new_remaining_payments) / \
                         ((1 + bi_weekly_interest_rate) ** new_remaining_payments - 1)
print("At this point bi-weekly payemnt is ", str(round(new_bi_weekly_payment,2)))

#calculating how much interest is saved
total_interest = (bi_weekly_payment*total_payments)-loan_amount
total_interest_extra_payment = (bi_weekly_payment*bi_weekly_periods_passed)+(new_bi_weekly_payment*new_remaining_payments) -(loan_amount+1000)
interest_saved = total_interest - total_interest_extra_payment



print("you have saved ", interest_saved)
