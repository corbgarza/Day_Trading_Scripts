#program for stock math with T+3 on cash account making percent_return a day
#with starting_total

#initialize variables
import sys
percent_return = 1 + .16#(int(input("Enter percent return:  ")) / 100)
starting_total = 1500#int(input("Enter starting total:  "))
day_counter = 3 + 1#int(input("Enter start day:  "))
week_counter = 4#int(input("Enter number of weeks:  "))
day_trade_amount = int(starting_total / 3)
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
        count = 1
        #cycles in 3 day waves
        while count < 4:
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

        #adds weekly list to main list
        profit_chart.append(week_chart)
        profit = int(profit * percent_return)
        del profit_chart[-1]
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

profit_loop()
