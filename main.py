import csv
import heapq
import math

class Member:
    def __init__(self, name, xcoord, ycoord, seats):
        self.name = name
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.seats = seats

filename = "data.csv"
rider_list = []
driver_list = []

with open(filename, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        member = Member(
            name=row['name'], 
            xcoord=float(row['xcoord']), 
            ycoord=float(row['ycoord']), 
            seats=int(row['seats'])
        )

        if int(row['seats']) > 0:
            driver_list.append(member)
        else:
            rider_list.append(member)

##### DJIKSTRA'S ALGORITHM!
def calculate_distance(member1, member2):
    return math.sqrt((member1.xcoord - member2.xcoord)**2 + (member1.ycoord - member2.ycoord)**2)

def assign_riders_to_drivers(riders, drivers):
    assignments = {}
    
    # Create a priority queue for each rider
    for rider in riders:
        pq = []
        for i, driver in enumerate(drivers):
            if driver.seats > 0:
                distance = calculate_distance(rider, driver)
                heapq.heappush(pq, (distance, i))
        
        # Assign the closest available driver to the rider
        while pq:
            distance, driver_index = heapq.heappop(pq)
            if drivers[driver_index].seats > 0:
                if drivers[driver_index].name not in assignments:
                    assignments[drivers[driver_index].name] = []
                assignments[drivers[driver_index].name].append(rider.name)
                drivers[driver_index].seats -= 1
                break
    
    return assignments

assignments = assign_riders_to_drivers(rider_list, driver_list)

for driver in sorted(assignments.keys()):
    print("Driver " + driver + " has the following riders assigned:")
    for rider in assignments[driver]:
        print(" - " + rider)