# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonSaveSlot3 = QPushButton(self.centralwidget)
        self.buttonSaveSlot3.setObjectName(u"buttonSaveSlot3")

        self.gridLayout.addWidget(self.buttonSaveSlot3, 6, 0, 1, 1)

        self.buttonGetSlot1 = QPushButton(self.centralwidget)
        self.buttonGetSlot1.setObjectName(u"buttonGetSlot1")

        self.gridLayout.addWidget(self.buttonGetSlot1, 0, 1, 1, 1)

        self.textEditSlot3 = QPlainTextEdit(self.centralwidget)
        self.textEditSlot3.setObjectName(u"textEditSlot3")

        self.gridLayout.addWidget(self.textEditSlot3, 6, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.buttonSaveSlot1 = QPushButton(self.centralwidget)
        self.buttonSaveSlot1.setObjectName(u"buttonSaveSlot1")

        self.gridLayout.addWidget(self.buttonSaveSlot1, 0, 0, 1, 1)

        self.textEditSlot1 = QPlainTextEdit(self.centralwidget)
        self.textEditSlot1.setObjectName(u"textEditSlot1")

        self.gridLayout.addWidget(self.textEditSlot1, 0, 2, 1, 1)

        self.buttonSaveSlot2 = QPushButton(self.centralwidget)
        self.buttonSaveSlot2.setObjectName(u"buttonSaveSlot2")

        self.gridLayout.addWidget(self.buttonSaveSlot2, 5, 0, 1, 1)

        self.buttonGetSlot2 = QPushButton(self.centralwidget)
        self.buttonGetSlot2.setObjectName(u"buttonGetSlot2")

        self.gridLayout.addWidget(self.buttonGetSlot2, 5, 1, 1, 1)

        self.textEditSlot2 = QPlainTextEdit(self.centralwidget)
        self.textEditSlot2.setObjectName(u"textEditSlot2")

        self.gridLayout.addWidget(self.textEditSlot2, 5, 2, 1, 1)

        self.buttonGetSlot3 = QPushButton(self.centralwidget)
        self.buttonGetSlot3.setObjectName(u"buttonGetSlot3")

        self.gridLayout.addWidget(self.buttonGetSlot3, 6, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuOME = QMenu(self.menubar)
        self.menuOME.setObjectName(u"menuOME")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOME.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buttonSaveSlot3.setText(QCoreApplication.translate("MainWindow", u"Save - Slot 3", None))
        self.buttonGetSlot1.setText(QCoreApplication.translate("MainWindow", u"Get - Slot 1", None))
        self.buttonSaveSlot1.setText(QCoreApplication.translate("MainWindow", u"Save - Slot 1", None))
        self.buttonSaveSlot2.setText(QCoreApplication.translate("MainWindow", u"Save - Slot 2", None))
        self.buttonGetSlot2.setText(QCoreApplication.translate("MainWindow", u"Get - Slot 2", None))
        self.buttonGetSlot3.setText(QCoreApplication.translate("MainWindow", u"Get - Slot 3", None))
        self.menuOME.setTitle(QCoreApplication.translate("MainWindow", u"OME", None))
    # retranslateUi

