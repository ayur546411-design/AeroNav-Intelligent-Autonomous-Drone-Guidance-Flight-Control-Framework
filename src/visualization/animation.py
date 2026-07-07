import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animate_2d_trajectory(time, target_x, target_y, actual_x, actual_y, title="2D Trajectory Animation"):
    """
    Animates a 2D trajectory tracking simulation.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    
    # Set plot limits based on data
    all_x = np.concatenate([target_x, actual_x])
    all_y = np.concatenate([target_y, actual_y])
    margin_x = (np.max(all_x) - np.min(all_x)) * 0.1
    margin_y = (np.max(all_y) - np.min(all_y)) * 0.1
    
    ax.set_xlim(np.min(all_x) - margin_x, np.max(all_x) + margin_x)
    ax.set_ylim(np.min(all_y) - margin_y, np.max(all_y) + margin_y)
    ax.grid(True)
    ax.axis('equal')
    
    target_line, = ax.plot([], [], 'b--', label='Target')
    actual_line, = ax.plot([], [], 'r-', label='Actual')
    agent_dot, = ax.plot([], [], 'ro', markersize=8)
    
    ax.legend()
    
    def init():
        target_line.set_data([], [])
        actual_line.set_data([], [])
        agent_dot.set_data([], [])
        return target_line, actual_line, agent_dot
        
    def update(frame):
        # Draw full target trajectory
        target_line.set_data(target_x, target_y)
        
        # Draw history up to current frame
        actual_line.set_data(actual_x[:frame], actual_y[:frame])
        
        # Draw current position
        agent_dot.set_data([actual_x[frame]], [actual_y[frame]])
        
        return target_line, actual_line, agent_dot
        
    ani = animation.FuncAnimation(fig, update, frames=len(time), init_func=init, blit=True, interval=20)
    plt.show()
    return ani
