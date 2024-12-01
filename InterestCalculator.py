base_emi = 42057
days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
#days_in_months30 = [30,30,30,30,30,30,30,30,30,30,30,30]
#days_in_months31 = [31,31,31,31,31,31,31,31,31,31,31,31]
years = [1,1,1,1,1]
total_principal_paid = 0
total_amount_paid=0
i = 0

for year in years:
    for days in days_in_months:
        
        pa_interest = (2500000-total_principal_paid)*14.25/100

        interest_per_day = pa_interest/365
        
        monthly_interest = interest_per_day*days
        
        emi_of_the_month = base_emi + monthly_interest
        
        total_principal_paid+=base_emi
        
        total_amount_paid += emi_of_the_month
        
        i+=1
    #print(round(emi_of_the_month,2),total_principal_paid,i)
    print(round(total_amount_paid,2))