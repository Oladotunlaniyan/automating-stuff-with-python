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


#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

# import os
# from PIL import Image

#      # Check if image needs to be resized.
# if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
# # Calculate the new width and height to resize to.
#     if width > height:
#             height = int((SQUARE_FIT_SIZE / width) * height)
#             width = SQUARE_FIT_SIZE
#     else:
#         width = int((SQUARE_FIT_SIZE / height) * width)
#         height = SQUARE_FIT_SIZE
# # Resize the image.
#         print('Resizing %s...' % (filename))
#         im = im.resize((width, height))