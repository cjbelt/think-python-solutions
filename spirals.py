from swampy.TurtleWorld import *
from mypolygon import arc

def spiral(t, n, r):
    r1 = 5
    for i in range(2*n):
        arc(t, r1, 180)
        r1 += r

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
spiral(bob, 5, 15)
wait_for_user()
