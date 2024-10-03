import csv
import heapq
import math
from collections import defaultdict

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

# Cluster riders by coordinates
def cluster_riders_by_coordinates(riders):
    clusters = defaultdict(list)
    for rider in riders:
        clusters[(rider.xcoord, rider.ycoord)].append(rider)
    return clusters

# Calculate Euclidean distance between two members
def calculate_distance(member1, member2):
    return math.sqrt((member1.xcoord - member2.xcoord)**2 + (member1.ycoord - member2.ycoord)**2)

def assign_riders_to_drivers(riders, drivers):
    assignments = {}

    # Cluster riders by their coordinates
    clustered_riders = cluster_riders_by_coordinates(riders)

    # Assign riders from the same coordinates to the same driver
    for coords, riders_at_same_coords in clustered_riders.items():
        pq = []
        for i, driver in enumerate(drivers):
            if driver.seats > 0:
                # Use the distance to the first rider in the group as the distance measure
                distance = calculate_distance(riders_at_same_coords[0], driver)
                heapq.heappush(pq, (distance, i))

        while pq and riders_at_same_coords:
            distance, driver_index = heapq.heappop(pq)
            driver = drivers[driver_index]
            
            # Try to assign as many riders from the same coordinates as possible
            while driver.seats > 0 and riders_at_same_coords:
                rider = riders_at_same_coords.pop(0)
                if driver.name not in assignments:
                    assignments[driver.name] = []
                assignments[driver.name].append(rider.name)
                driver.seats -= 1

    return assignments

assignments = assign_riders_to_drivers(rider_list, driver_list)

for driver in sorted(assignments.keys()):
    print("Driver " + driver + " has the following riders assigned:")
    for rider in assignments[driver]:
        print(" - " + rider)