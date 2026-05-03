# RoboControl

Real-time motion control system with PID control, sensor feedback, forward kinematics, and performance metrics.

---

## Overview

RoboControl is a simulation of a real-time robot motion control system. It models how control signals are generated and applied to drive a robot toward a target position using a PID controller. The system incorporates sensor feedback with noise, simulates motion dynamics, and computes forward kinematics for a multi-joint robotic arm.

This project demonstrates core concepts used in robotics, control systems, and real-time software.

---

## Key Features

* Real-time control loop running at fixed frequency (50 Hz)
* PID-based motion control (proportional, integral, derivative terms)
* Simulated sensor feedback with noise
* Forward kinematics for a 3-link robotic arm
* Structured logging for system state tracking
* Metrics for evaluating control performance

---

## System Architecture

```id="cz0c4t"
Target Position → PID Controller → Control Signal → Motion Simulation
                                      ↓
                               Sensor Feedback
                                      ↓
                              Error Computation
                                      ↓
                              Metrics & Logging
```

---

## How It Works

### 1. PID Controller

The PID controller computes a control signal based on:

* Current error (target − sensed position)
* Accumulated past error
* Rate of change of error

This allows the system to minimize error while maintaining stability.

---

### 2. Motion Simulation

The system updates position and velocity using a simplified physics model:

* velocity is adjusted using the control signal
* position is updated based on velocity
* random noise is added to simulate real-world uncertainty

---

### 3. Sensor Feedback

A noisy sensor reading is generated from the true position to mimic real hardware sensors. The controller uses this noisy signal instead of the actual state.

---

### 4. Forward Kinematics

The system computes the position of a 3-link robotic arm using joint angles and basic trigonometry, producing the end-effector position.

---

### 5. Metrics and Logging

The system tracks:

* average control error
* average control signal

Logs are printed with timestamps for debugging and analysis.

---

## Run the Project

```id="brvptn"
python3 main.py
```

---

## Sample Output

```id="tfu5mc"
[12:45:10] Starting RoboControl simulation...
[12:45:10] Step 0: target=10.00, sensed=0.02, pos=0.01, vel=0.20, end_effector=(2.83, 1.34)

=== Metrics Summary ===
Average absolute error: 4.2315
Average control signal: 3.8821
[12:45:14] Simulation complete.
```

---

## Tech Stack

* Python
* Control Systems (PID)
* Linear Algebra and Kinematics
* Real-time Simulation

---

## Key Learnings

* Designing stable control loops using PID
* Handling noisy sensor feedback
* Simulating motion dynamics
* Computing forward kinematics for robotic systems
* Measuring system performance using metrics

---

## Future Improvements

* Visualization of robot motion using matplotlib
* Extension to multi-axis (2D/3D) systems
* Trajectory planning instead of static targets
* Dynamic PID tuning
* Hardware integration with real sensors

---

## Author

Ancy Patel
