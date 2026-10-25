material = int(input("Enter material cost: "))
labour = int(input("Enter labour cost: "))
machine = int(input("Enter machine cost: "))
selling_price = int(input("Enter selling price: "))

total_cost = material + labour + machine
profit = selling_price - total_cost

print("Total Cost:", total_cost)
print("Profit:", profit)

if profit >= 2000:
    print("Profit Target Achieved")
else:
    print("Profit Target Not Achieved")
