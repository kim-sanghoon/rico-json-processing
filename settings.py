import os

# Information about json files
FILE_LIST = [name for name in os.listdir(os.path.join(os.path.curdir, 'json', 'raw'))]
# FILE_LIST = ['39429.json']

# Information about layout images
SCREEN_SIZE = (1440, 2560) # Do NOT change
ELEMENT_COLOR = {'EditText': 'orange',
                 'edit': 'orange',
                 'Text': 'blue',
                 'text': 'blue',
                 'Button': 'green',
                 #'button': 'green',
                 'Image': 'red',
                 'image': 'red',
                 'icon': 'red',
                 'CheckBox': 'pink',
                 'checkbox': 'pink',
                 'WebView': 'purple',
                 'AdView': 'brown',
                 'NumberPicker': 'gray',
                 }

FULL_NAME_COLOR = {'google.maps.api.android': 'skyblue', # Google Maps API
                   'google.android.gms.ads': 'brown', # Google Ads
                   'mopub.mobileads': 'brown', # Mopub Ads
                   }


# Others
APP_METADATA = open(os.path.join(os.path.curdir, 'metadata', 'app_details.csv'))
