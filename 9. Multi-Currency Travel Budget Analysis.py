
food = int(input("Enter food expense in rupees: "))
hotel = int(input("Enter hotel expense in rupees: "))
transport = int(input("Enter transport expense in rupees: "))

rate = 0.011

food_cost = food * rate
hotel_cost = hotel * rate
transport_cost = transport * rate

total = food_cost + hotel_cost + transport_cost
total = total + total * 2 / 100

print("Food Cost:", round(food_cost, 2))
print("Hotel Cost:", round(hotel_cost, 2))
print("Transport Cost:", round(transport_cost, 2))
print("Total Cost with Fee:", round(total, 2))

if hotel_cost >= food_cost and hotel_cost >= transport_cost:
    print("Largest Expense: Hotel")
elif food_cost >= transport_cost:
    print("Largest Expense: Food")
else:
    print("Largest Expense: Transport")

if total <= 300:
    print("Within Budget")
else:
    print("Budget Exceeded")
