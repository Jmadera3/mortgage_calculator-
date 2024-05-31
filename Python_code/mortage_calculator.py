print("""
#     #                                                     #####                                                                
##   ##  ####  #####  #####  ####    ##    ####  ######    #     #   ##   #       ####  #    # #        ##   #####  ####  #####  
# # # # #    # #    #   #   #    #  #  #  #    # #         #        #  #  #      #    # #    # #       #  #    #   #    # #    # 
#  #  # #    # #    #   #   #      #    # #      #####     #       #    # #      #      #    # #      #    #   #   #    # #    # 
#     # #    # #####    #   #  ### ###### #  ### #         #       ###### #      #      #    # #      ######   #   #    # #####  
#     # #    # #   #    #   #    # #    # #    # #         #     # #    # #      #    # #    # #      #    #   #   #    # #   #  
#     #  ####  #    #   #    ####  #    #  ####  ######     #####  #    # ######  ####   ####  ###### #    #   #    ####  #    #                                                                                                                                                                                                     
        
""")

#Welcome Section:
username = input("What's your name: \n")
print(f"Welcome {username}, to the online mortgage calculator.\nThis application was created to help potential home buyers estimate the price of their mortgage.\nLet's get started!!!") 

#Mortgage Formula class:
class Mortgage_Formula: 
    def __init__(self):
        #Principle amount
        ask_principle = input("Amount borrowed(e.g. starting amount) - 'if amount is 100,000 then input 100000 (don't use comma)':\n") 
        #String to number conversion:
        principle_list = [ask_principle] 
        principle_n = [eval (i) for i in principle_list]
        p = sum(principle_n)
        
        #Interest rate (yearly):
        ask_interest_rate = input("What's your yearly interest rate?:\n")
        #Sting to number conversion:
        in_r_list = [ask_interest_rate]
        in_r_n = [eval(i) for i in in_r_list]
        r_percent_whole = sum(in_r_n) 
        r = (r_percent_whole / 100)
        monthly_rate = r /12 
       
        #Loan terms/number of payments:
        ask_terms = input("What are the loan terms - how long is the loan in years. - For input just put number of years and exclude the keyword 'years':\n")
        terms_list = [ask_terms]
        term_convert = [eval (i) for i in terms_list]
        term = sum(term_convert)
        num_of_payments = term * 12
        n = num_of_payments
    
        #Monthly payment formula 
        def fixed_monthly_payment(self, p, monthly_rate, n):
            m_f1 =  (monthly_rate * p) * ((1 + monthly_rate) ** n)
            m_f2= ((1 + monthly_rate) ** n) - 1
            fixed_monthly_payment = float(m_f1 / m_f2)    
            return round(fixed_monthly_payment, 2)
        
        monthly_payment = fixed_monthly_payment(self, p, monthly_rate, n)
        print(f"Your monthly payment is estimated to be ${monthly_payment}")
        
#Add Purchase budget formula:
class Affordability_Calculator:
    def __init__(self):
        #Asking for monthly income 
        ask_income = input("What's your monthly income:\n")
        #string to int conversion
        m_i_list  = [ask_income]
        m_i_num = [eval(i) for i in m_i_list]
        monthly_income = sum(m_i_num)
        
        #sting to int conversion
        ask_percent = input("What's the percentage that your wiling - Experts recommend spending no more than 25% to 28%  of your monthly income - type in a number :\n")
        #string to int conversion
        percent_list = [ask_percent]
        percent_list_n = [eval(i) for i in percent_list]
        get_percent = sum(percent_list_n) /100
        
        
        def affordability(self):
            afford_total = int(get_percent * monthly_income)
            print(f"You maybe able to afford a ${afford_total} monthly mortgage payment.")
        
        affordability(self)

mort_for = Mortgage_Formula()

a_cal = Affordability_Calculator()