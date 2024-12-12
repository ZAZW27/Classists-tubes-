import json
import shutil

from PySide6.QtWidgets import QMessageBox

def saveData(data):
    print("fetching data")
    with open(f"app/data/courses/{data[0]}/note.json", 'r') as file: 
        fetch_data = json.load(file)
    
    print("updating data")
    fetch_data[data[1]] = {}
    fetch_data[data[1]]["title"] = data[2]
    fetch_data[data[1]]["deskripsi"] = data[3]
    fetch_data[data[1]]["created_at"] = data[4]
    fetch_data[data[1]]["created_at"] = data[4]
    
    with open(f"app/data/courses/{data[0]}/note.json", "w") as file: 
        json.dump(fetch_data, file, indent=4)
    print("data updated successfully!")
    
def deleteNote(course_id, note_id): 
    path = f"app/data/courses/{course_id}/note.json"
    
    with open(path, "r") as file: 
        note_data = json.load(file)

    del note_data[note_id]
    
    with open(path, "w") as file: 
        json.dump(note_data, file, indent=4)
    