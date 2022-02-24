stocks = {
    'GOOGLE': 435.90,
    'YOUTUBE': 80.76,
    'TIKTOK' : 700.89,
    'AMAZON': 200.54
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.keys(), stocks.values())))
