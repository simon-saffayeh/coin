import math

def change(m):
    dollar = math.floor(m)
    q = dollar * 4
    coins = m - dollar
    q_a = math.floor(coins * 4)
    coins -= q_a * 0.25
    coins = round(coins,2)
    
    d = math.floor(coins * 10)
    coins -= d * 0.1
    coins = round(coins,2)
    
    n = math.floor(coins * 20)
    coins -= n * 0.05
    coins = round(coins,2)
    p = math.floor(coins * 100)
    coins -= p * 0.01
    
    q += q_a
    count = q + d + n + p
    print('Change:')
    print(str(q) + ' Quarters')
    print(str(d) + ' Dimes')
    print(str(n) + ' Nickels')
    print(str(p) + ' Pennies')
    print('For a total of ' + str(count) + ' coins')


change(500000.68)
    