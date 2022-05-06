# Currency exchange
dollar = 70.25
sol = 83.3
gst = 5.17
gmt = 2.46

# Cross price
cross1_price = 14.3*sol
cross2_price = 14.3*sol
cross1_sell_price = 13.3*sol
cross2_sell_price = 13.3*sol
daily_proffit = 1.5*gst
current_price = 0

# Function
def calc(cros_price, cur_spent, d_prof, cros_sel_price):
    counter = 1
    proffit = 0
    while (proffit <1):
        print(f'Mint № {counter}')
        cur_spent = 0
        print(cur_spent)
        # Buying 2 crosses
        cur_spent -= cros_price
        print(cur_spent)
        print('Now you get 2 crosses')
        # Upgrading 2 crosses to 5th level
        cur_spent -= (20*gst + 10*gmt)*2
        print(cur_spent)
        # Earning some gst for running
        cur_spent += d_prof*2*2
        print(cur_spent)
        print('Now you get 5 level crosses')
        # Minting of 2 more crosses
        cur_spent -= (120*gst + 80*gmt)*2
        print(cur_spent)
        print('Now you minted 2 more crosses')
        # Selling 2 old crosses
        cur_spent += cros_sel_price
        print(cur_spent)
        print('Now you sold 2 parents crosses')
        counter +=1
        # New crosses costs total spent
        cros_price = -cur_spent
        proffit = cur_spent
        #print(cur_spent)
        print('-------------------------------')
    print(f'First invest money = ${cross1_price + cross2_price}') # Нужно взять cur_spent из первой итерации
    print(f'Total {counter-1} times minted. Total spent time {(counter-1)*3} days\nAnd now we have 2 new crosses and ${proffit}')

calc(cross1_price + cross2_price, current_price, daily_proffit, cross1_sell_price + cross2_sell_price)