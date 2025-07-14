def buy_and_sell_stock(arr):
    minimum = arr[0]
    profit = 0
    best_purchase_ind = 0
    best_sell_ind = 0
    for i in range(1, len(arr)):
        intermittent_profit = arr[i] - minimum
        if intermittent_profit > profit:
            best_sell_ind = i
            profit = intermittent_profit
        if arr[i] < minimum:
            minimum = arr[i]
            best_purchase_ind = i
    print(f'My best purchase price is {minimum} at {best_purchase_ind} index and my best sell price is {profit + minimum} at {best_sell_ind} index. Profit is {profit}')


arr = [7, 1, 3, 2, 6, 4, 8, 3]
buy_and_sell_stock(arr)