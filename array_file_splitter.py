import json
import collections
from collections import OrderedDict

input_file = open ('poi_data.json')
json_array = json.load(input_file, object_pairs_hook=OrderedDict)

for item in json_array:

    filename = item['pref_name'] + '.json'

    item['address']['postCode'] = str(item['address']['postCode'])

    with open(filename, 'w') as fp:
        json.dump(item, fp, indent=3)


