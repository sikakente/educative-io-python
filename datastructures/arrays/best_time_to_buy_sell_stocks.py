"""
Problem Statement
----------------
You are given an array prices where prices[i] is the price of a given stock on the ith day.  You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.  Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Input
-----
list of prices

Output
-------
max profit from buying and selling at the best time
"""


def max_profit(prices):
    min_price = float("inf")
    profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > profit:
            profit = price - min_price

    return profit


if __name__ == '__main__':
    import doctest

    doctest.testmod()
