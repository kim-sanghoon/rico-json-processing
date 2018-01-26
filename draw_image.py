import json, os
from settings import *
from PIL import Image

def draw(hier, img):
    #
    # Some non-standard layout/views, they don't have standard name.
    # Therefore, we have to guess the label using their name and resource-id.
    #
    checked = False
    for element_name in ELEMENT_COLOR.keys():
        if hier['name'].count(element_name) > 0:
            hier['name'] = element_name
            checked = True
            break

    if not checked and hier['resource_id'] is not None:
        for element_name in ELEMENT_COLOR.keys():
            if hier['resource_id'].count(element_name) > 0:
                hier['name'] = element_name
                break

    # Coloring
    if hier['name'] in ELEMENT_COLOR.keys():
        b = hier['bounds']
        try:
            block = Image.new('RGBA', (b[2] - b[0], b[3] - b[1]), ELEMENT_COLOR[hier['name']])
            img.paste(block, (b[0], b[1]))
        except ValueError:
            pass

    # Recursion
    if hier['children'] is not None:
        for child in hier['children']:
            draw(child, img)


for FILE_NAME in FILE_LIST:
    with open(os.path.join(os.path.curdir, 'json', 'refined', FILE_NAME), mode='r') as file:
        data = json.load(file)

    img = Image.new('RGBA', SCREEN_SIZE, 'white')
    draw(data['hierarchy'], img)

    img.save(os.path.join(os.path.curdir, 'layout', FILE_NAME + '_out.png'), 'PNG')
    print(os.path.join(os.path.curdir, 'layout', FILE_NAME + '_out.png'))


