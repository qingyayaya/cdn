import os
import glob
from PIL import Image

def genernateThumbnail(dir):
    files = glob.glob(dir + '/*.png')
    for file in files:
        img = Image.open(file)
        img.thumbnail((img.size[0] * 0.2, img.size[1] * 0.2))
        print(img.format, img.size, img.mode)
        name = os.path.join(dir, '..\cover', os.path.basename(file))
        img.save(name, 'png')
    print('done!')

if __name__ == '__main__':
    dir = os.path.abspath(os.path.dirname(__file__))
    genernateThumbnail(dir)