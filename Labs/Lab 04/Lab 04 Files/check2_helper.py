from PIL import Image

def make_square(image):
    width,height = image.size
    if width > height:
        return image.crop((0,0,(width-(width-height)),height))
    elif width < height:
        return image.crop((0,0,width,(height-(height-width))))
    elif width == height:
        return image