import PIL
from PIL import Image

def image_resizer(path, width, height):
    basewidth = width
    img = Image.open(path)
    wpercent = (basewidth / float(img.size[0]))
    # hsize = int((float(img.size[1]) * float(wpercent)))
    hsize = height
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save(path)

