import random as r
import math 
import time as t

x1 = int(input("Enter x1:"))
x2 = int(input("Enter x2:"))
y1 = int(input("Enter y1:"))
y2 = int(input("Enter y2:"))
z1 = int(input("Enter z1:"))
z2 = int(input("Enter z2:"))

# Initialize start time
start_time = t.time()

target_position = (x1, y1, z1)
radar_position = (x2, y2, z2)

def target_move(target_position):
    # Move target randomly within a range
    x = target_position[0] + r.uniform(-1000, 1000)
    y = target_position[1] + r.uniform(-1000, 1000)
    z = target_position[2] + r.uniform(-1000, 1000)
    return (x, y, z)

def track(x1, y1, z1, x, y, z):
    # Calculate distance between target and radar
    d = math.sqrt((x - x1)**2 + (y - y1)**2 + (z - z1)**2)
    final_time = t.time()  # Update the final time after the movement

    # Calculate velocity if there is a non-zero time difference
    time_difference = final_time - start_time
    if time_difference > 0:
        velocity = d / time_difference
    else:
        velocity = 0  # Avoid division by zero if no time has passed

    return (velocity, d)

def lock(x2, y2, z2, x, y, z):
    # Check if the target is within the lock range
    d1 = math.sqrt((x - x2)**2 + (y - y2)**2 + (z - z2)**2)
    
    if d1 <= 2500:
        print("Target has been locked")
    else:
        print("Finding the target")

# Main loop to update the target position and track it
while True:  # Loop for 10 iterations (for example)
    target_position = target_move(target_position)  # Move the target randomly

    # Track the target and calculate distance and velocity
    velocity, distance = track(x2, y2, z2, *target_position)

    # Lock on to the target if it's in range
    lock(x2, y2, z2, *target_position)

    # Print the results for each iteration
    print(f"Velocity: {velocity:.2f} meter per second")
    print(f"Distance: {distance:.2f} meter")
    t.sleep(1)

   







   





