product_price = int(input("Enter the price of the product: "))

if product_price < 100:
    final_price = product_price - (product_price * 0.02)
else:
    final_price = product_price - (product_price * 0.1)

print(f"the final price of the product is: {final_price}")