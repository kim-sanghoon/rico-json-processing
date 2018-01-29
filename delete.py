#!/usr/local/bin/python3
import json, sys, os

FILES = sys.argv[1:]

for FILE_NUM in FILES:
    try:
        FILE_JSON = json.load(open(os.path.join(os.path.curdir, 'json', 'refined', FILE_NUM + '.json')))
    except FileNotFoundError:
        print("File not found: %s" % os.path.join(os.path.curdir, 'json', 'refined', FILE_NUM + '.json'))
        continue

    print("File you want to delete is:")
    print("  - %s" % os.path.join(os.path.curdir, 'json', 'refined', FILE_NUM + '.json'))
    print("  - %s" % os.path.join(os.path.curdir, 'json', 'raw', FILE_NUM + '.json'))
    print("  - %s" % os.path.join(os.path.curdir, 'layout', FILE_NUM + '.json_out.png'))
    print("  - %s" % os.path.join(os.path.curdir, 'comparison', FILE_NUM + '.json_comp.png'))
    print("App info: ")
    print("  - Package name: %s" % FILE_JSON['app']['package_name'])
    print("  - Store name  : %s" % FILE_JSON['app']['store_name'])
    print("  - Category    : %s" % FILE_JSON['app']['category'])
    print("\nPlease check the information before you delete.\nDo you really want to delete this info? (Y/N) ")

    while True:
        n = input()
        if n == 'Y' or n == 'y':
            os.remove(os.path.join(os.path.curdir, 'json', 'refined', FILE_NUM + '.json'))
            os.remove(os.path.join(os.path.curdir, 'json', 'raw', FILE_NUM + '.json'))
            os.remove(os.path.join(os.path.curdir, 'layout', FILE_NUM + '.json_out.png'))
            os.remove(os.path.join(os.path.curdir, 'comparison', FILE_NUM + '.json_comp.png'))
            print("Delete complete.")
            break
        elif n == 'N' or n == 'n':
            print("Deletion aborted.")
            break
        else:
            print("Please answer with Y/N. ")