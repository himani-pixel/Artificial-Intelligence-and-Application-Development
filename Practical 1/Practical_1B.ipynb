# (Location, Traffic Signal, Passenger in Car, Ride Request)
table = {
   ('A', 'Green', 'No', 'Yes'): 'Pick Up Passenger',
   ('A', 'Green', 'No', 'No'): 'Move Forward',
   ('B', 'Red', 'Yes', 'No'): 'Stop',
   ('B', 'Green', 'Yes', 'No'): 'Drive to Destination',
   ('C', 'Yellow', 'No', 'No'): 'Slow Down',
   ('C', 'Green', 'No', 'No'): 'Pick Up Passenger',
   ('D', 'Red', 'Yes', 'No'): 'Stop',
   ('D', 'Green', 'Yes', 'Yes'): 'Drop Passenger'
}
sequence_table = {
   (('A', 'Green', 'No', 'Yes'),('A', 'Green', 'No', 'No')): 'Pick Up Passenger',
   (('A', 'Green', 'No', 'No'),('B', 'Green', 'Yes', 'No')): 'Drive to Destination',
   (('B', 'Red', 'Yes', 'No'),('B', 'Green', 'Yes', 'No')): 'Drive to Destination',
   (('B', 'Green', 'Yes', 'No'),('D', 'Red', 'Yes', 'No')): 'Stop',
   (('D', 'Red', 'Yes', 'No'),('D', 'Green', 'Yes', 'Yes')): 'Drop Passenger',
   (('C', 'Yellow', 'No', 'No'),('C', 'Green', 'No', 'No')): 'Slow Down'
}


percepts = []


def taxi_agent(percept):
   percepts.append(percept)


   if len(percepts) >= 2:
       last_two = tuple(percepts[-2:])
       if last_two in sequence_table:
           return sequence_table[last_two]


   return table.get(percept, "Wait")




print("===== Autonomous Taxi Table-Driven Agent =====")
n = int(input("Enter the number of percepts: "))
for i in range(n):
   print(f"\nPercept {i + 1}")


   location = input("Location (A/B/C/D): ").upper()
   signal = input("Traffic Signal (Green/Yellow/Red): ").capitalize()
   passenger = input("Passenger in Car? (Yes/No): ").capitalize()
   request = input("Ride Request? (Yes/No): ").capitalize()
   percept = (location, signal, passenger, request)
   action = taxi_agent(percept)


   print("Percept History:", percepts)
   print("Current Percept:", percept)
   print("Agent Action:", action)
print("Himani T016")
