import json
import shutil

from PySide6.QtWidgets import QMessageBox

def saveData(data):
    print("fetching data")
    with open(f"app/data/courses/{data[0]}/assignment.json", 'r') as file: 
        fetch_data = json.load(file)
    
    print("updating data")
    fetch_data[data[1]] = {}
    fetch_data[data[1]]["title"] = data[2]
    fetch_data[data[1]]["deskripsi"] = data[3]
    fetch_data[data[1]]["deadline"] = data[4]
    fetch_data[data[1]]["isFinished"] = True if data[5] == "Complete" else False
    
    with open(f"app/data/courses/{data[0]}/assignment.json", "w") as file: 
        json.dump(fetch_data, file, indent=4)
    print("data updated successfully!")
    
def deleteTodo(course_id, todo_id): 
    path = f"app/data/courses/{course_id}/assignment.json"
    
    with open(path, "r") as file: 
        todo_data = json.load(file)

    del todo_data[todo_id]
    
    with open(path, "w") as file: 
        json.dump(todo_data, file, indent=4)
        
def saveIsFinished(course_id, todo_id, isFinished): 
    path = f"app/data/courses/{course_id}/assignment.json"
    with open(path, 'r') as file: 
        todo_data = json.load(file)
    
    todo_data[todo_id]['isFinished'] = isFinished
    
    with open(path, 'w') as file: 
        json.dump(todo_data, file, indent=4)