table = {
    ('Yes', 'Yes', 'No'): 'Accept Order',
    ('Yes', 'No', 'No'): 'Wait for Restaurant',
    ('Yes', 'Yes', 'Yes'): 'Deliver Order',
    ('No', 'Yes', 'No'): 'Wait for Order',
    ('No', 'No', 'No'): 'Stay Idle',
    ('No', 'Yes', 'Yes'): 'Return to Restaurant',
    ('Yes', 'No', 'Yes'): 'Pick Up Order',
    ('No', 'No', 'Yes'): 'Go Offline'
}

percepts = []


def food_delivery_agent(percept):
    percepts.append(percept)
    action = table.get(percept, "Wait")
    return action


print("Online Food Delivery Table-Driven Agent")

n = int(input("Enter number of percepts: "))

for i in range(n):
    print(f"\nPercept {i + 1}")

    order = input("Order Available? (Yes/No): ").capitalize()
    restaurant = input("Restaurant Ready? (Yes/No): ").capitalize()
    delivery = input("Delivery Assigned? (Yes/No): ").capitalize()

    percept = (order, restaurant, delivery)
    action = food_delivery_agent(percept)

    print("Current Percept:", percept)
    print("Agent Action:", action)

print("Himani T016")
