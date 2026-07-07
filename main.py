import sys
import os

# Ensure the root directory is on the path so examples can easily import src
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from examples.altitude_control import main as run_altitude
from examples.boat_guidance import main as run_boat
from examples.figure8_demo import main as run_figure8

def main():
    print("Welcome to Advanced Drone Technology Simulator!")
    print("Please select a simulation to run:")
    print("1. Drone Altitude Control (Task 1)")
    print("2. Autonomous Boat Guidance (Task 2)")
    print("3. Drone Figure-8 Trajectory (Bonus Task)")
    print("0. Exit")
    
    choice = input("\nEnter your choice (0-3): ").strip()
    
    if choice == '1':
        print("Starting Drone Altitude Control Simulation...")
        run_altitude()
    elif choice == '2':
        print("Starting Autonomous Boat Guidance Simulation...")
        run_boat()
    elif choice == '3':
        print("Starting Drone Figure-8 Trajectory Simulation...")
        run_figure8()
    elif choice == '0':
        print("Exiting.")
    else:
        print("Invalid choice. Please run the script again and select a valid option.")

if __name__ == '__main__':
    main()
