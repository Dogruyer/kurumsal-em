import PIL
from PIL import Image
from .models import *


def image_resizer(gorsel):
    basewidth = 1940
    img = Image.open(gorsel)
    # wpercent = (basewidth / float(img.size[0]))
    # hsize = int((float(img.size[1]) * float(wpercent)))
    # hsize = 400
    img = img.resize((40, 40), PIL.Image.ANTIALIAS)
    img.save(gorsel.url)