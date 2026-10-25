
p1 = int(input("Enter first product price: "))
q1 = int(input("Enter first product quantity: "))

p2 = int(input("Enter second product price: "))
q2 = int(input("Enter second product quantity: "))

total = p1 * q1 + p2 * q2

if total >= 1000:
    discount = total * 10 / 100
else:
    discount = 0

amount = total - discount
tax = amount * 5 / 100
final_bill = amount + tax

print("Total:", total)
print("Discount:", discount)
print("Tax:", tax)
print("Final Bill:", final_bill)
