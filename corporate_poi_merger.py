import json 
import os 

'''
Merge 2 JSON files with information relevant to POI JSON files in folder,
merge them and output files
'''

def update_id(corporate_data, old_id):
  base_id = 30000000000000
  new_id = base_id + old_id
  return(new_id)

def pref_source(ryan_data, new_id):
  for i in ryan_data:
    if i["id"] == new_id:
      #print(i["apref_source"])
      return(i["pref_source"])

def address(ryan_data, new_id):
  for i in ryan_data:
    if i["id"] == new_id:
      #print(i["address"])
      return(i["address"])

def geo_code(ryan_data, new_id):
  for i in ryan_data:
    if i["id"] == new_id:
      #print(i["pref_geocode"])
      return(i["pref_geocode"]["center"])

def address_geocode_accuracy(ryan_data, new_id):
  for i in ryan_data:
    if i["id"] == new_id:
      #print(i["pref_geocode"])
      return(i["pref_geocode"]["address_geocode_accuracy"])

def localized_names(data):
  for i in data:
    return(data["localized_names"])

def is_poi_icon_supressed(ryan_data, new_id):
  for i in ryan_data:
    if i["id"] == new_id:
      #print(i["is_poi_icon_suppressed"])
      return(i["is_poi_icon_suppressed"])

def timezone(ryan_data, new_id):
  for i in ryan_data:
    if i["id"] == new_id:
      #print(i["timezone"]["identifier"])
      return(i["timezone"]["identifier"])

def poi_type(ryan_data, new_id):
  for i in ryan_data:
    if i["id"] == new_id:
      #print(i["vector_poi_display"]["poi_type"])
      return(i["vector_poi_display"]["poi_type"])

def min_zoom(ryan_data, new_id):
  for i in ryan_data:
    if i["id"] == new_id:
      #print(i["vector_poi_display"]["min_zoom"])
      return(i["vector_poi_display"]["min_zoom"])

def max_zoom(ryan_data, new_id):
  for i in ryan_data:
    if i["id"] == new_id:
      #print(i["vector_poi_display"]["min_zoom"])
      return(i["vector_poi_display"]["max_zoom"])

def main():
  with open("corporate_id.json", "r") as opened_json:
    poi_raw = opened_json.read()
    corporate_data = json.loads(poi_raw)
  
  with open("ryan_corporate.json", "r") as opened_json:
    ryan_raw = opened_json.read()
    ryan_data = json.loads(ryan_raw)
    
  from os import listdir
  from os.path import isfile, join 
  onlyfiles = [f for f in listdir("custom_poi_data") if isfile(join("custom_poi_data", f))]
  #print(onlyfiles)

  for i in corporate_data:

    old_id = i["ID"]
    corp_name = i["Name"]
    new_id = update_id(corporate_data, old_id)

    if corp_name + ".json" in onlyfiles: 

      source_folder = "custom_poi_data/"
    
      with open(source_folder + corp_name + ".json", "r") as opened_json:
        data_raw = opened_json.read()
        data = json.loads(data_raw)
      #print(data)

      main_export = {"id": new_id, "pref_source": pref_source(ryan_data, new_id), 
      "pref_name": corp_name, "address":address(ryan_data, new_id), 
      "pref_geocode": {"center": geo_code(ryan_data, new_id), 
      "address_geocode_accuracy": address_geocode_accuracy(ryan_data, new_id)}, 
      "localized_names": localized_names(data), "is_poi_icon_supressed": is_poi_icon_supressed(ryan_data, new_id), "timezone": {"identifier": timezone(ryan_data, new_id)}, "vector_poi_display":{"poi_type": poi_type(ryan_data, new_id), "min_zoom": min_zoom(ryan_data, new_id), "max_zoom": max_zoom(ryan_data, new_id)}}
      #print(main_export)

      file_name = i["Name"]+".json"
      x = json.dumps(main_export, indent=3, sort_keys=True)
      #print(x)
      f = open(i["Name"]+".json", "w")
      f.write(x)
      f.close() 
   
    else:

      main_export = {"id": new_id, "pref_source": pref_source(ryan_data, new_id), 
      "pref_name": corp_name, "address":address(ryan_data, new_id), 
      "pref_geocode": {"center": geo_code(ryan_data, new_id), 
      "address_geocode_accuracy": address_geocode_accuracy(ryan_data, new_id)}, 
      "timezone": {"identifier": timezone(ryan_data, new_id)}, 
      "vector_poi_display":{"poi_type": poi_type(ryan_data, new_id), 
      "min_zoom": min_zoom(ryan_data, new_id), 
      "max_zoom": max_zoom(ryan_data, new_id)}}
      #print(main_export)

      file_name = i["Name"]+".json"
      x = json.dumps(main_export, indent=3, sort_keys=True)
      #print(x)
      f = open(i["Name"]+".json", "w")
      f.write(x)
      f.close() 



main()
