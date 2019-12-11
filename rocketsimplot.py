'''Welcome to the Rocket Launch Simulation Workshop!

This is the main file you will be using. You won't need any other files.
- To run the code, press F5.
- In case the pygame visualisation window would be stuck, type drawing.pg.quit() in the
  IPython console and press enter.
  
Good luck! Please feel free to ask questions.

Workshop by: Team Voorlichting (Study-AE@tudelft.nl)
Version: 1.1
'''

# =============================================================================
# Preparation of the simulation
# =============================================================================
# Import required packages
from tools import drawing
from tools import timer
from matplotlib import pyplot as plt

# Create simulation window, size in pixels (1 pixel = 1 m)
xmax      = 1056        # [pixels]
ymax      = 594         # [pixels]
drawing.window(xmax, ymax)

# Load and scale simulation images
imgbg     = drawing.scaleimage(drawing.loadimage('images/background.png'), (xmax,ymax))
imgrocket = drawing.scaleimage(drawing.loadimage('images/rocket.png'), (128,128))

# Parameters of the rocket
neng      = 9           # Number of engines [-]
threng    = 750000      # Thrust per engine [N]
cdrag     = 0.5         # Drag coefficient [-]
S         = 10.52       # Frontal area (d = 3.66 m, calculate offline) [m2]
fuelflow  = 2555.0      # Total fuel flow [kg/s]

# Constants
g         = 9.81        # Gravity acceleration [m/s2]
rho       = 1.225       # Air density [kg/m3]

# Initial conditions of the rocket, these non-constant values will be updated during the simulation loop!
h         = 0.0         # Initial altitude [m]
vy        = 0.0         # Initial speed [m/s]
m         = 333400.0    # Initial mass [kg]

# Make empty tables
ttab      = []          # Time
htab      = []          # Altitude
vtab      = []          # Speed
atab      = []          # Acceleration
mtab      = []          # Mass

# =============================================================================
# Simulation of the rocket launch
# =============================================================================
# Start the clock
t = timer.start()

# Start the simulation, loop as long as running equals True
running = True
while running == True:
    # Calculate forces: use the variable names and NOT the value itself!
    Fgrav = 
    Fthr  = 
    Fdrag = 

    # Sum of the forces, check the signs of the forces using the free body diagram
    Ftot = 

    # Calculate the vertical acceleration
    ay = 

    # Calculate time step and update the vertical speed and position
    dt = timer.timestep()   # This function calculates and returns the value of dt for every loop
    vy = vy + ay*dt         # Update speed
    h = h + vy*dt           # Update height

    # Update the mass of the rocket
    m = 
    
    # Draw new frame
    drawing.clear()
    drawing.paste(imgbg, xmax/2, ymax) # Background picture in midbottom screen
    drawing.paste(imgrocket, xmax/2, 30+ymax-h) # Rocket picture with variable vertical location
    close = drawing.showframe() # Includes quit checking (returns True if pressing ESC or close window)

    # Add values to tables
    ttab.append(timer.time())
    htab.append(h)
    vtab.append(vy)
    atab.append(ay)
    mtab.append(m)

    # End simulation when the rocket is higher than 500m or when the user ends the simulation manually
    if h > 500 or close == True:
        running = False

# Close simulation window
drawing.closewindow()

# =============================================================================
# Show the simulation results if the user did not end the simulation manually
# =============================================================================
if close != True:
    # Draw plots (4 subplots)
    plt.close('all')
    
    plt.figure(1)
    plt.title('Altitude [m] vs Time [s]')
    plt.plot(ttab,htab)
    
    plt.figure(2)
    plt.title('Speed [m/s] vs Time [s]')
    plt.plot(ttab,vtab)
    
    plt.figure(3)
    plt.title('Acceleration [m/s2] vs Time [s]')
    plt.plot(ttab,atab)
    
    plt.figure(4)
    plt.title('Mass [kg] vs Time [s]')
    plt.plot(ttab,mtab)
    
    # Ready drawing, show interactive window
    plt.show()

# End message
print('Ready.')
