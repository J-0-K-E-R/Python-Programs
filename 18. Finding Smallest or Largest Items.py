# In this, we'll use heapq library to find the n number of largest or smallest items from any type of dataset.


import heapq

rand = [15, 85, 148, 68981, 2, 0, 48, 16849, 7955, 68894, 999]
print(heapq.nlargest(4, rand))                                      # This will return the first 4 largest items.

stocks = [
    {'Name': 'GOOG', 'Price': 1175.91},
    {'Name': 'DOW J', 'Price': 26007.07},
    {'Name': 'AAPL', 'Price': 199.04},
    {'Name': 'SBUX', 'Price': 95.22},
    {'Name': 'NKE', 'Price': 81.28},
    {'Name': 'MSFT', 'Price': 135.28}
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['Price'])) # This will return the 2 smallest items with key as 'Price'