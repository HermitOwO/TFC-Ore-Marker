import os
import zipfile
import modify

version = '2.1'

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file), path))

with zipfile.ZipFile('./releases/TFC Ore Marker v' + version + '.zip', mode='w') as zf:
    zf.write('credits.txt')
    zipdir('base', zf)
    zipdir('modified_files', zf)
