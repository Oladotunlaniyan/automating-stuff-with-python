import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0

    for filename in filenames:
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
            numNonPhotoFiles += 1
            continue  
        try:
            imagePath = os.path.join(foldername, filename)
            with Image.open(imagePath) as img:
                width, height = img.size
        except:
            numNonPhotoFiles += 1
            continue
        
        if width > 500 and height > 500:
            numPhotoFiles += 1
        else:
            numNonPhotoFiles += 1

    totalFiles = numPhotoFiles + numNonPhotoFiles
    if totalFiles > 0 and numPhotoFiles / totalFiles > 0.5:
        print(os.path.abspath(foldername))
