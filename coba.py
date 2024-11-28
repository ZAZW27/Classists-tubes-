import os
import json

course_path = "courses"

folders = {}
for item in os.listdir(course_path): 
    item_path = os.path.join(course_path, item)  
    # check if it exists and a directory
    if not os.path.isdir(item_path): continue
    
    id_json_path = os.path.join(item_path, "id.json")
    if not os.path.isfile(id_json_path): continue
    
    with open(id_json_path, 'r') as json_file:
        content = json.load(json_file)
        folders[item] = content


print(folders)
