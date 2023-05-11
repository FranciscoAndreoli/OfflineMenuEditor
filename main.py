import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
from JSONFileManager import JSONFileManager
from JSONEditor import JSONEditor
from JSONModel import JSONModel
from JSONValidator import JSONValidator

if __name__ == "__main__":
    app = QApplication(sys.argv)
    JSON_File_Manager = JSONFileManager() # Creamos instancias de las clases y luego lo pasamos como parámetro al constructor de mainWindow. Inyección de dependencias.
    JSON_Editor = JSONEditor()
    JSON_Model = JSONModel()
    JSON_Validator = JSONValidator()
    main_Window = MainWindow(JSON_File_Manager, JSON_Editor, JSON_Model, JSON_Validator)
    main_Window.show()
    sys.exit(app.exec())

#An instance of MainWindow is created, passing the instances of the MVC components (JSONFileManager, JSONEditor, JSONModel, and JSONValidator)
#as arguments to the constructor.
#This establishes the connections between the MVC components and the main window, allowing them to interact with each other.*/
