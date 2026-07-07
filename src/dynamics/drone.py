import math

class Drone1D:
    def __init__(self, mass=1.0, dt=0.05):
        self.mass = mass
        self.dt = dt
        self.g = 9.81
        self.z = 0.0
        self.z_dot = 0.0
    
    def update(self, thrust, wind_disturbance=0.0):
        # F = m*a -> a = (thrust - m*g + wind_disturbance) / m
        acceleration = (thrust - self.mass * self.g + wind_disturbance) / self.mass
        self.z_dot += acceleration * self.dt
        self.z += self.z_dot * self.dt
        
        # Ground constraint
        if self.z < 0:
            self.z = 0
            self.z_dot = 0
            
    def get_state(self):
        return self.z, self.z_dot
        
    def reset(self):
        self.z = 0.0
        self.z_dot = 0.0

class Boat2D:
    def __init__(self, mass=10.0, dt=0.1):
        self.mass = mass
        self.dt = dt
        self.x = 0.0
        self.y = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.drag_coeff = 0.5
        
    def update(self, thrust_x, thrust_y, current_x=0.0, current_y=0.0):
        # Simple dynamics with drag
        ax = (thrust_x - self.drag_coeff * self.vx + current_x) / self.mass
        ay = (thrust_y - self.drag_coeff * self.vy + current_y) / self.mass
        
        self.vx += ax * self.dt
        self.vy += ay * self.dt
        
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt
        
    def get_state(self):
        return self.x, self.y, self.vx, self.vy
        
    def reset(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        self.vx = 0.0
        self.vy = 0.0

class Drone2D:
    def __init__(self, mass=1.0, dt=0.05):
        self.mass = mass
        self.dt = dt
        self.x = 0.0
        self.y = 0.0
        self.vx = 0.0
        self.vy = 0.0
        
    def update(self, force_x, force_y, dist_x=0.0, dist_y=0.0):
        ax = (force_x + dist_x) / self.mass
        ay = (force_y + dist_y) / self.mass
        
        self.vx += ax * self.dt
        self.vy += ay * self.dt
        
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt
        
    def get_state(self):
        return self.x, self.y, self.vx, self.vy
        
    def reset(self):
        self.x = 0.0
        self.y = 0.0
        self.vx = 0.0
        self.vy = 0.0
