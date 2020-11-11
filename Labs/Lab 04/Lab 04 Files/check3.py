import wikimedia
import check2_helper
from PIL import Image

x = input("Search image: ")
images = wikimedia.find_images(x,4)

if len(images)==4:
    im = Image.new('RGB', (512,512), 'white')
    im1 = images[0]
    im1 = check2_helper.make_square(im1)
    im2 = images[1]
    im2 = check2_helper.make_square(im2)
    im3 = images[2]
    im3 = check2_helper.make_square(im3)
    im4 = images[3]
    im4 = check2_helper.make_square(im4)
    im1 = im1.resize((256,256))
    im2 = im2.resize((256,256))
    im3 = im3.resize((256,256))
    im4 = im4.resize((256,256))
    im.paste(im1,(0,0))
    im.paste(im2,(0,256))
    im.paste(im3,(256,0))
    im.paste(im4,(256,256))
    im.show()
else:
    print("Could not find a sufficient number of images.")