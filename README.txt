Task 2: Surprising Galactus! (Arduino Apogee Detection System)
The goal of this task was to program an Arduino chipset to detect and indicate the apogee (highest point) of the module’s flight path using a pressure/force sensors.

Challenges Faced:
1.Learning wiring connections and basic C++ required for Arduino programming in TinkerCAD.
2.Figuring out a logical method to use the force/pressure sensor effectively.
3.Understanding and applying the specific Arduino code structure.

Approach:
Referred to YouTube tutorials to understand the basic syntax, wiring, and application of Arduino chipsets in TinkerCAD.

1.Assumptions
Air drag is neglected in calculations.
Maximum pressure is recorded at launch, so we use the maximum detectible force as the starting point for analysis.

2.Logic Implementation

Sensor Input:
The sensor measures the ambient atmospheric pressure (in terns of force whoch is directly proportinal to the presseure and inversely proportional to the altitude of the module).
Pressure data is smoothed using a moving average to reduce noise.

Smoothed Data Variables:
avg, s, q represent smoothed pressure (proprtional to force deteced) values at times t, t-1, and t-2.

OUTPUTS:
Ascending (Module Going Up):
If q > s > avg : Green LED lights up.
Atmospheric pressure is continuously decreasing.

At Apogee (Peak Reached):
If q > s < avg : Yellow LED + Buzzer ON.
There is a slight delay due to smoothing, but indicates apogee detection.

Descending (Module Coming Down):
If q < s < avg :Only Yellow LED ON.
Atmospheric pressure is continuously increasing.

For times when the avg=s=q, we use a Red LED to show standby/rest condition.

Output Indicators
Green LED : Ascending.
Yellow LED + Buzzer : Apogee detected.
Yellow LED : Descending.
Red LED : Standby

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Task 1: Planning to Surprise Galactus (Flight Altitude and Velocity Animation)

This task involves writing a python code to animate the flight altitude and velocity using the pressure data from the module stored in a csv file.

Challenges Faced
1.Learning the required libraries in Python
pandas : to import the data from the CSV file
numpy : to convert data points to numerical values and calculate gradients for velocity
matplotlib : to plot and animate the graphs

2.Figuring out the algorithm and program logic
Converting pressure readings to altitude
Handling noisy sensor data
Animating altitude and velocity over time 


Approach:
1.We start by using pandas to import the relevant csv data points, and converting them into numerical array values using the numpy module.
2.We use the barometric equation (in the logarithmic form) to calculate the altitude of the module.
3.Using a list-array loop we take a moving average to account for faulty sensor data.
4.We then compute the slope of alt vs time graph to find velocity vs time using the gradient function of numpy module.
5.We proceed to plot the graphs using matplotlib and FuncAnimation.
