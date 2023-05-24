# This Python file uses the following encoding: utf-8
#import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QDialog, QVBoxLayout, QTextEdit, QPushButton, QFileDialog
#from PySide6.QtGui import QDragEnterEvent, QDropEvent
from ui_form import Ui_MainWindow
#from DragDrop import DragDrop
import json
class MainWindow(QMainWindow):

    def __init__(self, JSON_File_Manager,JSON_Editor, JSON_Model, JSON_Validator, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.JSONFileManager = JSON_File_Manager
        self.JSONEditor = JSON_Editor
        self.JSONModel = JSON_Model
        self.JSONValidator = JSON_Validator

        #self.ui.buttonDrop.drop.connect(lambda:self.uploadJsonFromDragDropButton("Slot1.json"))

        self.ui.buttonUploadJson.clicked.connect(lambda:self.uploadJsonFromQPlainText("slot1.json", self.ui.boxJsonLoader))
        self.ui.buttonUploadJson_2.clicked.connect(lambda:self.uploadJsonFromQPlainText("slot2.json", self.ui.boxJsonLoader_2))
        self.ui.buttonUploadJson_3.clicked.connect(lambda:self.uploadJsonFromQPlainText("slot3.json", self.ui.boxJsonLoader_3))
        self.ui.buttonUploadJson_4.clicked.connect(lambda:self.uploadJsonFromQPlainText("slot4.json", self.ui.boxJsonLoader_4))
        self.ui.buttonUploadJson_5.clicked.connect(lambda:self.uploadJsonFromQPlainText("slot5.json", self.ui.boxJsonLoader_5))

        self.ui.buttonExistingJson.clicked.connect(lambda: self.getJson("slot1.json"))
        self.ui.buttonExistingJson_2.clicked.connect(lambda: self.getJson("slot2.json"))
        self.ui.buttonExistingJson_3.clicked.connect(lambda: self.getJson("slot3.json"))
        self.ui.buttonExistingJson_4.clicked.connect(lambda: self.getJson("slot4.json"))
        self.ui.buttonExistingJson_5.clicked.connect(lambda: self.getJson("slot5.json"))

        self.ui.buttonDrop.clicked.connect(lambda:self.uploadJsonFromDragDropButton("Slot1.json"))
        self.ui.buttonDrop_2.clicked.connect(lambda:self.uploadJsonFromDragDropButton("Slot2.json"))
        self.ui.buttonDrop_3.clicked.connect(lambda:self.uploadJsonFromDragDropButton("Slot3.json"))
        self.ui.buttonDrop_4.clicked.connect(lambda:self.uploadJsonFromDragDropButton("Slot4.json"))
        self.ui.buttonDrop_5.clicked.connect(lambda:self.uploadJsonFromDragDropButton("Slot5.json"))


    def uploadJsonFromDragDropButton(self,filename):
        print("Button pressed: " + filename)
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Select File")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("JSON Files (*.json);;Text Files (*.txt)")
        file_dialog.fileSelected.connect(lambda file_path: self.JSONFileManager.uploadFileWithDragDropButton(file_path, filename))
        file_dialog.exec_()


    def uploadJsonFromQPlainText(self,filename, textEdit):
        text = textEdit.toPlainText()
        success = self.JSONFileManager.saveToFile(text, filename)
        textEdit.clear()
        if success:
            QMessageBox.information(self, "Success", "JSON file saved")
        else:
            QMessageBox.critical(self, "Error", "Invalid JSON text")



    def getJson(self, filename):
        jsonData, success = self.JSONFileManager.getJson(filename)
        if success:
            self.openJsonViewer(jsonData)
        else:
            QMessageBox.critical(self, "Error", "Error decoding JSON file: " + filename)


    def openJsonViewer(self, jsonData):

        dialog = QDialog()
        dialog.setWindowTitle("JSON Viewer")
        layout = QVBoxLayout()
        text_edit = QTextEdit()
        text_edit.setPlainText(json.dumps(jsonData, indent=4))
        layout.addWidget(text_edit)
        close_button = QPushButton("Close")
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.exec()
