import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def image_resizer(path, width, height):

    basewidth = width
    img = Image.open(path)
    wpercent = (basewidth / float(img.size[0]))
    # hsize = int((float(img.size[1]) * float(wpercent)))
    hsize = height
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save(path)


def make_watermark(input_image_path, output_image_path, text, pos, font):

    photo = Image.open(input_image_path)
    # make the image editable
    drawing = ImageDraw.Draw(photo)

    black = (3, 8, 12)
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", font)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(output_image_path)
