import json
import collections
from collections import OrderedDict

input_file = open ('poi_data.json')
json_array = json.load(input_file, object_pairs_hook=OrderedDict)

for item in json_array:
    #poi_list = []

    #poi_details = collections.OrderedDict()
    #poi_details['id'] = item['id']
    #poi_details['pref_source'] = item['pref_source']
    #poi_details['pref_name'] = item['pref_name']
    #poi_details['address'] = item['address']
    #poi_details['pref_geocode'] = item['pref_geocode']
    #poi_details['is_poi_icon_suppressed'] = item['is_poi_icon_suppressed']
    #poi_details['timezone'] = item['timezone']
    #poi_details['native_locale'] = item['native_locale']
    #poi_details['vector_poi_display'] = item['vector_poi_display']
    #poi_list.append(poi_details)

    filename = item['pref_name'] + '.json'

   # temp = str(item['address']['postCode'])

    #item['address']['postCode'] = temp

    item['address']['postCode'] = str(item['address']['postCode'])
    
#    with open(filename, 'w') as fp:
 #       json.dump(poi_list, fp, indent=3)

    with open(filename, 'w') as fp:
        json.dump(item, fp, indent=3)


