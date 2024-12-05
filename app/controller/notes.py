import json

def saveData(data):
    print("fetching data")
    with open(f"app/data/courses/{data[0]}/note.json", 'r') as file: 
        fetch_data = json.load(file)
    
    print("updating data")
    fetch_data[data[1]]["title"] = data[2]
    fetch_data[data[1]]["deskripsi"] = data[3]
    fetch_data[data[1]]["created_at"] = data[4]
    
    with open(f"app/data/courses/{data[0]}/note.json", "w") as file: 
        json.dump(fetch_data, file, indent=4)
    print("data updated successfully!")