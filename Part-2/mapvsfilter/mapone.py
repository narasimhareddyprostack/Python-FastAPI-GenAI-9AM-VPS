prices=[98,198,298,398,498]

def plusone(price):
    return price+1

new_prices=list(map(plusone,prices))
print(prices)
print(new_prices)