def max_profit(prices):
    if not prices:
        return None

    max_profit = 0
    min_price = prices[0]

    for price in prices:
        # Calculate the potential profit for the current day
        current_profit = price - min_price

        # Update the maximum profit if needed
        max_profit = max(max_profit, current_profit)

        # Update the minimum price if a lower price is found
        min_price = min(min_price, price)

    return max_profit

# Example usage:
prices = [7,6,4,3,1]
result = max_profit(prices)
print(result)  # Output: 5
