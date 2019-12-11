'''Supporting script for the simulation time

Timer functions:
    - start() = start timer
    - timestep = get timestep in seconds since last call of timestep (or start first time)
    - time() = get current value of timer since start in seconds
'''

import time as timemod

# Globals
t_timer = 0.0
tstart = 0.0

def start():
    # Start timer
    global t_timer, tstart
    t_timer = timemod.time()
    tstart = t_timer

def timestep():
    # reutrn timestep
    global t_timer
    tnew = timemod.time()
    dt = tnew - t_timer
    t_timer = tnew
    return dt

def time():
    return timemod.time() - tstart
