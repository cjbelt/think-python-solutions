from swampy.Lumpy import Lumpy
from dicts import histogram, invert_dict

lumpy = Lumpy()
lumpy.make_reference()

hist = histogram('parrot')
inverse = invert_dict(hist)

lumpy.object_diagram()
