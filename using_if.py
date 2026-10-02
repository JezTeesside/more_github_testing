def calculate_total(qty):
    price = 50
    total = price * qty
    if(total > 1000):
        discount = total * 10/100
    else:
        discount = total * 5/100
    print(f"Total amount for quantity {qty} is {total-discount} ")

calculate_total(0)
calculate_total(10)
calculate_total(20)
calculate_total(25)