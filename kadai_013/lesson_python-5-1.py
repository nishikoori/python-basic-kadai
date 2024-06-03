def total_price(price, tax):
    tax_amount = price*(tax / 100)
    total = price + tax_amount
    return total

print(f"{total_price(1200, 10)}円")
