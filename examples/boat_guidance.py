import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controllers.pid import PIDController
from src.dynamics.drone import Boat2D

def get_target_trajectory(t):
    # A simple smooth trajectory (e.g., sine wave path)
    x = 2.0 * t
    y = 5.0 * np.sin(0.5 * t)
    return x, y

def run_simulation(kp, kd, current_x, current_y):
    dt = 0.1
    t_end = 30.0
    time = np.arange(0, t_end, dt)
    
    boat = Boat2D(mass=10.0, dt=dt)
    
    pid_x = PIDController(kp, 0, kd, dt)
    pid_y = PIDController(kp, 0, kd, dt)
    
    x_hist = []
    y_hist = []
    
    target_x_hist = []
    target_y_hist = []
    
    for t in time:
        target_x, target_y = get_target_trajectory(t)
        
        x, y, vx, vy = boat.get_state()
        
        error_x = target_x - x
        error_y = target_y - y
        
        thrust_x = pid_x.update(error_x)
        thrust_y = pid_y.update(error_y)
        
        boat.update(thrust_x, thrust_y, current_x, current_y)
        
        x_hist.append(x)
        y_hist.append(y)
        target_x_hist.append(target_x)
        target_y_hist.append(target_y)
        
    return target_x_hist, target_y_hist, x_hist, y_hist

def main():
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(bottom=0.3)
    
    init_kp = 10.0
    init_kd = 5.0
    init_cx = 0.0
    init_cy = 0.0
    
    tx, ty, bx, by = run_simulation(init_kp, init_kd, init_cx, init_cy)
    
    target_line, = ax.plot(tx, ty, 'b--', label='Desired Trajectory')
    boat_line, = ax.plot(bx, by, 'r-', label='Boat Path')
    
    ax.set_title('Autonomous Boat Guidance')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.legend()
    ax.grid(True)
    ax.axis('equal')
    
    # Sliders
    axcolor = 'lightgoldenrodyellow'
    ax_kp = plt.axes([0.15, 0.2, 0.65, 0.03], facecolor=axcolor)
    ax_kd = plt.axes([0.15, 0.15, 0.65, 0.03], facecolor=axcolor)
    ax_cx = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor=axcolor)
    ax_cy = plt.axes([0.15, 0.05, 0.65, 0.03], facecolor=axcolor)
    
    s_kp = Slider(ax_kp, 'Kp', 0.0, 50.0, valinit=init_kp)
    s_kd = Slider(ax_kd, 'Kd', 0.0, 20.0, valinit=init_kd)
    s_cx = Slider(ax_cx, 'Current X', -20.0, 20.0, valinit=init_cx)
    s_cy = Slider(ax_cy, 'Current Y', -20.0, 20.0, valinit=init_cy)
    
    def update(val):
        kp = s_kp.val
        kd = s_kd.val
        cx = s_cx.val
        cy = s_cy.val
        
        _, _, bx, by = run_simulation(kp, kd, cx, cy)
        boat_line.set_xdata(bx)
        boat_line.set_ydata(by)
        
        # update axis limits if needed
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw_idle()
        
    s_kp.on_changed(update)
    s_kd.on_changed(update)
    s_cx.on_changed(update)
    s_cy.on_changed(update)
    
    plt.show()

if __name__ == '__main__':
    main()
