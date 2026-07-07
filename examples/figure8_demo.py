import sys
import os
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controllers.pid import PIDController
from src.dynamics.drone import Drone2D
from src.visualization.animation import animate_2d_trajectory

def get_figure8_trajectory(t):
    # Parametric figure-8 (Lissajous curve)
    A = 10.0
    B = 10.0
    omega = 0.5
    
    x = A * np.sin(omega * t)
    y = B * np.sin(2 * omega * t)
    return x, y

def main():
    dt = 0.05
    t_end = 25.0
    time = np.arange(0, t_end, dt)
    
    drone = Drone2D(mass=1.0, dt=dt)
    
    # PID controllers for X and Y axes
    kp, ki, kd = 5.0, 0.1, 3.0
    pid_x = PIDController(kp, ki, kd, dt)
    pid_y = PIDController(kp, ki, kd, dt)
    
    x_hist = []
    y_hist = []
    tx_hist = []
    ty_hist = []
    
    # Simulate disturbance halfway through
    dist_x = 0.0
    dist_y = 0.0
    
    for t in time:
        if t > t_end / 2:
            dist_x = 2.0  # Constant wind in X direction
            dist_y = -1.5 # Constant wind in Y direction
            
        tx, ty = get_figure8_trajectory(t)
        
        x, y, vx, vy = drone.get_state()
        
        error_x = tx - x
        error_y = ty - y
        
        force_x = pid_x.update(error_x)
        force_y = pid_y.update(error_y)
        
        drone.update(force_x, force_y, dist_x, dist_y)
        
        x_hist.append(x)
        y_hist.append(y)
        tx_hist.append(tx)
        ty_hist.append(ty)
        
    print("Simulation complete. Starting animation...")
    animate_2d_trajectory(time, tx_hist, ty_hist, x_hist, y_hist, title="Drone Figure-8 Trajectory Tracking")

if __name__ == '__main__':
    main()
