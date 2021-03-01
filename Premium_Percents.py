#calculates percent return, premium price, and dollar return

while True:
    dict_ = {'-15%':0.85, '-12.5%':0.875, '-10%':0.90, '-7.5%':0.925, '-5.0%':0.95, '5.0%':1.05, '7.5%':1.075, '10%':1.10, '12.5%':1.125, '15%':1.15, '20%':1.20, '30%':1.30, '40%':1.40, '50%':1.50, '60%':1.60, '70%':1.70, '80%':1.80, '90%':1.90, '100%':2.00}
    premium = float(input('\nEnter Premium: '))
    contracts = float(input('Enter # of Contracts: '))
    print()
    total_cost = round(premium * contracts * 100, 2)
    for x in dict_:
        premium_price = round(dict_[x] * premium, 2)
        actual_premium = round(premium_price * contracts * 100, 2)
        dollar_return = actual_premium - total_cost
        print(premium_price, x, dollar_return, '\n')
    loop_var = input('Continue? y/n: ').lower()
    if loop_var == 'n':
        break
