from settings import *
from PIL import Image
import os
from multiprocessing.dummy import Pool

def work(FILE_NAME):
# for FILE_NAME in FILE_LIST:
    canvas = Image.new("RGBA", (2880, 2560), 'white')
    try:
        origin = Image.open(os.path.join(os.path.curdir, 'original_picture', FILE_NAME.split('.')[0] + '.jpg'))
    except:
        err = open('comp_err_log.txt', 'a')
        err.write(FILE_NAME + ": Error occurred while opening original pic.\n")
        print(FILE_NAME + ": Error occurred while opening original pic.")
        err.close()
        origin = Image.new("RGBA", (1440, 2560), "black")
        pass
    try:
        layout = Image.open(os.path.join(os.path.curdir, 'layout', FILE_NAME + '_out.png'))
    except:
        err = open('comp_err_log.txt', 'a')
        err.write(FILE_NAME + ": Error occurred while opening layout pic.\n")
        err.close()
        print(FILE_NAME + ": Error occurred while opening layout pic.")
        layout = Image.new("RGBA", (1440, 2560), "black")
        pass
    # origin = Image.open('original_picture/' + FILE_NAME.split('.')[0] + '.jpg')
    # layout = Image.open('layout/' + FILE_NAME + '_out.png')

    origin = origin.resize((1440, 2560), Image.ANTIALIAS)

    canvas.paste(origin, (0, 0))
    canvas.paste(layout, (1440, 0))

    canvas.save(os.path.join(os.path.curdir, 'comparison', FILE_NAME + '_comp.png'), 'PNG')
    print(os.path.join(os.path.curdir, 'comparison', FILE_NAME + '_comp.png'))
    # canvas.save('./comparison/' + FILE_NAME + '_comp.png', 'PNG')
    # print('./comparison/' + FILE_NAME + '_comp.png')


threads = Pool(40)
threads.map(work, FILE_LIST)
threads.close()
threads.join()
