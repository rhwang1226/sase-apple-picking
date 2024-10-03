# Djikstra's Algorithm for SASE Apple Picking Car Assignments
## Algorithm Overview

My Society of Asian Scientists and Engineers (SASE) chapter is going on an apple picking field trip, and I needed to organize transportation. I saw in this a potential to apply computer science concepts, which is an opportunity I couldn't pass; I love it when concepts of computer science have real life applications. The goal was to make this assignment as efficient as possible, ensuring that riders were paired with drivers based on proximity to minimize travel time. To achieve this, I implemented a custom approach based on Dijkstra's algorithm, which is traditionally used for finding the shortest paths between points in a graph.

### Step-by-Step Breakdown

#### 1. Data Preparation
Each driver and rider was represented by a `Member` class that holds their name, their geographical coordinates (x and y values), and the number of available seats in the case of drivers. This data was extracted from a `data.csv` file, where both the driver and rider details were stored. Drivers are identified by their positive seat count, while riders have zero seats.

#### 2. Distance Calculation
To simulate the "closeness" between riders and drivers, I calculated the Euclidean distance between the coordinates of each rider and driver. This straightforward distance calculation forms the basis of how riders are assigned to the nearest drivers.

#### 3. Priority Queue for Assignments
For each rider, I used a priority queue (implemented via Python’s `heapq`) to store the distances to all drivers. The priority queue automatically orders these drivers from closest to farthest. The rider is then assigned to the closest available driver (i.e., the driver with remaining seats) by popping the driver from the heap with the smallest distance. This ensures that every rider is assigned to the most geographically optimal driver.

#### 4. Driver Preferences
In addition to the algorithmic assignment, some drivers requested to drive specific friends. To accommodate these preferences, I manually removed those friends from the `data.csv` file, effectively removing them from the pool of riders needing assignment. I also decremented the available seat count for these drivers, reflecting the reserved spots for their friends. This ensured that the program would only assign the remaining riders to drivers based on availability and proximity.

#### 5. Handling Seat Capacity
Once a rider is assigned to a driver, the driver’s available seat count is decremented. If a driver’s seat count reaches zero, that driver is no longer eligible for further assignments. The algorithm continues this process, iterating through the riders and ensuring that each one is assigned to the closest driver with available seats.

#### 6. Output
After all riders are assigned, the results are printed, showing which rider is assigned to which driver. This is done in alphabetical order of the driver’s name, making it easy to review and understand the final assignments.

### Flexibility and Real-World Application

This algorithm illustrates a practical use of Dijkstra’s principles in a real-world context. It efficiently handles geographic proximity and seat availability, but also allows for human factors, such as driver preferences for specific passengers. By combining the precision of algorithmic logic with manual adjustments, the program achieves both optimal and customized outcomes.

In this project, Dijkstra’s algorithm was adapted for a slightly different use case: instead of finding the shortest paths in a network, it was used to find the closest riders to drivers, ensuring a streamlined assignment process. The solution showcases how computer science techniques can be applied to everyday challenges in a flexible and meaningful way.

## How to Run the Program

### Prerequisites
- Ensure you have Python installed (Python 3.6 or higher is recommended).
- Make sure you have access to the `data.csv` file containing the riders and drivers information.

### Steps to Run

1. **Clone the repository:**

   First, clone the repository to your local machine using the following command:
   `git clone https://github.com/rhwang1226/sase-apple-picking.git`

2. **Navigate to the project directory:**

After cloning, navigate into the project directory:
    `cd sase-apple-picking`

3. **Prepare the `data.csv` file:**

Ensure that the `data.csv` file contains the necessary rider and driver information in the following format, with riders separated by newlines:
    `name,xcoord,ycoord,seats`
- `name`: The name of the rider or driver.
- `xcoord`: X-coordinate representing the person's location.
- `ycoord`: Y-coordinate representing the person's location.
- `seats`: The number of seats available for a driver (0 for riders).

4. **Run the program:**

Execute the Python program by running `python3 main.py`.

5. **Review the output:**

After running the program, the assignments will be printed to the console, showing which rider is assigned to each driver.
