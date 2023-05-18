# This Python file uses the following encoding: utf-8
#import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QDialog, QVBoxLayout, QTextEdit, QPushButton
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from ui_form import Ui_MainWindow
from DragDrop import DragDrop
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

        self.ui.buttonDrop = DragDrop("Drop files to upload (or click)", self)
        self.ui.frameDropFiles.layout().addWidget(self.ui.buttonDrop)
        self.ui.buttonDrop.setFixedSize(300, 190)
        self.ui.buttonDrop.move(26,228)

        self.ui.buttonDrop_2 = DragDrop("Drop files to upload (or click)", self)
        self.ui.frameDropFiles_2.layout().addWidget(self.ui.buttonDrop_2)
        self.ui.buttonDrop_2.setFixedSize(300, 190)
        self.ui.buttonDrop_2.move(26,228)
        #self.ui.buttonDrop_2 = DragDrop("Drop files to upload (or clickkk)", self)
        #buttonDrop_2.setParent(ui.slot2)

        self.ui.buttonUploadJson.clicked.connect(lambda:self.uploadJson("Slot1.json", self.ui.boxJsonLoader))
        self.ui.buttonUploadJson_2.clicked.connect(lambda:self.uploadJson("Slot2.json", self.ui.boxJsonLoader_2))
    #     self.ui.buttonUploadJson_3.clicked.connect(lambda:self.saveToFileSlot("Slot3.json", self.ui.textEditSlot3))
        self.ui.buttonExistingJson.clicked.connect(lambda: self.getJson("Slot1.json"))
        self.ui.buttonExistingJson_2.clicked.connect(lambda: self.getJson("Slot2.json"))
    #     self.ui.buttonExistingJson_3.clicked.connect(lambda: self.getFileSlot("Slot3.json", self.ui.textEditSlot3))
        self.ui.buttonDrop.clicked.connect(lambda:self.uploadJsonFile("Slot1.json"))
        self.ui.buttonDrop_2.clicked.connect(lambda:self.uploadJsonFile("Slot2.json"))

    def uploadJsonFile(self,filename):
        print("Button pressed: " + filename)

    def uploadJson(self,filename, textEdit):
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
