import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# loading the data from the CSV raw data file
FILE = "Raw_Test_Flight_Data_25 - Sheet1.csv"
COL = "Pressure (Pa)"
dt = 1.0  # time delay

# reading the  CSV data points
df = pd.read_csv(FILE)
pressure = pd.to_numeric(df[COL], errors="coerce").fillna(
    method="bfill").fillna(method="ffill").to_numpy()
time = np.arange(len(pressure)) * dt

#finding values of altitude using the barometric relation
P0, T0, g, M, R = 101325, 288.15, 9.80665, 0.0289644, 8.3144598
altitude = (T0 * R / (M * g)) * np.log(P0 / pressure)

#smoothening the graph by taking the moving average to account for any erroneous readings

def moving_avg(arr, window=5):
    smoothed = []
    for i in range(len(arr)):
        start = max(0, i - window // 2)
        end = min(len(arr), i + window // 2 + 1)
        total = 0
        count = 0
        for j in range(start, end):
            total += arr[j]
            count += 1
        smoothed.append(total / count)
    return np.array(smoothed)


alt_smooth = moving_avg(altitude, window=5)

# computing velocity using numpy module
velocity = np.gradient(alt_smooth, dt)

# animated graph setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# labelling of the required graphs 

ax1.set_title("Altitude vs Time (Smoothed)")
ax1.set_ylabel("Altitude (m)")
ax2.set_title("Velocity vs Time (Smoothed)")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Vertical Velocity (m/s)")

alt_line, = ax1.plot([], [], color="blue", lw=2)
vel_line, = ax2.plot([], [], color="red", lw=2)

ax1.set_xlim(0, max(time))
ax1.set_ylim(min(alt_smooth)-10, max(alt_smooth)+10)
ax2.set_xlim(0, max(time))
ax2.set_ylim(min(velocity)-10, max(velocity)+10)

# creating animation functions

def init():
    alt_line.set_data([], [])
    vel_line.set_data([], [])
    return alt_line, vel_line

def update(i):
    alt_line.set_data(time[:i], alt_smooth[:i])
    vel_line.set_data(time[:i], velocity[:i])
    return alt_line, vel_line

# setting time interval for graph animation speed

ani = FuncAnimation(fig, update, init_func=init, frames=len(
    time), interval=400, blit=True, repeat=False)

plt.tight_layout()
plt.show()


