import os

# Information about json files
FILE_LIST = [name for name in os.listdir(os.path.join(os.path.curdir, 'json', 'raw'))]
# FILE_LIST = ['1001.json']

# Information about layout images
SCREEN_SIZE = (1440, 2560) # Do NOT change
ELEMENT_COLOR = {'EditText': 'orange',
                 #'edit': 'orange',
                 'CheckedTextView': 'lime',
                 'Text': 'blue',
                 'text': 'blue',
                 'TextView': 'blue',
                 'RadioButton': 'lime',
                 'Button': 'green',
                 #'button': 'green',
                 'Image': 'red',
                 'image': 'red',
                 'icon': 'red',
                 'CheckBox': 'pink',
                 'checkbox': 'pink',
                 'Checkbox': 'pink',
                 'checkBox': 'pink',
                 'WebView': 'purple',
                 'AdView': 'brown',
                 'Banner': 'brown',
                 'NumberPicker': 'gray',
                 'SpeedometerGauge': 'red',
                 'Gauge': 'red',
                 'ArcProgress': 'red',
                 'SimpleDraweeView': 'red',
                 'MonthView': 'yellow',
                 'AccessibleDateAnimator': 'yellow',
                 'MapView': 'skyblue',
                 'VideoView': 'navy',
                 'Chart': 'red',
                 'SeekBar': 'gold',
                 'PictureView': 'red',
                 'Picture': 'red',
                 'ActionMenuItemView': 'green',
                 'ImageSurfaceView': 'red',
                 'ImageView': 'red',
                 'SurfaceView': 'red',
                 'Graph': 'red',
                 'RadialPicker': 'ivory',
                 'time_picker': 'ivory',
                 'TimePicker': 'ivory',
                 'ProgressBar': 'magenta',
                 }

ELEMENT_EXCEPT = [#'feeditem',
                  #'edit_profile',
                  #'credit',
                  'background_holder',
                  'background_image',
                  ]

FULL_NAME_COLOR = {'google.maps.api.android': 'skyblue', # Google Maps API
                   'google.android.gms.ads': 'brown', # Google Ads
                   'mopub.mobileads': 'brown', # Mopub Ads
                   'maps.D': 'skyblue', # Google Maps
                   'maps.ad.ay$a': 'skyblue', # Google Maps
                   'drumpadmachine.ui.Pad': 'red', # Game image element
                   }


# Others
APP_METADATA = open(os.path.join(os.path.curdir, 'metadata', 'app_details.csv'))
