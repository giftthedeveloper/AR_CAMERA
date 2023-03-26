#thank you Jesus

#Let's set up a small unregular api that can fetch our filter image as well as their annotations and properties(alpha and morph)
#images are usually in RGB but some images have 'alpha' which controls the transparency 
filters_API = {
    'rainbowmouthfilter':
        [{'png_path': "filters_folder/rainbowmouthfilter.png",
          'annotation_file': "filters_folder/rainbowmouthfilter.csv",
          'morph': True, 'animated': False, 'has_alpha': True}],
    'nosemask_ears_filter':
        [{'path': "filters_folder/nosemask_ears_filter.png",
          'annotation_file': "filters_folder/nosemask_ears_filter.csv",
          'morph': True, 'animated': False, 'has_alpha': True}],
    'fowerfilter':
        [{'path': "filters_folder/fowerfilter.png",
          'annotation_file': "filters_folder/fowerfilter.csv",
          'morph': False, 'animated': False, 'has_alpha': True}],
    'moustache_filter':
        [{'path': "filters_folder/moustache_filter.png",
          'annotation_file': "filters_folder/moustache_filter.csv",
          'morph': False, 'animated': False, 'has_alpha': True}],
    'heartfilter':
        [{'path': "filters_folder/heartfilter.png",
          'annotation_file': "filter_folder/heartfilter.csv",
          'morph': True, 'animated': False, 'has_alpha': True}],
    'glasses_filter':
        [{'path': "filters_folder/glasses_filter.png",
          'annotation_file': "filters_folder/glasses_filter.csv",
          'morph': False, 'animated': False, 'has_alpha': True}],
    'dog_ears_nose_filter':
        [{'path': "filters_folder/dog_ears_nose_filter.png",
          'annotation_file': "filters_folder/dog_ears_nose_filter.csv",
          'morph': False, 'animated': False, 'has_alpha': True}],
    'cutebunny_filter':
        [{'path': "filters_folder/cutebunny_filter.png",
          'annotation_file': "filters_folder/cutebunny_filter.csv",
          'morph': False, 'animated': False, 'has_alpha': True}],
    'cityfilter':
        [{'path': "filters_folder/cityfilter.png",
          'annotation_file': "filters_folder/cityfilter.csv",
          'morph': False, 'animated': False, 'has_alpha': True}],
    'butterfly_filter':
        [{'path': "filters_folder/butterfly_filter.png",
          'annotation_file': "filters_folder/butterfly_filter.csv",
          'morph': False, 'animated': False, 'has_alpha': True}],
    'bulgyeyes_filter':
        [{'path': "filters_folder/bulgyeyes_filter.png",
          'annotation_file': "filters_folder/bulgyeyes_filter.csv",
          'morph': False, 'animated': False, 'has_alpha': True}],
          #remains angel_filter and blueflower_filter.png
    
}


