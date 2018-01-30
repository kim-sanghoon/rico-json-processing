import json, os, csv
from settings import *
from element import element

app_info_iter = csv.reader(APP_METADATA)
app_info = {i[0]: i[0:3] for i in app_info_iter}

for FILE_NAME in FILE_LIST:
    print("Do: " + os.path.join(os.path.curdir, 'json', 'raw', FILE_NAME))
    FILE = open(os.path.join(os.path.curdir, 'json', 'raw', FILE_NAME))

    data = json.load(FILE)
    parsed_data = {}

    try:
        parsed_data['app'] = {'package_name': data['activity_name'].split('/')[0],
                          'store_name': app_info[data['activity_name'].split('/')[0]][1],
                          'category': app_info[data['activity_name'].split('/')[0]][2]}
    except:
        print("Metadata error: " + FILE_NAME + "  :  " + data['activity_name'].split('/')[0])
    parsed_data['activity_name'] = data['activity_name'].split('/')[1].split('.')[-1]
    parsed_data['keyboard'] = data['is_keyboard_deployed']
    try:
        parsed_data['hierarchy'] = element(data['activity']['root']).to_dict()
    except:
        print("Parsing error: " + FILE_NAME + "  :  " + data['activity_name'].split('/')[0])

    output = open(os.path.join(os.path.curdir, 'json', 'refined', FILE_NAME), mode='w')
    json.dump(parsed_data, output, indent=2, sort_keys=True)
    print("Done: " + os.path.join(os.path.curdir, 'json', 'refined', FILE_NAME))
