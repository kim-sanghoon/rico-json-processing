from settings import *
from PIL import Image

for FILE_NAME in FILE_LIST:
    canvas = Image.new("RGBA", (2880, 2560), 'white')
    origin = Image.open('original_picture/' + FILE_NAME.split('.')[0] + '.jpg')
    layout = Image.open('layout/' + FILE_NAME + '_out.png')

    origin = origin.resize((1440, 2560), Image.ANTIALIAS)

    canvas.paste(origin, (0, 0))
    canvas.paste(layout, (1440, 0))

    canvas.save('./comparison/' + FILE_NAME + '_comp.png', 'PNG')
    print('./comparison/' + FILE_NAME + '_comp.png')