from vpython import *

def spheres_cube():
    t = range(0, 256, 51)

    for x in t:
        for y in t:
            for z in t:
                pos = vector(x, y, z)
                sphere_color = vector(x/255.0, y/255.0, z/255.0)
                sphere(pos=pos, radius=10, color=sphere_color)

def colors_spheres():
    from color_list import read_colors

    _, rgbs = read_colors()

    for rgb, n in rgbs:
        x = float.fromhex('0x' + rgb[1:3])
        y = float.fromhex('0x' + rgb[3:5])
        z = float.fromhex('0x' + rgb[5:])
        sphere(pos=vector(x, y, z), radius=5, color=vector(x/255.0, y/255.0, z/255.0))

if __name__ == '__main__':
    # scene.range = (256, 256, 256)
    # scene.center = vector(0, 0, 0)

    color = vector(0.1, 0.1, 0.9)
    # sphere(pos=vector(0, 0, 0), radius=5, color=color)

    # t = range(0, 256, 51)

    # for x in t:
    #     for y in t:
    #         for z in t:
    #             pos = vector(x, y, z)
    #             sphere_color = vector()
    #             sphere(pos=pos, radius=10, color=color)

    # spheres_cube()
    # print(float.fromhex('0xf0'))
    # print(hex(16))
    colors_spheres()
