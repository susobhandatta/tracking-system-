from math import *
import matplotlib.pyplot as plt

# Input parameters
m = float(input("Enter the mass of the rocket (kg): "))
t = float(input("Enter the thrust (N): "))
a = float(input("Enter the cross-sectional area (m²): "))
si = int(input("Enter the specific impulse (s): "))
ts = float(input("Enter the time step (s): "))
bt = int(input("Enter the burn time (s): "))
latitude = float(input("Enter the latitude of the launch site (degrees): "))

# Constants
dc = 0.5  # Drag coefficient
ga = 9.8  # Gravitational acceleration (m/s²)
p0 = 1.225  # Air density at sea level (kg/m³)
H = 8500  # Atmospheric scale height (m)
R = 6371000  # Radius of Earth (m)
Omega = 7.292e-5  # Angular velocity of Earth (rad/s)

# Initial conditions
h0 = 0  # Initial altitude (m)
v = 0  # Initial velocity (m/s)
v_earth = Omega * R * cos(radians(latitude))  # Initial velocity due to Earth's rotation

# Lists to store trajectory data
time_list = []
altitude_list = []

# Simulation loop
time = 0
for i in range(0, bt, int(ts)):
    # Calculate air density at the current altitude
    rho = p0 * exp(-h0 / H)

    # Calculate the mass flow rate
    mfr = t / (si * ga)

    # Update the rocket's mass
    m1 = m - (mfr * ts)

    # Calculate forces
    fg = m1 * ga  # Gravity force
    fd = 0.5 * rho * (v ** 2) * a * dc  # Drag force
    fn = t - fg - fd  # Net force

    # Update acceleration, velocity, and altitude
    acc = fn / m1  # Acceleration
    v1 = v + acc * ts  # Velocity
    h1 = h0 + v1 * ts  # Altitude

    # Add Earth's rotational effect to the eastward velocity (if any)
    coriolis_accel = 2 * Omega * v * sin(radians(latitude))
    v1 += coriolis_accel * ts  # Adjusted velocity

    # Update variables for the next iteration
    v = v1 + v_earth  # Total velocity includes Earth's initial velocity
    h0 = h1
    m = m1
    time += ts

    # Store data for plotting
    time_list.append(time)
    altitude_list.append(h1)

    # Print intermediate values
    print(f"Time: {time:.2f}s, Velocity: {v1:.2f} m/s, Altitude: {h1:.2f} m")

# Plot the trajectory with altitude on the x-axis
plt.plot(altitude_list, time_list, label="Rocket Trajectory")
plt.xlabel("Altitude (m)")
plt.ylabel("Time (s)")
plt.title("Rocket Trajectory with Earth's Rotation Effect")
plt.grid()
plt.legend()
plt.show()