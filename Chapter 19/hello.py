# from PIL import Image

# catIm = Image.open('zophie.png')
# catIm.rotate(90).save('rotated90.png')
# catIm.rotate(180).save('rotated180.png')
# catIm.rotate(270).save('rotated270.png')


# catIm.rotate(6).save('rotated6.png')
# catIm.rotate(6, expand=True).save('rotated6_expanded.png')


# from PIL import Image
 
# im = Image.new('RGBA', (100, 100))
# im.getpixel((0, 0))
 
# for x in range(100):
#            for y in range(50):
#            im.putpixel((x, y), (210, 210, 210))

# from PIL import ImageColor
# for x in range(100):
#          for y in range(50, 100):
#             im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
#    im.getpixel((0, 0))
#     im.getpixel((0, 50))
#    (169, 169, 169, 255)
# im.save('putPixel.png')

# from PIL import Image, ImageDraw, ImageFont
# import os

# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)
# draw.text((20, 150), 'Hello', fill='purple')
# fontsFolder = 'FONT_FOLDER' # e.g. ‘/Library/Fonts'
# arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
# draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
# im.save('text.png')


