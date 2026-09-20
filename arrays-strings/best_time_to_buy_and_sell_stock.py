"""
You are given an array prices where prices[i] is the price of a given stock on day i.
Find the maximum profit you can achieve by choosing a single day to buy and a later
single day to sell. Return the maximum profit; if no profitable trade exists, return 0.

Example:
prices = [7, 1, 5, 3, 6, 4]
return 5

How to test this:
pytest -q reference_tests -k best_time_to_buy_and_sell_stock
# or
pytest -q reference_tests/test_reference_solutions.py -k best_time_to_buy_and_sell_stock
"""


def best_time_to_buy_and_sell_stock(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit
