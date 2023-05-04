# import things
from svg import Parser, Rasterizer, SVG
from PIL import Image  # for saving rasterized image
# Parse from a file
svg = Parser.parse_file('my_cool_img.svg')
print('Image is {} by {}.'.format(svg.width, svg.height))
rast = Rasterizer()
buff = rast.rasterize(svg, svg.width, svg.height)
im = Image.frombytes('RGBA', svg.width, svg.height, buff)
im.save('my_cool_img.png')  # save the converted image!