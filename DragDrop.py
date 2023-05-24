from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from JSONFileManager import JSONFileManager

class DragDrop(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAcceptDrops(True)
        self.JSONFileManager = JSONFileManager()

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            for url in urls:
                file_path = url.toLocalFile()
                if file_path.endswith((".txt", ".json")):
                    event.acceptProposedAction()
                    return

        event.ignore()

    def dropEvent(self, event: QDropEvent):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            print("Archivo soltado:", file_path)
            self.handleDrop(file_path)

    def handleDrop(self, file_path): #Here i get from wich button the drag and drop was activated
        parent_widget = self.parentWidget()

        while parent_widget is not None:
            if isinstance(parent_widget, QWidget) and parent_widget.objectName()[:4].lower() =='slot':
                #print("Widget name:", parent_widget.objectName())
                break
            parent_widget = parent_widget.parentWidget()

        slotName = parent_widget.objectName() + ".json"
        print("slot: ", slotName)
        file_text = JSONFileManager.readTextFromFile(file_path)
        self.JSONFileManager.saveToFile(file_text, slotName)
        #print("Json presente en ", parent_widget.objectName(), ": ", file_text)
