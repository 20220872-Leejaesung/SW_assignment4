def maxProfit_bruteforce(prices):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j]-price, max_price)
    return max_price

if __name__ ==__main__:
    input_list = [7,1,5,3,6,4]
    profit= maxProfit_bruteforce(input_list)
    print(profit)
