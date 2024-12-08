from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvg import *

import json
import os

def edit_course_form(main_window, course_id): 
    with open(f"app/data/courses/{course_id}/id.json", "r") as file: 
        data = json.load(file)
    # Create the dialog
    modal = QDialog(main_window)
    modal.setStyleSheet("color: rgb(0, 0, 0);")
    modal.setWindowTitle("Choose a Course Details")
    modal.setGeometry(200, 200, 400, 400)

    # Main Layout
    main_layout = QVBoxLayout()

    # Instructions
    instructions = QLabel("Fill in the course details:")
    instructions.setAlignment(Qt.AlignCenter)
    main_layout.addWidget(instructions)

    # Create Form Layout
    form_layout = QFormLayout()

    # Course Name Input
    course_name_input = QLineEdit()
    course_name_input.setText(data.get("title", "Couldn't fetch title"))
    form_layout.addRow("Course Name:", course_name_input)

    # Hari (Day) Dropdown
    hari_list = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu"]
    get_current_day = hari_list.index(data.get("hari", 'senin'))
    
    hari_select = QComboBox()
    hari_select.addItems(hari_list)
    hari_select.setCurrentIndex(get_current_day)
    form_layout.addRow("Hari:", hari_select)

    # Sesi (Session) Dropdown
    sesi_list = ["1", "2", "3", "4"]
    get_current_sesi = sesi_list.index(data.get("sesi", "1"))
    
    sesi_select = QComboBox()
    sesi_select.addItems(sesi_list)
    sesi_select.setCurrentIndex(get_current_sesi)
    form_layout.addRow("Sesi:", sesi_select)

    # Gedung (Building) Dropdown
    gedung_list = ["A", "B", "E", "F", "G"]
    get_current_gedung = gedung_list.index(data['lokasi'][0])
    
    gedung_select = QComboBox()
    gedung_select.addItems(gedung_list)
    gedung_select.setCurrentIndex(get_current_gedung)
    form_layout.addRow("Gedung:", gedung_select)

    # Lantai (Floor) Dropdown and class
    lantai_list = ["1", "2", "3"]
    ruangan_list = [str(i) for i in range(1, 11)]
    
    get_current_kelas = data['lokasi'][1]
    
    get_current_lantai = lantai_list.index(get_current_kelas[0])
    get_current_ruang = ruangan_list.index(get_current_kelas[-1])
    
    lantai_select = QComboBox()
    lantai_select.addItems(lantai_list)
    lantai_select.setCurrentIndex(get_current_lantai)
    form_layout.addRow("Lantai:", lantai_select)

    # Ruangan (Room) Dropdown
    ruangan_select = QComboBox()
    ruangan_select.addItems(ruangan_list) 
    ruangan_select.setCurrentIndex(get_current_ruang) 
    form_layout.addRow("Ruangan:", ruangan_select)

    # Create Radio Button Group for Colors
    radio_group = QButtonGroup()

    # Load colors from the file
    with open("app/data/colors.json", "r") as color_File: 
        colors = json.load(color_File)

    # Grid Layout for Color Radio Buttons
    color_grid_layout = QGridLayout()
    row, col = 0, 0

    # Add a radio button and color box for each color in the JSON file
    checkColor = []
    for key, values in colors.items():
        color_name = values[0]
        primary_color = values[1]  # Primary color (e.g., "rgb(239, 20, 20)")

        # Create radio button
        radio_button = QRadioButton(f"{color_name}")  # Add name for clarity
        radio_group.addButton(radio_button, int(key))  # Use key as the ID
        
        # Style radio button (to show black border and selection effect)
        radio_button.setStyleSheet(f"""
            QRadioButton {{
                padding: 5px;
                border: 2px solid black;
                border-radius: 5px;
                background-color: {primary_color};
            }}
            QRadioButton::indicator {{
                width: 16px;
                height: 16px;
                border: 2px solid black;
                border-radius: 8px;
                background-color: white;
            }}
            QRadioButton::indicator:checked {{
                background-color: #4CAF50;  /* Green for selected state */
                border: 2px solid black;
            }}
            QRadioButton::indicator:checked:hover {{
                background-color: #45a049;  /* Darker green on hover */
            }}
        """)

        # Add the radio button to the grid layout
        color_grid_layout.addWidget(radio_button, row, col)
        
        checkColor.append(radio_button)
        
        # Adjust row and column for grid layout
        col += 1
        if col > 3:  # Change number of columns here if needed
            col = 0
            row += 1
    
    current_color = int(data.get("color_id", "1")) - 1
    checkColor[(current_color)].setChecked(True)
    
    # Add the color grid layout to the form layout
    form_layout.addRow("Select Color:", color_grid_layout)

    # Buttons
    submit_button = QPushButton("Submit")
    cancel_button = QPushButton("Cancel")

    # Close modal on cancel
    cancel_button.clicked.connect(modal.reject)

    # Submission logic
    def submit_form():
        # Get values from the inputs
        course_name = course_name_input.text()
        hari = (hari_select.currentText()).lower()
        sesi = sesi_select.currentText()
        gedung = gedung_select.currentText()
        lantai = lantai_select.currentText()
        ruangan = ruangan_select.currentText()

        # Get the selected color
        selected_color_id = radio_group.checkedId()
        selected_color = colors.get(str(selected_color_id), ['grey', 'rgb(202, 202, 202)', 'rgb(235, 235, 235)']) 
        
        print(selected_color)
        
        for key, value in colors.items():
            if value == selected_color:
                selected_color = key
                break
        
        course_identificatio =[course_name, hari, sesi, gedung, f"{lantai}0{ruangan}", selected_color]        
        edit_course_identification(course_identificatio, course_id)
                
        modal.accept()

    submit_button.clicked.connect(submit_form)

    # Buttons Layout
    buttons_layout = QHBoxLayout()
    buttons_layout.addStretch()
    buttons_layout.addWidget(cancel_button)
    buttons_layout.addWidget(submit_button)

    # Main layout
    main_layout.addLayout(form_layout)
    main_layout.addLayout(buttons_layout)

    modal.setLayout(main_layout)

    # Execute the dialog and wait for user interaction
    modal.exec_()
    
def edit_course_identification(data, course_id): 
    path = f"app/data/courses/{course_id}/id.json"
    
    
    write_data = {
        "title": data[0], 
        "color_id": data[5], 
        "sesi": data[2], 
        "hari": data[1], 
        "lokasi": [data[3], data[4]]
    }
    
    with open(path, "w") as file: 
        json.dump(write_data, file, indent=4)

    print(write_data)