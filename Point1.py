class Point(object):
    """Represents a point in 2-D space"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner, color.
    """

class Circle(object):
    """Represents a circle.

    attributes: center, radius, color.
    """

def distance_between_points(p1, p2):
    import math
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

def move_new_rectangle(rect, dx, dy):
    import copy
    new_rect = copy.deepcopy(rect)
    new_rect.corner.x += dx
    new_rect.corner.y += dy
    return new_rect

if __name__ == '__main__':
    blank = Point()
    black = Point()
    blank.x = 3.0
    blank.y = 4.0
    black.x = 7.0
    black.y = 8.0
    # print(distance_between_points(blank, black))

    rect = Rectangle()
    rect.width = 50.0
    rect.height = 100.0
    rect.corner = Point()
    rect.corner.x = 0.0
    rect.corner.y = 0.0
    # print(rect.corner.x, rect.corner.y)
    move_rectangle(rect, 3, 4)
    # print(rect.corner.x, rect.corner.y)
    new_rect = move_new_rectangle(rect, 5, 5)
    # print(new_rect.corner.x, new_rect.corner.y)
    # print(rect.corner.x, rect.corner.y)
    p = Point(3, 4)
    print(p)
