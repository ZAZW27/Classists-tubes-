
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
import sys
import os
import json


def Notif(main_window, ui, check_assignment): 
    stop_loop = False
    notif_data = getData()

    for notif in notif_data: 
        if stop_loop: break
        dialog = QDialog()
        dialog.setWindowTitle(notif.get('title', 'Title not found'))
        dialog.resize(300, 150)

        # Create a layout
        layout = QVBoxLayout()

        # Add a title
        title_label = QLabel(notif.get('title', 'Title not found'))
        layout.addWidget(title_label)

        # Add a description
        description_label = QLabel(notif.get('deskripsi', 'deskripsi not found'))
        layout.addWidget(description_label)

        deadline = QLabel(notif.get('deadline', 'deadline not found'))
        layout.addWidget(deadline)

        # Add buttons
        button_layout = QHBoxLayout()
        
        view_button = QPushButton("View")
        view_button.clicked.connect(lambda: checkAssignemnt())  # Action for the View button
        button_layout.addWidget(view_button)
        def checkAssignemnt():
            stopNotif()
            check_assignment(main_window, ui, notif['path'][0], notif['path'][1])

        def stopNotif(): 
            nonlocal stop_loop 
            stop_loop = True 
            dialog.accept() 
        
        cancel_button = QPushButton("Next")
        cancel_button.clicked.connect(dialog.reject)  # Close the dialog when Cancel is clicked
        button_layout.addWidget(cancel_button)
        
        stopNotifBtn = QPushButton("Close all")
        stopNotifBtn.clicked.connect(lambda: stopNotif())  # Action for the View button
        button_layout.addWidget(stopNotifBtn)

        layout.addLayout(button_layout)

        # Set the layout to the dialog
        dialog.setLayout(layout)

        # Execute the dialog
        if dialog.exec_() == QDialog.Accepted:
            print("Dialog closed with 'Close' button")

def getData(): 
    path = 'app/data/courses'
    courses = (os.listdir(path))
    
    fetched_data = []
    for course in courses: 
        with open(f"{path}/{course}/assignment.json", 'r') as assignments: 
            assignment_data = json.load(assignments)
            
        for assignment_id in assignment_data: 
            if assignment_data[assignment_id]['isFinished'] == False: 
                assignment_data[assignment_id]['path'] = [course, assignment_id]
                fetched_data.append(assignment_data[assignment_id])
    
    return fetched_data
