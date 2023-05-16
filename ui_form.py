# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1146, 656)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_14 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFocusPolicy(Qt.ClickFocus)
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.slot1 = QWidget()
        self.slot1.setObjectName(u"slot1")
        self.slot1.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.slot1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frameHeader = QFrame(self.slot1)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setMinimumSize(QSize(0, 50))
        self.frameHeader.setMaximumSize(QSize(16777215, 50))
        self.frameHeader.setStyleSheet(u"")
        self.frameHeader.setFrameShape(QFrame.Box)
        self.frameHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frameHeader)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.nameOfSlot = QLabel(self.frameHeader)
        self.nameOfSlot.setObjectName(u"nameOfSlot")

        self.horizontalLayout_27.addWidget(self.nameOfSlot)

        self.horizontalSpacer_6 = QSpacerItem(944, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.frameHeader)

        self.frameMainTax = QFrame(self.slot1)
        self.frameMainTax.setObjectName(u"frameMainTax")
        self.frameMainTax.setMinimumSize(QSize(0, 150))
        self.frameMainTax.setMaximumSize(QSize(16777215, 150))
        self.frameMainTax.setFrameShape(QFrame.StyledPanel)
        self.frameMainTax.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frameMainTax)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frameTax = QFrame(self.frameMainTax)
        self.frameTax.setObjectName(u"frameTax")
        self.frameTax.setMinimumSize(QSize(300, 0))
        self.frameTax.setMaximumSize(QSize(16777215, 150))
        self.frameTax.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frameTax.setFrameShape(QFrame.Box)
        self.frameTax.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frameTax)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.labelTaxFrame = QLabel(self.frameTax)
        self.labelTaxFrame.setObjectName(u"labelTaxFrame")

        self.verticalLayout_9.addWidget(self.labelTaxFrame)

        self.frameTaxType = QFrame(self.frameTax)
        self.frameTaxType.setObjectName(u"frameTaxType")
        self.frameTaxType.setMinimumSize(QSize(0, 25))
        self.frameTaxType.setFrameShape(QFrame.StyledPanel)
        self.frameTaxType.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frameTaxType)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.labelTaxType = QLabel(self.frameTaxType)
        self.labelTaxType.setObjectName(u"labelTaxType")
        self.labelTaxType.setMinimumSize(QSize(150, 0))
        self.labelTaxType.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_28.addWidget(self.labelTaxType)

        self.labelTaxIncluded = QLabel(self.frameTaxType)
        self.labelTaxIncluded.setObjectName(u"labelTaxIncluded")

        self.horizontalLayout_28.addWidget(self.labelTaxIncluded)


        self.verticalLayout_9.addWidget(self.frameTaxType)

        self.frameDisplayTax = QFrame(self.frameTax)
        self.frameDisplayTax.setObjectName(u"frameDisplayTax")
        self.frameDisplayTax.setMinimumSize(QSize(0, 25))
        self.frameDisplayTax.setFrameShape(QFrame.StyledPanel)
        self.frameDisplayTax.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frameDisplayTax)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.labelDisplayTax = QLabel(self.frameDisplayTax)
        self.labelDisplayTax.setObjectName(u"labelDisplayTax")
        self.labelDisplayTax.setMinimumSize(QSize(150, 0))
        self.labelDisplayTax.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_31.addWidget(self.labelDisplayTax)

        self.labelTrueFalseTax = QLabel(self.frameDisplayTax)
        self.labelTrueFalseTax.setObjectName(u"labelTrueFalseTax")

        self.horizontalLayout_31.addWidget(self.labelTrueFalseTax)


        self.verticalLayout_9.addWidget(self.frameDisplayTax)

        self.frameNameNewTax = QFrame(self.frameTax)
        self.frameNameNewTax.setObjectName(u"frameNameNewTax")
        self.frameNameNewTax.setMinimumSize(QSize(0, 25))
        self.frameNameNewTax.setFrameShape(QFrame.StyledPanel)
        self.frameNameNewTax.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frameNameNewTax)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.labelNewTax = QLabel(self.frameNameNewTax)
        self.labelNewTax.setObjectName(u"labelNewTax")
        self.labelNewTax.setMinimumSize(QSize(150, 0))
        self.labelNewTax.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_29.addWidget(self.labelNewTax)

        self.labelPercentageNewTax = QLabel(self.frameNameNewTax)
        self.labelPercentageNewTax.setObjectName(u"labelPercentageNewTax")
        self.labelPercentageNewTax.setMinimumSize(QSize(100, 0))
        self.labelPercentageNewTax.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_29.addWidget(self.labelPercentageNewTax)

        self.horizontalSpacer_8 = QSpacerItem(163, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_8)

        self.buttonRemoveTax = QPushButton(self.frameNameNewTax)
        self.buttonRemoveTax.setObjectName(u"buttonRemoveTax")
        self.buttonRemoveTax.setMinimumSize(QSize(100, 0))
        self.buttonRemoveTax.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_29.addWidget(self.buttonRemoveTax)


        self.verticalLayout_9.addWidget(self.frameNameNewTax)

        self.frameButtonAddTax = QFrame(self.frameTax)
        self.frameButtonAddTax.setObjectName(u"frameButtonAddTax")
        self.frameButtonAddTax.setMinimumSize(QSize(0, 25))
        self.frameButtonAddTax.setFrameShape(QFrame.StyledPanel)
        self.frameButtonAddTax.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frameButtonAddTax)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_7)

        self.buttonAddTax = QPushButton(self.frameButtonAddTax)
        self.buttonAddTax.setObjectName(u"buttonAddTax")
        self.buttonAddTax.setMinimumSize(QSize(100, 0))
        self.buttonAddTax.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_30.addWidget(self.buttonAddTax, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.frameButtonAddTax)


        self.horizontalLayout_5.addWidget(self.frameTax)

        self.horizontalSpacer = QSpacerItem(536, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frameMainTax)

        self.frameJsonOptions = QFrame(self.slot1)
        self.frameJsonOptions.setObjectName(u"frameJsonOptions")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameJsonOptions.sizePolicy().hasHeightForWidth())
        self.frameJsonOptions.setSizePolicy(sizePolicy)
        self.frameJsonOptions.setMinimumSize(QSize(0, 50))
        self.frameJsonOptions.setMaximumSize(QSize(16777215, 200))
        self.frameJsonOptions.setFrameShape(QFrame.StyledPanel)
        self.frameJsonOptions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameJsonOptions)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameDropFiles = QFrame(self.frameJsonOptions)
        self.frameDropFiles.setObjectName(u"frameDropFiles")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameDropFiles.sizePolicy().hasHeightForWidth())
        self.frameDropFiles.setSizePolicy(sizePolicy1)
        self.frameDropFiles.setMinimumSize(QSize(300, 0))
        self.frameDropFiles.setFrameShape(QFrame.StyledPanel)
        self.frameDropFiles.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameDropFiles)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.frameDropFiles)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMinimumSize(QSize(2, 0))

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.horizontalLayout.addWidget(self.frameDropFiles)

        self.framePasteJson = QFrame(self.frameJsonOptions)
        self.framePasteJson.setObjectName(u"framePasteJson")
        self.framePasteJson.setMinimumSize(QSize(350, 0))
        self.framePasteJson.setFrameShape(QFrame.StyledPanel)
        self.framePasteJson.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.framePasteJson)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frameJson = QFrame(self.framePasteJson)
        self.frameJson.setObjectName(u"frameJson")
        self.frameJson.setFrameShape(QFrame.StyledPanel)
        self.frameJson.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frameJson)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.boxJsonLoader = QPlainTextEdit(self.frameJson)
        self.boxJsonLoader.setObjectName(u"boxJsonLoader")
        sizePolicy2.setHeightForWidth(self.boxJsonLoader.sizePolicy().hasHeightForWidth())
        self.boxJsonLoader.setSizePolicy(sizePolicy2)
        self.boxJsonLoader.setAutoFillBackground(True)
        self.boxJsonLoader.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.boxJsonLoader)


        self.verticalLayout_3.addWidget(self.frameJson)

        self.frameUploadExisting = QFrame(self.framePasteJson)
        self.frameUploadExisting.setObjectName(u"frameUploadExisting")
        self.frameUploadExisting.setFrameShape(QFrame.StyledPanel)
        self.frameUploadExisting.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameUploadExisting)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonUploadJson = QPushButton(self.frameUploadExisting)
        self.buttonUploadJson.setObjectName(u"buttonUploadJson")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.buttonUploadJson.sizePolicy().hasHeightForWidth())
        self.buttonUploadJson.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.buttonUploadJson)

        self.buttonExistingJson = QPushButton(self.frameUploadExisting)
        self.buttonExistingJson.setObjectName(u"buttonExistingJson")
        self.buttonExistingJson.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.buttonExistingJson)


        self.verticalLayout_3.addWidget(self.frameUploadExisting)


        self.horizontalLayout.addWidget(self.framePasteJson)

        self.frameMenuImage = QFrame(self.frameJsonOptions)
        self.frameMenuImage.setObjectName(u"frameMenuImage")
        self.frameMenuImage.setMinimumSize(QSize(250, 0))
        self.frameMenuImage.setSizeIncrement(QSize(0, 0))
        self.frameMenuImage.setStyleSheet(u"")
        self.frameMenuImage.setFrameShape(QFrame.Box)
        self.frameMenuImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frameMenuImage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LabelMenuImage = QLabel(self.frameMenuImage)
        self.LabelMenuImage.setObjectName(u"LabelMenuImage")

        self.verticalLayout.addWidget(self.LabelMenuImage)

        self.menuImage = QLabel(self.frameMenuImage)
        self.menuImage.setObjectName(u"menuImage")
        self.menuImage.setFrameShape(QFrame.Box)
        self.menuImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.menuImage)


        self.horizontalLayout.addWidget(self.frameMenuImage)

        self.frameLoadAll = QFrame(self.frameJsonOptions)
        self.frameLoadAll.setObjectName(u"frameLoadAll")
        self.frameLoadAll.setFrameShape(QFrame.StyledPanel)
        self.frameLoadAll.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frameLoadAll)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_2 = QSpacerItem(20, 134, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.buttonLoadAll = QPushButton(self.frameLoadAll)
        self.buttonLoadAll.setObjectName(u"buttonLoadAll")
        self.buttonLoadAll.setMinimumSize(QSize(0, 35))

        self.verticalLayout_8.addWidget(self.buttonLoadAll)


        self.horizontalLayout.addWidget(self.frameLoadAll)


        self.verticalLayout_2.addWidget(self.frameJsonOptions)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.slot1, "")
        self.slot2 = QWidget()
        self.slot2.setObjectName(u"slot2")
        self.verticalLayout_15 = QVBoxLayout(self.slot2)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frameHeader_2 = QFrame(self.slot2)
        self.frameHeader_2.setObjectName(u"frameHeader_2")
        self.frameHeader_2.setMinimumSize(QSize(0, 50))
        self.frameHeader_2.setMaximumSize(QSize(16777215, 50))
        self.frameHeader_2.setStyleSheet(u"")
        self.frameHeader_2.setFrameShape(QFrame.Box)
        self.frameHeader_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frameHeader_2)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.nameOfSlot_2 = QLabel(self.frameHeader_2)
        self.nameOfSlot_2.setObjectName(u"nameOfSlot_2")

        self.horizontalLayout_37.addWidget(self.nameOfSlot_2)

        self.horizontalSpacer_12 = QSpacerItem(944, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_12)


        self.verticalLayout_15.addWidget(self.frameHeader_2)

        self.frameMainTax_2 = QFrame(self.slot2)
        self.frameMainTax_2.setObjectName(u"frameMainTax_2")
        self.frameMainTax_2.setMinimumSize(QSize(0, 150))
        self.frameMainTax_2.setMaximumSize(QSize(16777215, 150))
        self.frameMainTax_2.setFrameShape(QFrame.StyledPanel)
        self.frameMainTax_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frameMainTax_2)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frameTax_2 = QFrame(self.frameMainTax_2)
        self.frameTax_2.setObjectName(u"frameTax_2")
        self.frameTax_2.setMinimumSize(QSize(300, 0))
        self.frameTax_2.setMaximumSize(QSize(16777215, 150))
        self.frameTax_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frameTax_2.setFrameShape(QFrame.Box)
        self.frameTax_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frameTax_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.labelTaxFrame_2 = QLabel(self.frameTax_2)
        self.labelTaxFrame_2.setObjectName(u"labelTaxFrame_2")

        self.verticalLayout_10.addWidget(self.labelTaxFrame_2)

        self.frameTaxType_2 = QFrame(self.frameTax_2)
        self.frameTaxType_2.setObjectName(u"frameTaxType_2")
        self.frameTaxType_2.setMinimumSize(QSize(0, 25))
        self.frameTaxType_2.setFrameShape(QFrame.StyledPanel)
        self.frameTaxType_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frameTaxType_2)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.labelTaxType_2 = QLabel(self.frameTaxType_2)
        self.labelTaxType_2.setObjectName(u"labelTaxType_2")
        self.labelTaxType_2.setMinimumSize(QSize(150, 0))
        self.labelTaxType_2.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_33.addWidget(self.labelTaxType_2)

        self.labelTaxIncluded_2 = QLabel(self.frameTaxType_2)
        self.labelTaxIncluded_2.setObjectName(u"labelTaxIncluded_2")

        self.horizontalLayout_33.addWidget(self.labelTaxIncluded_2)


        self.verticalLayout_10.addWidget(self.frameTaxType_2)

        self.frameDisplayTax_2 = QFrame(self.frameTax_2)
        self.frameDisplayTax_2.setObjectName(u"frameDisplayTax_2")
        self.frameDisplayTax_2.setMinimumSize(QSize(0, 25))
        self.frameDisplayTax_2.setFrameShape(QFrame.StyledPanel)
        self.frameDisplayTax_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frameDisplayTax_2)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.labelDisplayTax_2 = QLabel(self.frameDisplayTax_2)
        self.labelDisplayTax_2.setObjectName(u"labelDisplayTax_2")
        self.labelDisplayTax_2.setMinimumSize(QSize(150, 0))
        self.labelDisplayTax_2.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_34.addWidget(self.labelDisplayTax_2)

        self.labelTrueFalseTax_2 = QLabel(self.frameDisplayTax_2)
        self.labelTrueFalseTax_2.setObjectName(u"labelTrueFalseTax_2")

        self.horizontalLayout_34.addWidget(self.labelTrueFalseTax_2)


        self.verticalLayout_10.addWidget(self.frameDisplayTax_2)

        self.frameNameNewTax_2 = QFrame(self.frameTax_2)
        self.frameNameNewTax_2.setObjectName(u"frameNameNewTax_2")
        self.frameNameNewTax_2.setMinimumSize(QSize(0, 25))
        self.frameNameNewTax_2.setFrameShape(QFrame.StyledPanel)
        self.frameNameNewTax_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frameNameNewTax_2)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.labelNewTax_2 = QLabel(self.frameNameNewTax_2)
        self.labelNewTax_2.setObjectName(u"labelNewTax_2")
        self.labelNewTax_2.setMinimumSize(QSize(150, 0))
        self.labelNewTax_2.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_35.addWidget(self.labelNewTax_2)

        self.labelPercentageNewTax_2 = QLabel(self.frameNameNewTax_2)
        self.labelPercentageNewTax_2.setObjectName(u"labelPercentageNewTax_2")
        self.labelPercentageNewTax_2.setMinimumSize(QSize(100, 0))
        self.labelPercentageNewTax_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_35.addWidget(self.labelPercentageNewTax_2)

        self.horizontalSpacer_9 = QSpacerItem(163, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_9)

        self.buttonRemoveTax_2 = QPushButton(self.frameNameNewTax_2)
        self.buttonRemoveTax_2.setObjectName(u"buttonRemoveTax_2")
        self.buttonRemoveTax_2.setMinimumSize(QSize(100, 0))
        self.buttonRemoveTax_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_35.addWidget(self.buttonRemoveTax_2)


        self.verticalLayout_10.addWidget(self.frameNameNewTax_2)

        self.frameButtonAddTax_2 = QFrame(self.frameTax_2)
        self.frameButtonAddTax_2.setObjectName(u"frameButtonAddTax_2")
        self.frameButtonAddTax_2.setMinimumSize(QSize(0, 25))
        self.frameButtonAddTax_2.setFrameShape(QFrame.StyledPanel)
        self.frameButtonAddTax_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frameButtonAddTax_2)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_10)

        self.buttonAddTax_2 = QPushButton(self.frameButtonAddTax_2)
        self.buttonAddTax_2.setObjectName(u"buttonAddTax_2")
        self.buttonAddTax_2.setMinimumSize(QSize(100, 0))
        self.buttonAddTax_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_36.addWidget(self.buttonAddTax_2, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_10.addWidget(self.frameButtonAddTax_2)


        self.horizontalLayout_32.addWidget(self.frameTax_2)

        self.horizontalSpacer_11 = QSpacerItem(536, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_11)


        self.verticalLayout_15.addWidget(self.frameMainTax_2)

        self.frameJsonOptions_2 = QFrame(self.slot2)
        self.frameJsonOptions_2.setObjectName(u"frameJsonOptions_2")
        sizePolicy.setHeightForWidth(self.frameJsonOptions_2.sizePolicy().hasHeightForWidth())
        self.frameJsonOptions_2.setSizePolicy(sizePolicy)
        self.frameJsonOptions_2.setMinimumSize(QSize(0, 50))
        self.frameJsonOptions_2.setMaximumSize(QSize(16777215, 200))
        self.frameJsonOptions_2.setFrameShape(QFrame.StyledPanel)
        self.frameJsonOptions_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frameJsonOptions_2)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frameDropFiles_2 = QFrame(self.frameJsonOptions_2)
        self.frameDropFiles_2.setObjectName(u"frameDropFiles_2")
        sizePolicy1.setHeightForWidth(self.frameDropFiles_2.sizePolicy().hasHeightForWidth())
        self.frameDropFiles_2.setSizePolicy(sizePolicy1)
        self.frameDropFiles_2.setMinimumSize(QSize(300, 0))
        self.frameDropFiles_2.setFrameShape(QFrame.StyledPanel)
        self.frameDropFiles_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frameDropFiles_2)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.pushButton_16 = QPushButton(self.frameDropFiles_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy2.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy2)
        self.pushButton_16.setMinimumSize(QSize(2, 0))

        self.horizontalLayout_39.addWidget(self.pushButton_16)


        self.horizontalLayout_38.addWidget(self.frameDropFiles_2)

        self.framePasteJson_2 = QFrame(self.frameJsonOptions_2)
        self.framePasteJson_2.setObjectName(u"framePasteJson_2")
        self.framePasteJson_2.setMinimumSize(QSize(350, 0))
        self.framePasteJson_2.setFrameShape(QFrame.StyledPanel)
        self.framePasteJson_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.framePasteJson_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frameJson_2 = QFrame(self.framePasteJson_2)
        self.frameJson_2.setObjectName(u"frameJson_2")
        self.frameJson_2.setFrameShape(QFrame.StyledPanel)
        self.frameJson_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frameJson_2)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.boxJsonLoader_2 = QPlainTextEdit(self.frameJson_2)
        self.boxJsonLoader_2.setObjectName(u"boxJsonLoader_2")
        sizePolicy2.setHeightForWidth(self.boxJsonLoader_2.sizePolicy().hasHeightForWidth())
        self.boxJsonLoader_2.setSizePolicy(sizePolicy2)
        self.boxJsonLoader_2.setAutoFillBackground(True)
        self.boxJsonLoader_2.setStyleSheet(u"")

        self.horizontalLayout_40.addWidget(self.boxJsonLoader_2)


        self.verticalLayout_11.addWidget(self.frameJson_2)

        self.frameUploadExisting_2 = QFrame(self.framePasteJson_2)
        self.frameUploadExisting_2.setObjectName(u"frameUploadExisting_2")
        self.frameUploadExisting_2.setFrameShape(QFrame.StyledPanel)
        self.frameUploadExisting_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frameUploadExisting_2)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.buttonUploadJson_2 = QPushButton(self.frameUploadExisting_2)
        self.buttonUploadJson_2.setObjectName(u"buttonUploadJson_2")
        sizePolicy3.setHeightForWidth(self.buttonUploadJson_2.sizePolicy().hasHeightForWidth())
        self.buttonUploadJson_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_41.addWidget(self.buttonUploadJson_2)

        self.buttonExistingJson_2 = QPushButton(self.frameUploadExisting_2)
        self.buttonExistingJson_2.setObjectName(u"buttonExistingJson_2")
        self.buttonExistingJson_2.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_41.addWidget(self.buttonExistingJson_2)


        self.verticalLayout_11.addWidget(self.frameUploadExisting_2)


        self.horizontalLayout_38.addWidget(self.framePasteJson_2)

        self.frameMenuImage_2 = QFrame(self.frameJsonOptions_2)
        self.frameMenuImage_2.setObjectName(u"frameMenuImage_2")
        self.frameMenuImage_2.setMinimumSize(QSize(250, 0))
        self.frameMenuImage_2.setSizeIncrement(QSize(0, 0))
        self.frameMenuImage_2.setStyleSheet(u"")
        self.frameMenuImage_2.setFrameShape(QFrame.Box)
        self.frameMenuImage_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frameMenuImage_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.LabelMenuImage_2 = QLabel(self.frameMenuImage_2)
        self.LabelMenuImage_2.setObjectName(u"LabelMenuImage_2")

        self.verticalLayout_12.addWidget(self.LabelMenuImage_2)

        self.menuImage_2 = QLabel(self.frameMenuImage_2)
        self.menuImage_2.setObjectName(u"menuImage_2")
        self.menuImage_2.setFrameShape(QFrame.Box)
        self.menuImage_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.menuImage_2)


        self.horizontalLayout_38.addWidget(self.frameMenuImage_2)

        self.frameLoadAll_2 = QFrame(self.frameJsonOptions_2)
        self.frameLoadAll_2.setObjectName(u"frameLoadAll_2")
        self.frameLoadAll_2.setFrameShape(QFrame.StyledPanel)
        self.frameLoadAll_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frameLoadAll_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSpacer_4 = QSpacerItem(20, 134, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.buttonLoadAll_2 = QPushButton(self.frameLoadAll_2)
        self.buttonLoadAll_2.setObjectName(u"buttonLoadAll_2")
        self.buttonLoadAll_2.setMinimumSize(QSize(0, 35))

        self.verticalLayout_13.addWidget(self.buttonLoadAll_2)


        self.horizontalLayout_38.addWidget(self.frameLoadAll_2)


        self.verticalLayout_15.addWidget(self.frameJsonOptions_2)

        self.verticalSpacer_3 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.slot2, "")
        self.slot3 = QWidget()
        self.slot3.setObjectName(u"slot3")
        self.buttonSaveSlot3 = QPushButton(self.slot3)
        self.buttonSaveSlot3.setObjectName(u"buttonSaveSlot3")
        self.buttonSaveSlot3.setGeometry(QRect(0, 88, 75, 24))
        self.textEditSlot3 = QPlainTextEdit(self.slot3)
        self.textEditSlot3.setObjectName(u"textEditSlot3")
        self.textEditSlot3.setGeometry(QRect(162, 0, 256, 192))
        self.buttonGetSlot3 = QPushButton(self.slot3)
        self.buttonGetSlot3.setObjectName(u"buttonGetSlot3")
        self.buttonGetSlot3.setGeometry(QRect(81, 88, 75, 24))
        self.tabWidget.addTab(self.slot3, "")

        self.verticalLayout_14.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1146, 22))
        self.menuOME = QMenu(self.menubar)
        self.menuOME.setObjectName(u"menuOME")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOME.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nameOfSlot.setText(QCoreApplication.translate("MainWindow", u"NAME OF THE SLOT", None))
        self.labelTaxFrame.setText(QCoreApplication.translate("MainWindow", u"Tax Rates", None))
        self.labelTaxType.setText(QCoreApplication.translate("MainWindow", u"Tax Type:", None))
        self.labelTaxIncluded.setText(QCoreApplication.translate("MainWindow", u"IncludedInBasePrice", None))
        self.labelDisplayTax.setText(QCoreApplication.translate("MainWindow", u"Display Tax:", None))
        self.labelTrueFalseTax.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.labelNewTax.setText(QCoreApplication.translate("MainWindow", u"Name of New Tax", None))
        self.labelPercentageNewTax.setText(QCoreApplication.translate("MainWindow", u"6.000%", None))
        self.buttonRemoveTax.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        self.buttonAddTax.setText(QCoreApplication.translate("MainWindow", u"ADD NEW", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Drop files to upload (or click)", None))
        self.buttonUploadJson.setText(QCoreApplication.translate("MainWindow", u"UPLOAD JSON", None))
        self.buttonExistingJson.setText(QCoreApplication.translate("MainWindow", u"EXISTING JSON", None))
        self.LabelMenuImage.setText(QCoreApplication.translate("MainWindow", u"MENU IMAGE", None))
        self.menuImage.setText(QCoreApplication.translate("MainWindow", u"IMAGE", None))
        self.buttonLoadAll.setText(QCoreApplication.translate("MainWindow", u"LOAD ALL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.slot1), QCoreApplication.translate("MainWindow", u"Slot 1", None))
        self.nameOfSlot_2.setText(QCoreApplication.translate("MainWindow", u"NAME OF THE SLOT", None))
        self.labelTaxFrame_2.setText(QCoreApplication.translate("MainWindow", u"Tax Rates", None))
        self.labelTaxType_2.setText(QCoreApplication.translate("MainWindow", u"Tax Type:", None))
        self.labelTaxIncluded_2.setText(QCoreApplication.translate("MainWindow", u"IncludedInBasePrice", None))
        self.labelDisplayTax_2.setText(QCoreApplication.translate("MainWindow", u"Display Tax:", None))
        self.labelTrueFalseTax_2.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.labelNewTax_2.setText(QCoreApplication.translate("MainWindow", u"Name of New Tax", None))
        self.labelPercentageNewTax_2.setText(QCoreApplication.translate("MainWindow", u"6.000%", None))
        self.buttonRemoveTax_2.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        self.buttonAddTax_2.setText(QCoreApplication.translate("MainWindow", u"ADD NEW", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Drop files to upload (or click)", None))
        self.buttonUploadJson_2.setText(QCoreApplication.translate("MainWindow", u"UPLOAD JSON", None))
        self.buttonExistingJson_2.setText(QCoreApplication.translate("MainWindow", u"EXISTING JSON", None))
        self.LabelMenuImage_2.setText(QCoreApplication.translate("MainWindow", u"MENU IMAGE", None))
        self.menuImage_2.setText(QCoreApplication.translate("MainWindow", u"IMAGE", None))
        self.buttonLoadAll_2.setText(QCoreApplication.translate("MainWindow", u"LOAD ALL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.slot2), QCoreApplication.translate("MainWindow", u"Slot 2", None))
        self.buttonSaveSlot3.setText(QCoreApplication.translate("MainWindow", u"Save - Slot 3", None))
        self.buttonGetSlot3.setText(QCoreApplication.translate("MainWindow", u"Get - Slot 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.slot3), QCoreApplication.translate("MainWindow", u"Slot 3", None))
        self.menuOME.setTitle(QCoreApplication.translate("MainWindow", u"OME", None))
    # retranslateUi

