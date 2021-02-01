max_price = 0
stock = [7, 1, 5, 3, 6, 4]
stock.reverse()
stocks = []
price_map = {}
# print(type(int(stock.pop())))
for i in range(len(stock)):
    stocks.append(int(stock.pop()))
print(stocks)


for i, price in enumerate(stocks):
    #price_map[i] = price
    #print(price_map)
    for j in range(i, len(stocks)):
        max_price = max(stocks[j] - price, max_price)

print(max_price)