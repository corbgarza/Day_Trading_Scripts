#script to build future app off; calculates max profit/loss, optimal
#strike difference, buy/sell prices to open/close
#https://www.projectoption.com/vertical-spreads-explained/

#initialize variables num_dict['']
stock_ticker = spread_type = trade_type = ''
num_dict = {'stock_price':0.0, 'upper_strike':0, 'lower_strike':0, 'spread_width':0, 'break_even':0.0, 'bid_price':0.0, 'ask_price':0.0, 'premium_price':0.0, 'max_profit':0.0,'max_loss':0.0}
loop = 'y'

#method to initialize variables for standard calculations
def standard_initialize():
    global num_list, spread_type, trade_type
    num_dict['stock_price'] = float(input('\nEnter stock price:  '))
    num_dict['upper_strike'] = int(input('Enter upper strike:  '))
    num_dict['lower_strike'] = int(input('Enter lower strike:  '))
    num_dict['spread_width'] = num_dict['upper_strike'] - num_dict['lower_strike']
    num_dict['bid_price'] = float(input('Enter bid price:  '))
    num_dict['ask_price'] = float(input('Enter ask price:  '))
    
    trade_type = input('Enter trade type: (bull/bear_call/put) ')

#method to initialize variables for reverse calculations
def reverse_initialize():
    global num_list


#method for debit spreads; bull call | bear put
def debit_spread():
    global num_list

    num_dict['premium_price'] = round((num_dict['bid_price'] - num_dict['ask_price']), 2)
    num_dict['max_profit'] = round(((num_dict['spread_width'] - num_dict['premium_price']) * 100), 2)
    num_dict['max_loss'] = round((num_dict['premium_price'] * 100), 2)
    
    if trade_type == 'bull_call':
        num_dict['break_even'] = round((num_dict['lower_strike'] + num_dict['premium_price']), 2)
    elif trade_type == 'bear_put':
        num_dict['break_even'] = round((num_dict['upper_strike'] - num_dict['premium_price']), 2)

#method for credit spreads; bear call | bull put; also converging
def credit_spread():
    global num_list

    num_dict['premium_price'] = round((num_dict['ask_price'] - num_dict['bid_price']), 2)
    num_dict['max_profit'] = round(((num_dict['premium_price'] * 100)), 2)
    num_dict['max_loss'] = round(((num_dict['spread_width'] - num_dict['premium_price']) * 100), 2)

    if trade_type == 'bear_call':
        num_dict['break_even'] = round((num_dict['lower_strike'] + num_dict['premium_price']), 2)
    elif trade_type == 'bull_put':
        num_dict['break_even'] = round((num_dict['upper_strike'] - num_dict['premium_price']), 2)

while loop == 'y':
    standard_initialize()

    if (trade_type == 'bull_call') or (trade_type == 'bear_put'):
        debit_spread()
        print('Spread width', num_dict['spread_width'], 'break even', num_dict['break_even'], 'premium paid', num_dict['premium_price'], 'max profit', num_dict['max_profit'], 'max loss', num_dict['max_loss'])
    elif (trade_type == 'bear_call') or (trade_type == 'bull_put'):
        credit_spread()
        print('Spread width', num_dict['spread_width'], 'break even', num_dict['break_even'], 'premium received', num_dict['premium_price'], 'max profit', num_dict['max_profit'], 'max loss', num_dict['max_loss'])

    loop = input('\ncontinue? y/n  ').lower()
