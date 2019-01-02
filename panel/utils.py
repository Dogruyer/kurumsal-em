from PIL import Image
from resizeimage import resizeimage
import pdb
from .models import *

def resim_bicimlendir(resim, width, height):
    pdb.set_trace()
    fd_img = open(resim, 'r')
    img = Image.open(fd_img)
    img = resizeimage.resize_contain(img, [width, height])
    getir = Slider.objects.get(slider_image.path = resim)
    img.save(resim, img.format)
    fd_img.close()

