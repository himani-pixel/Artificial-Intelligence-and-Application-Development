table = {
   # Location, Status, Obstacle, Battery
   # Room A
   ('A', 'Dirty', 'Clear', 'High'): 'Suck',
   ('A', 'Clean', 'Clear', 'High'): 'Move_Right',
   ('A', 'Dirty', 'Obstacle', 'High'): 'Avoid_Obstacle -> Suck',
   ('A', 'Clean', 'Obstacle', 'High'): 'Avoid_Obstacle -> Move_Left',
   ('A', 'Clean', 'Clear', 'Low'): 'Go_To_Dock',


   # Room B
   ('B', 'Dirty', 'Clear', 'High'): 'Suck',
   ('B', 'Clean', 'Clear', 'High'): 'Move_Right',
   ('B', 'Dirty', 'Obstacle', 'High'): 'Avoid_Obstacle -> Suck',
   ('B', 'Clean', 'Obstacle', 'High'): 'Avoid_Obstacle -> Move_Left',
   ('B', 'Clean', 'Clear', 'Low'): 'Go_To_Dock',
}


sequence_table = {
   (('A', 'Dirty', 'Clear', 'High'),('A', 'Clean', 'Clear', 'High')): 'Move_Right',
   (('A', 'Dirty', 'Clear', 'High'),('B', 'Dirty', 'Clear', 'High')): 'Suck',
   (('A', 'Dirty', 'Clear', 'High'),('B', 'Clean', 'Clear', 'High')): 'Move_Right',
   (('A', 'Dirty', 'Clear', 'High'),('B', 'Dirty', 'Obstacle', 'High')): 'Avoid_Obstacle -> Suck',
   (('A', 'Dirty', 'Clear', 'High'),('B', 'Clean', 'Obstacle', 'High')): 'Avoid_Obstacle -> Move_Left',
   (('A', 'Clean', 'Clear', 'High'),('A', 'Clean', 'Clear', 'Low')): 'Go_To_Dock',
   (('B', 'Dirty', 'Clear', 'High'),('B', 'Clean', 'Clear', 'High')): 'Move_Right',
   (('B', 'Dirty', 'Clear', 'High'),('B', 'Dirty', 'Obstacle', 'High')): 'Avoid_Obstacle -> Suck',


   (('B', 'Dirty', 'Clear', 'High'),('B', 'Clean', 'Obstacle', 'High')): 'Avoid_Obstacle -> Move_Left',


   (('B', 'Clean', 'Clear', 'High'),('B', 'Clean', 'Clear', 'Low')): 'Go_To_Dock'
}


# Store percept history
percepts = []


# Table-driven agent
def table_driven_agent(percept):
   percepts.append(percept)


   # Check last two percepts in sequence table
   if len(percepts) >= 2:
       last_two = tuple(percepts[-2:])
       if last_two in sequence_table:
           return sequence_table[last_two]


   # Otherwise check simple lookup table
   return table.get(percept, "NoOperation")




# Main Program
print("===== Vacuum Cleaner Table-Driven Agent (2 Rooms) =====")


n = int(input("Enter number of percepts: "))


for i in range(n):
   print(f"\nPercept {i+1}")


   location = input("Enter Location (A/B): ").upper()
   status = input("Enter Status (Clean/Dirty): ").capitalize()
   obstacle = input("Enter Obstacle (Clear/Obstacle): ").capitalize()
   battery = input("Enter Battery (High/Low): ").capitalize()


   percept = (location, status, obstacle, battery)


   action = table_driven_agent(percept)


   print("\nPercept History :", percepts)
   print("Agent Action    :", action)


print("\nProgram Executed Successfully.")
print("Himani Malankar")
