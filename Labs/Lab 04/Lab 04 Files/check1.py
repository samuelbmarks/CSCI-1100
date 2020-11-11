from PIL import Image

im = Image.new('RGB',(512,512),'white')

im1 = Image.open('im.jpg')
im1 = im1.resize((256,256))
im.paste(im1, (0,0))

im2 = Image.open('ca.jpg')
im2 = im2.resize((256,256))
im.paste(im2, (0,256))

im3 = Image.open('hk.jpg')
im3 = im3.resize((256,256))
im.paste(im3, (256,0))

im4 = Image.open('bw.jpg')
im4 = im4.resize((256,256))
im.paste(im4, (256,256))

im.show()