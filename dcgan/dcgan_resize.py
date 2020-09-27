import os
import glob
from PIL import Image

files = glob.glob('icon/*.png')
a = 0
for f in files:
    a += 1
    img = Image.open(f)
    # 128*128にリサイズ
    img_resize = img.resize((128, 128))
    ftitle, fext = os.path.splitext(f)
    img_resize.save('icon_resize/' + str(a) + fext)
