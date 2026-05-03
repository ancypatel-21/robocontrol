import random

def update_position(position, velocity, control_signal, dt):
    noise = random.uniform(-0.05, 0.05)

    velocity += control_signal * dt
    position += velocity * dt + noise

    return position, velocity

def read_sensor(position):
    sensor_noise = random.uniform(-0.1, 0.1)
    return position + sensor_noise