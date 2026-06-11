from Wobbler import *
import math
import random

class Tagger(Wobbler):
    """Turtles playing tag!"""

    def __init__(self, world, speed, clumsiness, color, it=False):
        Wobbler.__init__(self, world, speed, clumsiness, color)

        self.it = it
        self.sulking = 0

    def steer(self):
        # point to the origin
        # self.heading = at + 180

        if self.sulking > 0:
            self.sulking -= 1

            if self.sulking == 0:
                self.speed = self.old_speed

            return

        dist, t = self.find_nearest()

        if self.it:
            self.point_toward(t.x, t.y)

            if self.is_near(t):
                self.tag_it(t)

        if not self.it:
            if self.is_near(t, 15):
                self.point_away(t.x, t.y)
        # else:
        #     self.point_away(t.x, t.y)

        if self.calc_distance() > 200:
            self.point_toward()

    def calc_distance(self, x=0, y=0):
        dx = self.x - x
        dy = self.y - y

        return math.sqrt(dx**2 + dy**2)

    def find_nearest(self):
        t = []

        for turtle in self.world.animals:
            if turtle != self:
                t.append((self.calc_distance(turtle.x, turtle.y), turtle))

        t.sort()

        try:
            return t[0]
        except KeyError:
            return None

    def point_toward(self, x=0, y=0):
        dx = self.x - x
        dy = self.y - y

        self.heading = math.degrees(math.atan2(dy, dx)) + 180

    def point_away(self, x=0, y=0):
        self.point_toward(x, y)
        self.heading -= 180

    def turn_it(self):
        self.it = True
        self.old_color = self.color
        self.old_speed = self.speed
        self.color = "red"
        self.speed = 0
        self.sulking = 200
        self.redraw()

    def turn_off_it(self):
        self.it = False
        self.color = self.old_color
        self.redraw()

    def tag_it(self, other):
        self.turn_off_it()
        other.turn_it()

    def is_near(self, other, d=10):
        if self.calc_distance(other.x, other.y) < d:
            return True

        return False

if __name__ == '__main__':
    world = make_world(Tagger)
    random.choice(world.animals).turn_it()
    world.mainloop()
