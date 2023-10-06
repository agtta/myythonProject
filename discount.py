from datetime import date, timedelta, datetime

today = date.today()
print(today)
print(type(today))

time = datetime.now()
print(time)
print(type(time))

print(time.hour)

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0 },
    {'sku': 2, 'exp_date': today, 'price': 80.0 },
    {'sku': 3, 'exp_date': tomorrow, 'price': 20.0},
    {'sku': 4, 'exp_date': today, 'price': 50},
]
print(products)
