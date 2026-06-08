from swampy.TurtleWorld import *

def koch (t, length, angle = 60):
    if length < 3:
        fd(t, length)
        return

    koch(t, length/3, angle)
    lt(t, angle)
    koch(t, length/3, angle)
    rt(t, 2*angle)
    koch(t, length/3, angle)
    lt(t, angle)
    koch(t, length/3, angle)

def snowflake (t, length, angle = 60):
    for i in range(3):
        koch(t, length, angle)
        rt(t, 120)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

# koch(bob, 500)
snowflake(bob, 500, 85)
wait_for_user()
