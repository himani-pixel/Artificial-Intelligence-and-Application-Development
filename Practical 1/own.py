# (Location, Temperature, Motion Detected)


table = {
   ('Living Room', 'Hot', 'Yes'): 'Turn On AC',
   ('Living Room', 'Cold', 'No'): 'Turn Off AC',


   ('Bedroom', 'Hot', 'Yes'): 'Turn On Fan',
   ('Bedroom', 'Cold', 'No'): 'Turn Off Fan',


   ('Kitchen', 'Hot', 'Yes'): 'Start Exhaust Fan',
   ('Kitchen', 'Cold', 'No'): 'Turn Off Exhaust Fan',


   ('Garage', 'Cold', 'Yes'): 'Turn On Light',
   ('Garage', 'Hot', 'No'): 'Turn Off Light'
}


percepts = []


def smart_home_agent(percept):
   percepts.append(percept)
   return table.get(percept, "No Action")


print("Smart Home Table-Driven Agent")


n = int(input("Enter number of percepts: "))


for i in range(n):
   print(f"\nPercept {i + 1}")


   location = input("Enter Location (Living Room/Bedroom/Kitchen/Garage): ").title()
   temperature = input("Enter Temperature (Hot/Cold): ").capitalize()
   motion = input("Motion Detected? (Yes/No): ").capitalize()


   percept = (location, temperature, motion)


   action = smart_home_agent(percept)


   print("Current Percept :", percept)
   print("Percept History :", percepts)
   print("Agent Action    :", action)
