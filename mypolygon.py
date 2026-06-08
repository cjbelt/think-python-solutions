from swampy.TurtleWorld import *
from math import pi, sin

# world = TurtleWorld()
# bob = Turtle()

def polyline(t, n, length, angle):
    # print("polyline:")
    # print("t: ", t)
    # print("n: ", n)
    # print("length: ", length)
    # print("angle: ", angle)
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n):
    """draws a polygon with n sides with a length value; use the polyline function to do it"""
    polyline(t, n, length, 360/n)

def circle(t, r):
    """turtle t draws a circle with radius r; uses the arc function"""
    # print("circle:")
    # print("t: ", t)
    # print("r: ", r)
    arc(t, r, 360)

def arc(t, r, angle):
    """turtle t draws an arc with radius r and an angle value"""
    # print("arc:")
    # print("t: ", t)
    # print("r: ", r)
    # print("angle: ", angle)
    arc_length = 2 * pi * r * angle / 360
    # print("arc_length: ", arc_length)
    n = int(arc_length / 3) + 1
    # print("n: ", n)
    step_length = arc_length / n
    # print("step_length: ", step_length)
    step_angle = float(angle) / n
    # print("step_angle: ", step_angle)
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def flower(t, angle, r, n):
    """draws a flower using the arc function
        t: turtle
        r: radius
        n: number of petals"""

    step_angle = 360 / n
    for i in range(n):
        for i in range(2):
            arc(t, r, angle)
            lt(t, 180-angle)
        rt(t, step_angle)

def pie(t, n, l):

    polygon(t, l, n)
    angle = 360 / n
    lt(t, (180 - angle) / 2)
    legs = l * sin((180 - angle) / 2 * pi/180) / sin(angle * pi/180)
    for i in range(n - 1):
        polyline(t, 2, legs, 180 - angle)
        rt(t, -360/n)



# square(bob, 600)
# polygon(bob, 100, 20)
# bob.delay = 0.1
# circle(bob, 50)
# arc(bob, 50, 360)
# flower(bob, 20, 200, 15)
# pie(bob, 10, 100)
# wait_for_user()
