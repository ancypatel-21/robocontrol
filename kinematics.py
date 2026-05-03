import math

def forward_kinematics(theta1, theta2, theta3, l1=1.0, l2=1.0, l3=1.0):
    x1 = l1 * math.cos(theta1)
    y1 = l1 * math.sin(theta1)

    x2 = x1 + l2 * math.cos(theta1 + theta2)
    y2 = y1 + l2 * math.sin(theta1 + theta2)

    x3 = x2 + l3 * math.cos(theta1 + theta2 + theta3)
    y3 = y2 + l3 * math.sin(theta1 + theta2 + theta3)

    return {
        "joint1": (x1, y1),
        "joint2": (x2, y2),
        "end_effector": (x3, y3)
    }