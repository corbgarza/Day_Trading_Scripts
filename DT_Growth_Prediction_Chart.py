#program for stock math with T+2 on cash account making percent_return a day with starting total
while True:
    #initialize variables
    import sys
    percent_return = 1 + (int(input("Enter percent return:  ")) / 100)
    starting_total = int(input("Enter starting total:  "))
    day_counter = 2 + int(input("Enter start day:  "))
    week_counter = int(input("Enter number of weeks:  "))
    day_trade_amount = int(starting_total / 2.5)
    profit = int(day_trade_amount * percent_return)
    profit_chart = []
    week_chart = [0,0,0,0,0]
    weeks = week_num = week_total = week_percent_return = 0

    #produces profit predictions based off input data
    def profit_loop():
        #initialize variables
        global profit_chart, week_chart, week_num
        global day_counter, profit, weeks, week_total, week_percent_return

        #cycles weekly periods
        for x in range(0,100):
            count = 0
            
            #cycles in 2 day waves
            while count < 2:
                
                #end of week reset
                if(day_counter > 5):
                    day_counter-=5
                    week_num+=1
                    profit_chart.append(week_chart)
                    week_chart = [0,0,0,0,0]
                    
                #adds values to list and increases counts
                week_chart[day_counter-1] = profit
                day_counter+=1
                count+=1
            #END WHILE LOOP
            
            #adds weekly list to main list
            profit_chart.append(week_chart)
            profit = int(profit * percent_return)
            del profit_chart[-1]
        #END FOR LOOP
            
        #prints out data
        for x in profit_chart:
            if weeks >= week_counter:
                break
            if weeks % 4 == 0:
                print()
            for y in x:
                week_total+=y
            printstr = 'Week {} Total: {:,} {}'
            print(printstr.format(weeks, week_total, x))
            weeks+=1
            week_total = 0
        #END FOR LOOP
    #END DEF()
            
    profit_loop()
    loop_var = input('Continue? y/n:  ').lower()
    if loop_var == 'n':
        break
#END WHILE LOOP
