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
            print("Carpeta creada, direccion = ", self.folder_path)

    def saveToFile(self, text, filename):
        filepath = os.path.join(self.folder_path, filename)
        try:
            json.loads(text)
            with open(filepath, "w") as file:
                file.write(text)
            print("Guardado Exitosamente")
        except json.JSONDecodeError:
            print("Error: El texto no es un JSON válido")

    def getFile(self, filename):
        filepath = os.path.join(self.folder_path, filename)
        try:
            with open(filepath) as file:
                data = json.load(file)

            # Convert the JSON data to string
            json_text = json.dumps(data, indent=4)

            return json_text
        except FileNotFoundError:
            print("Archivo no encontrado: ", filepath)
        except json.JSONDecodeError:
            print("Error decodificando archivo JSON: ", filepath)
