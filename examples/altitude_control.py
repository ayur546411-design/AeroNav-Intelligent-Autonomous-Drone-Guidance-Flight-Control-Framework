import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controllers.pid import PIDController
from src.dynamics.drone import Drone1D

def run_simulation(kp, ki, kd, wind_mag):
    dt = 0.05
    t_end = 15.0
    time = np.arange(0, t_end, dt)
    
    drone = Drone1D(mass=1.0, dt=dt)
    pid = PIDController(kp, ki, kd, dt)
    
    target_altitude = 10.0
    
    z_history = []
    
    for t in time:
        z, z_dot = drone.get_state()
        error = target_altitude - z
        
        control_thrust = pid.update(error)
        
        # Base thrust to hover = mass * g
        thrust = drone.mass * drone.g + control_thrust
        
        # Wind disturbance after 6 seconds
        disturbance = wind_mag if t >= 6.0 else 0.0
        
        drone.update(thrust, wind_disturbance=disturbance)
        z_history.append(drone.get_state()[0])
        
    return time, z_history, target_altitude

def main():
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(bottom=0.35)
    
    init_kp = 5.0
    init_ki = 0.5
    init_kd = 2.0
    init_wind = -5.0
    
    time, z_hist, target_alt = run_simulation(init_kp, init_ki, init_kd, init_wind)
    
    line, = ax.plot(time, z_hist, label='Drone Altitude', color='b')
    target_line = ax.axhline(target_alt, color='r', linestyle='--', label='Target Altitude')
    ax.axvline(6.0, color='gray', linestyle=':', label='Disturbance Start')
    
    ax.set_title('Drone Altitude Control with PID')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Altitude (m)')
    ax.set_ylim(0, 15)
    ax.legend()
    ax.grid(True)
    
    # Sliders
    axcolor = 'lightgoldenrodyellow'
    ax_kp = plt.axes([0.15, 0.2, 0.65, 0.03], facecolor=axcolor)
    ax_ki = plt.axes([0.15, 0.15, 0.65, 0.03], facecolor=axcolor)
    ax_kd = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor=axcolor)
    ax_wind = plt.axes([0.15, 0.05, 0.65, 0.03], facecolor=axcolor)
    
    s_kp = Slider(ax_kp, 'Kp', 0.0, 20.0, valinit=init_kp)
    s_ki = Slider(ax_ki, 'Ki', 0.0, 10.0, valinit=init_ki)
    s_kd = Slider(ax_kd, 'Kd', 0.0, 10.0, valinit=init_kd)
    s_wind = Slider(ax_wind, 'Wind', -15.0, 15.0, valinit=init_wind)
    
    def update(val):
        kp = s_kp.val
        ki = s_ki.val
        kd = s_kd.val
        wind = s_wind.val
        
        t, z, _ = run_simulation(kp, ki, kd, wind)
        line.set_ydata(z)
        fig.canvas.draw_idle()
        
    s_kp.on_changed(update)
    s_ki.on_changed(update)
    s_kd.on_changed(update)
    s_wind.on_changed(update)
    
    plt.show()

if __name__ == '__main__':
    main()
