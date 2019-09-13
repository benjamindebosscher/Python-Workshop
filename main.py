'''Welcome to the Rocket Launch Simulation Workshop!

This is the main file you will be using. You won't need any other files.
- To run the code, press F5.
- In case the pygame visualisation window would be stuck, type pg.quit() in the
  shell and press enter.

Good luck! If any, feel free to ask questions.

Code developped by: Team Voorlichting (Study-AE@tudelft.nl)
Version: 0.2
'''

# =============================================================================
# Preparation for the simulation
# =============================================================================
# Import required packages
import math
import pygame as pg
from src.visualisation import Environment, Rocket, plotter

# Initialise the required objects
environment = Environment()
rocket = Rocket()

# Initialise the time
pc_time_previous = pg.time.get_ticks()*0.001                # [s]
running = True

# =============================================================================
# Simulation of the rocket lauch
# =============================================================================
# Start of the simulation
while running:
    # Calculate the time step size dt from the pc time in seconds
    pc_time_current = pg.time.get_ticks()*0.001             # [s]
    dt = pc_time_current-pc_time_previous                   # [s]
    pc_time_previous = pc_time_current                      # [s]

    # Constants throught the simulation
    diameter_rocket = 3.66                                  # [m]
    nr_engines = 9                                          # [-]
    thrust_per_engine = 750000                              # [N]
    coeff_drag = 0.5                                        # [-]
    g = 9.81                                                # [m/s^2]
    massflow = 2555                                         # [kg/s]
    rho = 1.225                                             # [kg/m^3]
    pi = math.pi                                            # [-]

    # Extract rocket data from the previous loop in order to do numerical calculations
    mass_previous = rocket.mass[-1]                         # [kg]
    velocity_previous = rocket.vy[-1]                       # [m/s]
    position_previous = rocket.y[-1]                        # [m]
    time_previous = rocket.time[-1]                         # [s]

    # Calculate the current mass using the massflow and the time step dt numerically
    mass_current = mass_previous-massflow*dt

    # Calculate the TOTAL thrust of the rocket in [N]
    T = nr_engines*thrust_per_engine

    # Calculate the CURRENT weight of the rocket in [N]
    W = -mass_current*g

    # Calculate the CURRENT aerodynamic drag of the rocket in [N]
    # HINT: 'to the power of' in Python is given by **
    D = -0.5*rho*velocity_previous**2*(diameter_rocket/2)**2*pi*coeff_drag

    # Calculate the vertical acceleration of the rocket using Newtons's Second Law in [m/s^2]
    ay = (T+W+D)/mass_current

    # Calculate the vertical velocity of the rocket numerically in [m/s]
    vy = ay*dt + velocity_previous

    # Calculate the vertical position of the rocket numerically in [m]
    y = vy*dt + position_previous

    # Save the calculated results for next loop and for plotting purposes
    rocket.savemass(mass_current)
    rocket.saveacceleration(ay)
    rocket.savevelocity(vy)
    rocket.saveposition(y)
    rocket.savetime(time_previous+dt)

    # Update the pygame simulation screen with the current location of the rocket
    environment.update(y)

    # Terminate the simulation when an altitude of 500m is reached
    if y > 500:
        running = False

    # In case it is necessary to terminate the simulation earlier than an altitude of 500m
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

# =============================================================================
# Quit the visualisation and plot the results
# =============================================================================
# Quit the pygame simulation screen
pg.quit()

# Plot the rocket launch characteristics
plotter(rocket.y, rocket.vy, rocket.ay, rocket.mass, rocket.time)
