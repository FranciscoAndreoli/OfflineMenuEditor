# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self, JSON_File_Manager,JSON_Editor, JSON_Model, JSON_Validator, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.JSONFileManager = JSON_File_Manager
        self.JSONEditor = JSON_Editor
        self.JSONModel = JSON_Model
        self.JSONValidator = JSON_Validator

        self.ui.buttonSaveSlot1.clicked.connect(lambda:self.saveToFileSlot("Slot1.json", self.ui.textEditSlot1))
        self.ui.buttonSaveSlot2.clicked.connect(lambda:self.saveToFileSlot("Slot2.json", self.ui.textEditSlot2))
        self.ui.buttonSaveSlot3.clicked.connect(lambda:self.saveToFileSlot("Slot3.json", self.ui.textEditSlot3))
        self.ui.buttonGetSlot1.clicked.connect(lambda: self.getFileSlot("Slot1.json", self.ui.textEditSlot1))
        self.ui.buttonGetSlot2.clicked.connect(lambda: self.getFileSlot("Slot2.json", self.ui.textEditSlot2))
        self.ui.buttonGetSlot3.clicked.connect(lambda: self.getFileSlot("Slot3.json", self.ui.textEditSlot3))

    def saveToFileSlot(self,filename, textEdit):
        text = textEdit.toPlainText()
        self.JSONFileManager.saveToFile(text, filename)

    def getFileSlot(self, filename, textEdit):
        text = self.JSONFileManager.getFile(filename)
        textEdit.setPlainText(text)
