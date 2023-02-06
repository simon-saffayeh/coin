import math

def change(m):
    dollar = math.floor(m)
    q = dollar * 4
    coins = round(m - dollar,2)
    q_a = math.floor(coins/25)
    print(dollar)
    print(coins)
    print(q_a)

change(50.40)
    