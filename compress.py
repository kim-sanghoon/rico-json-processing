from multiprocessing.dummy import Pool
from PIL import Image
from settings import *
import os


def work(file_name):
    try:
        origin = Image.open(os.path.join(os.path.curdir, 'comparison', file_name + '_comp.png'))
    except FileNotFoundError:
        print("File not found: " + file_name + "_comp.png")
        return

    compressed_screen_size = (int(2880 / compress_ratio), int(2560 // compress_ratio))

    new = origin.resize(compressed_screen_size, Image.ANTIALIAS)
    new.save(os.path.join(os.path.curdir, 'compressed_comp', file_name + '_' + str(compress_ratio) + 'compressed.png'), 'PNG')
    print(os.path.join(os.path.curdir, 'compressed_comp', file_name + '_' + str(compress_ratio) + 'compressed.png'))


try:
    compress_ratio = float(input("Please input compression ratio: "))
except:
    print("Wrong input. Default value(2.0) will be used.")
    compress_ratio = 2.0

threads = Pool(40)
threads.map(work, FILE_LIST)
threads.close()
threads.join()
