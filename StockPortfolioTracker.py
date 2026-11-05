stock_prices = {
    "AAPL": 180,
    "TSLA": 250
}

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total = price * quantity

    print("Stock found")
    print("Total investment:", total)

    with open("stock.txt", "a") as file:
        file.write(f"stock_name: {stock_name}\n")
        file.write(f"stock_price: {price}\n")
        file.write(f"quantity: {quantity}\n")
        file.write(f"total investment: {total}\n")

else:
    print("Invalid stock name")

            