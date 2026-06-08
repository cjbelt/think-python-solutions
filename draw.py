def draw_rectangle(canvas, rect):
    bbox = [[rect.corner.x, rect.corner.y], [rect.corner.x + rect.width, rect.corner.y + rect.height]]
    canvas.rectangle(bbox, outline='black', width=2, fill=rect.color)

def draw_point(canvas, p):
    canvas.circle([p.x, p.y], 5, outline=None, color='black')

def draw_circle(canvas, circle):
    canvas.circle([circle.center.x, circle.center.y], circle.radius, outline=None, color=circle.color)

if __name__ == '__main__':
    from swampy.World import World
    import Point1

    world = World()
    canvas = world.ca(width=500, heigh=500, background='white')
    # bbox = [[-150, -100], [150, 100]]
    # canvas.rectangle(bbox, outline='black', width=2, fill='green4')
    # canvas.circle([-25, 0], 70, outline=None, fill='red')

    white_rect = Point1.Rectangle()
    white_rect.corner = Point1.Point()
    white_rect.corner.x = -150
    white_rect.corner.y = 0
    white_rect.width = 300
    white_rect.height = 100
    white_rect.color = 'white'
    draw_rectangle(canvas, white_rect)

    red_rect = Point1.Rectangle()
    red_rect.corner = Point1.Point()
    red_rect.corner.x = -150
    red_rect.corner.y = -100
    red_rect.width = 300
    red_rect.height = 100
    red_rect.color = 'red'
    draw_rectangle(canvas, red_rect)

    points = [[-150, -100], [-150, 100], [10, 0]]
    canvas.polygon(points, fill='dark slate blue')
    world.mainloop()
