good_price = True
house_price = 1000000
downpayment = house_price *(10/100)

if good_price:
    print("you need to put down 10%")
else:
    print("you need to put down 200%")
print(f"your down payment is  {downpayment}" )