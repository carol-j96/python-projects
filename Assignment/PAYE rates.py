def calculate_paye(taxable_income):
    #calculate PAYE based on KRA 202 Annual Tax bands
    tax=0
    remaining=taxable_income
    
    #band 1: first 24000@10%
    if remaining>0:
        taxable=min(remaining, 24000)
        tax+=taxable*0.10
        remaining-=taxable
        
    #band 2:next 8333@25%(24001-32333)
    if remaining>0:
        taxable=min(remaining, 8333)
        tax+=taxable*0.25
        remaining-=taxable
    
    #band 3:next 467667@30%(32334-500000)
    if remaining>0:
        taxable=min(remaining, 467667)
        tax+=taxable*0.30
        remaining-=taxable
    
    #band 4:next 300,000@32.5%(500,001-800,000)
    if remaining>0:
        taxable=min(remaining, 300000)
        tax+=taxable*0.325
        remaining-=taxable
    
    #band 5:above 800,000@35%
    if remaining>0:
        tax+=remaining*0.35
    return tax
def main():
    print ("KENYA PAYROLL SYSTEM")
    try:
        #1.get user input
        basic_salary=float(input("\nEnter basic salary(KES):"))
        allowances=float(input("\nEnter Total Allowances(KES):"))
        #calculate PAYE tax
        taxable_income=basic_salary+allowances
        gross_tax=calculate_paye(taxable_income)
        
        net_pay=taxable_income-gross_tax
        
        #output results
        print("NET PAY:",net_pay)
        
    except ValueError:
        print("Error: Please enter valid numbers for basic salary and allowances")
if_name_=="_main_":
    main()