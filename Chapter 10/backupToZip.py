import zipfile, os

def backupToZip(folder):

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder)

        if not os.path.exists(zipFilename):
            break 
        number = number + 1 

        print(f'Creating {zipFilename}...')
        backupZip = zipfile.ZipFile(zipFilename, 'w')

        print('Done.') 
    
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')

        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder) + '-'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
        print('Done.')