# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125
}

print("=== Stock Portfolio Tracker ===")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' when you finish adding stocks.\n")

portfolio = {}
total_investment = 0

while True:
    stock = input("Enter stock name: ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Choose from the available stocks.\n")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    value = stock_prices[stock] * quantity
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_investment += value
    print(f"Added {quantity} x {stock} = ${value}\n")

# Display result
print("\n=== Your Portfolio ===")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${qty * stock_prices[stock]}")

print(f"\nTotal Investment: ${total_investment}")

# Save to file
with open("portfolio.txt", "w") as file:
    file.write("=== Stock Portfolio ===\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
    file.write(f"\nTotal Investment: ${total_investment}\n")

print("\nResult saved to portfolio.txt")