def curconv(country,amt):
    dollars = 0
    exchange_rate = {'EUR': 1.18 , 'JPY' : 0.0096}
    try:
        return amt * exchange_rate[country]
    except:
        print('Invalid Currency')

print(curconv('EUR' ,100))
