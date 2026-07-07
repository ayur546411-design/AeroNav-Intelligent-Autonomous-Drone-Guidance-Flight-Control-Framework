# <p align="center">AeroNav</p>

<p align="center">
  <img src="assets/images/banner.png" alt="AeroNav Banner" width="100%">
</p>

<p align="center">
  <strong>Autonomous Drone Guidance & Flight Control Framework</strong>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

---

## ✨ Overview

**AeroNav** is a modern autonomous drone simulation framework built entirely in Python. It demonstrates real-world flight control concepts including **PID control**, **trajectory tracking**, **waypoint navigation**, **wind disturbance modeling**, and **interactive flight visualization**.

Designed with a modular architecture, AeroNav provides an educational and extensible platform for robotics enthusiasts, developers, and researchers interested in autonomous aerial systems.

---

# 🎬 Demo

<p align="center">
<img src="assets/demo.gif" width="850">
</p>

---

# 📸 Screenshots

| Drone Altitude Control | Figure-8 Tracking |
|:----------------------:|:-----------------:|
| <img src="assets/screenshots/altitude.png" width="400"> | <img src="assets/screenshots/figure8.png" width="400"> |

| Boat Guidance | Flight Analytics |
|:-------------:|:----------------:|
| <img src="assets/screenshots/boat.png" width="400"> | <img src="assets/screenshots/analytics.png" width="400"> |

---

# 🚀 Features

- ✈️ Autonomous Drone Flight Simulation
- 🎯 PID Flight Controller
- 🌪️ Wind Disturbance Simulation
- 📍 Waypoint Navigation
- ♾️ Figure-8 Trajectory Tracking
- 🛥️ Autonomous Boat Guidance
- 📈 Real-Time Flight Analytics
- 🎬 Interactive Animation
- 🧩 Modular Software Architecture
- 📊 Performance Visualization
- 🐍 Pure Python Implementation

---

# 🏗️ Project Architecture

```
AeroNav
│
├── assets/
│
├── src/
│   ├── controllers/
│   ├── dynamics/
│   ├── guidance/
│   ├── trajectory/
│   ├── visualization/
│   └── utils/
│
├── examples/
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AeroNav.git
```

Move inside the project

```bash
cd AeroNav
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run

```bash
python main.py
```

---

# 📂 Modules

## 🚁 Drone Dynamics

- Drone Physics
- Gravity
- Thrust
- Velocity
- Acceleration

---

## 🎯 PID Controller

- Proportional Control
- Integral Control
- Derivative Control
- Anti-Windup
- Gain Tuning

---

## 🌪️ Wind Simulation

- Constant Wind
- Gusts
- Random Disturbance
- Environmental Noise

---

## 📍 Guidance System

- Waypoint Navigation
- Path Following
- Position Error Correction

---

## ♾️ Trajectory Generator

- Circle
- Figure-8
- Spiral
- Square
- Custom Paths

---

## 🎬 Visualization

- Live Drone Animation
- Flight Dashboard
- Telemetry Graphs
- Tracking Performance

---

## 🛥️ Boat Guidance

- Autonomous Navigation
- Water Current Compensation
- Path Tracking
- Guidance Controller

---

# 📊 Flight Analytics

The simulator records:

- Altitude
- Velocity
- Position
- Error
- PID Output
- Wind Force
- Trajectory Deviation

---

# 🛠️ Built With

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| NumPy | Numerical Computing |
| SciPy | Scientific Computing |
| Matplotlib | Visualization |
| ImageIO | GIF Generation |

---

# 📈 Roadmap

- [x] PID Flight Controller
- [x] Drone Dynamics
- [x] Wind Simulation
- [x] Boat Guidance
- [x] Figure-8 Tracking
- [x] Interactive Animation
- [ ] Kalman Filter
- [ ] Obstacle Avoidance
- [ ] Computer Vision Landing
- [ ] SLAM Integration
- [ ] ROS 2 Support
- [ ] PX4 Integration
- [ ] Reinforcement Learning Controller
- [ ] Multi-Drone Swarm

---

# 🤝 Contributing

Contributions are welcome!

Feel free to submit issues, feature requests, or pull requests to improve AeroNav.

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

---

<p align="center">

**Built with ❤️ for Robotics, Autonomous Systems & Flight Control**

</p>
