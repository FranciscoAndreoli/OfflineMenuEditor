import os
import json


class JSONFileManager:
    def __init__(self):

        self.user_folder = os.path.expanduser('~') #Obtiene la direccion del usuario
        # Crea el camino para la nueva carpeta
        self.folder_path = os.path.join(self.user_folder, '.offline-menu-editor')
        # Crea la carpeta para almacenar los JSONS
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
            print("Folder created, directory = ", self.folder_path)

    def saveToFile(self, text, filename):
        filepath = os.path.join(self.folder_path, filename)
        try:
            json.loads(text)
            with open(filepath, "w") as file:
                file.write(text)
            print("Succesfully saved")
            return True
        except json.JSONDecodeError:
            return False

    def getJson(self, filename):
        filepath = os.path.join(self.folder_path, filename)
        try:
            with open(filepath) as file:
                data = json.load(file)
            return data, True
        except FileNotFoundError:
            #print("File not found: ", filepath)
            return False, False
        except json.JSONDecodeError:
            #print("Error decoding JSON file: ", filepath)
            return False, False

