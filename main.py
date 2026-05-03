import time
import math
from pid import PIDController
from simulation import update_position, read_sensor
from logger import log
from metrics import Metrics
from kinematics import forward_kinematics

target_position = 10.0
position = 0.0
velocity = 0.0

pid = PIDController(kp=2.0, ki=0.1, kd=0.5)
metrics = Metrics()

dt = 0.02
steps = 200

theta1 = 0.2
theta2 = 0.4
theta3 = 0.3

log("Starting RoboControl simulation...")

for step in range(steps):
    sensed_position = read_sensor(position)
    error = target_position - sensed_position

    control = pid.compute(target_position, sensed_position, dt)
    position, velocity = update_position(position, velocity, control, dt)

    arm_state = forward_kinematics(theta1, theta2, theta3)

    metrics.record(error, control)
    log(
        f"Step {step}: target={target_position:.2f}, sensed={sensed_position:.2f}, "
        f"pos={position:.2f}, vel={velocity:.2f}, end_effector={arm_state['end_effector']}"
    )

    theta1 += 0.001 * control
    theta2 += 0.0005 * control
    theta3 += 0.0003 * control

    time.sleep(dt)

metrics.summary()
log("Simulation complete.")