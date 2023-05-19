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
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
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
        self.verticalLayout_4 = QVBoxLayout(self.slot3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frameHeader_3 = QFrame(self.slot3)
        self.frameHeader_3.setObjectName(u"frameHeader_3")
        self.frameHeader_3.setMinimumSize(QSize(0, 50))
        self.frameHeader_3.setMaximumSize(QSize(16777215, 50))
        self.frameHeader_3.setStyleSheet(u"")
        self.frameHeader_3.setFrameShape(QFrame.Box)
        self.frameHeader_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frameHeader_3)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.nameOfSlot_3 = QLabel(self.frameHeader_3)
        self.nameOfSlot_3.setObjectName(u"nameOfSlot_3")

        self.horizontalLayout_51.addWidget(self.nameOfSlot_3)

        self.horizontalSpacer_16 = QSpacerItem(944, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_16)


        self.verticalLayout_4.addWidget(self.frameHeader_3)

        self.frameMainTax_3 = QFrame(self.slot3)
        self.frameMainTax_3.setObjectName(u"frameMainTax_3")
        self.frameMainTax_3.setMinimumSize(QSize(0, 150))
        self.frameMainTax_3.setMaximumSize(QSize(16777215, 150))
        self.frameMainTax_3.setFrameShape(QFrame.StyledPanel)
        self.frameMainTax_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frameMainTax_3)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frameTax_3 = QFrame(self.frameMainTax_3)
        self.frameTax_3.setObjectName(u"frameTax_3")
        self.frameTax_3.setMinimumSize(QSize(300, 0))
        self.frameTax_3.setMaximumSize(QSize(16777215, 150))
        self.frameTax_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frameTax_3.setFrameShape(QFrame.Box)
        self.frameTax_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frameTax_3)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.labelTaxFrame_3 = QLabel(self.frameTax_3)
        self.labelTaxFrame_3.setObjectName(u"labelTaxFrame_3")

        self.verticalLayout_19.addWidget(self.labelTaxFrame_3)

        self.frameTaxType_3 = QFrame(self.frameTax_3)
        self.frameTaxType_3.setObjectName(u"frameTaxType_3")
        self.frameTaxType_3.setMinimumSize(QSize(0, 25))
        self.frameTaxType_3.setFrameShape(QFrame.StyledPanel)
        self.frameTaxType_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frameTaxType_3)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.labelTaxType_3 = QLabel(self.frameTaxType_3)
        self.labelTaxType_3.setObjectName(u"labelTaxType_3")
        self.labelTaxType_3.setMinimumSize(QSize(150, 0))
        self.labelTaxType_3.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_47.addWidget(self.labelTaxType_3)

        self.labelTaxIncluded_3 = QLabel(self.frameTaxType_3)
        self.labelTaxIncluded_3.setObjectName(u"labelTaxIncluded_3")

        self.horizontalLayout_47.addWidget(self.labelTaxIncluded_3)


        self.verticalLayout_19.addWidget(self.frameTaxType_3)

        self.frameDisplayTax_3 = QFrame(self.frameTax_3)
        self.frameDisplayTax_3.setObjectName(u"frameDisplayTax_3")
        self.frameDisplayTax_3.setMinimumSize(QSize(0, 25))
        self.frameDisplayTax_3.setFrameShape(QFrame.StyledPanel)
        self.frameDisplayTax_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frameDisplayTax_3)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.labelDisplayTax_3 = QLabel(self.frameDisplayTax_3)
        self.labelDisplayTax_3.setObjectName(u"labelDisplayTax_3")
        self.labelDisplayTax_3.setMinimumSize(QSize(150, 0))
        self.labelDisplayTax_3.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_48.addWidget(self.labelDisplayTax_3)

        self.labelTrueFalseTax_3 = QLabel(self.frameDisplayTax_3)
        self.labelTrueFalseTax_3.setObjectName(u"labelTrueFalseTax_3")

        self.horizontalLayout_48.addWidget(self.labelTrueFalseTax_3)


        self.verticalLayout_19.addWidget(self.frameDisplayTax_3)

        self.frameNameNewTax_3 = QFrame(self.frameTax_3)
        self.frameNameNewTax_3.setObjectName(u"frameNameNewTax_3")
        self.frameNameNewTax_3.setMinimumSize(QSize(0, 25))
        self.frameNameNewTax_3.setFrameShape(QFrame.StyledPanel)
        self.frameNameNewTax_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frameNameNewTax_3)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.labelNewTax_3 = QLabel(self.frameNameNewTax_3)
        self.labelNewTax_3.setObjectName(u"labelNewTax_3")
        self.labelNewTax_3.setMinimumSize(QSize(150, 0))
        self.labelNewTax_3.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_49.addWidget(self.labelNewTax_3)

        self.labelPercentageNewTax_3 = QLabel(self.frameNameNewTax_3)
        self.labelPercentageNewTax_3.setObjectName(u"labelPercentageNewTax_3")
        self.labelPercentageNewTax_3.setMinimumSize(QSize(100, 0))
        self.labelPercentageNewTax_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_49.addWidget(self.labelPercentageNewTax_3)

        self.horizontalSpacer_13 = QSpacerItem(163, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_13)

        self.buttonRemoveTax_3 = QPushButton(self.frameNameNewTax_3)
        self.buttonRemoveTax_3.setObjectName(u"buttonRemoveTax_3")
        self.buttonRemoveTax_3.setMinimumSize(QSize(100, 0))
        self.buttonRemoveTax_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_49.addWidget(self.buttonRemoveTax_3)


        self.verticalLayout_19.addWidget(self.frameNameNewTax_3)

        self.frameButtonAddTax_3 = QFrame(self.frameTax_3)
        self.frameButtonAddTax_3.setObjectName(u"frameButtonAddTax_3")
        self.frameButtonAddTax_3.setMinimumSize(QSize(0, 25))
        self.frameButtonAddTax_3.setFrameShape(QFrame.StyledPanel)
        self.frameButtonAddTax_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frameButtonAddTax_3)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_14)

        self.buttonAddTax_3 = QPushButton(self.frameButtonAddTax_3)
        self.buttonAddTax_3.setObjectName(u"buttonAddTax_3")
        self.buttonAddTax_3.setMinimumSize(QSize(100, 0))
        self.buttonAddTax_3.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_50.addWidget(self.buttonAddTax_3, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_19.addWidget(self.frameButtonAddTax_3)


        self.horizontalLayout_46.addWidget(self.frameTax_3)

        self.horizontalSpacer_15 = QSpacerItem(536, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_15)


        self.verticalLayout_4.addWidget(self.frameMainTax_3)

        self.frameJsonOptions_3 = QFrame(self.slot3)
        self.frameJsonOptions_3.setObjectName(u"frameJsonOptions_3")
        sizePolicy.setHeightForWidth(self.frameJsonOptions_3.sizePolicy().hasHeightForWidth())
        self.frameJsonOptions_3.setSizePolicy(sizePolicy)
        self.frameJsonOptions_3.setMinimumSize(QSize(0, 50))
        self.frameJsonOptions_3.setMaximumSize(QSize(16777215, 200))
        self.frameJsonOptions_3.setFrameShape(QFrame.StyledPanel)
        self.frameJsonOptions_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frameJsonOptions_3)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frameDropFiles_3 = QFrame(self.frameJsonOptions_3)
        self.frameDropFiles_3.setObjectName(u"frameDropFiles_3")
        sizePolicy1.setHeightForWidth(self.frameDropFiles_3.sizePolicy().hasHeightForWidth())
        self.frameDropFiles_3.setSizePolicy(sizePolicy1)
        self.frameDropFiles_3.setMinimumSize(QSize(300, 0))
        self.frameDropFiles_3.setFrameShape(QFrame.StyledPanel)
        self.frameDropFiles_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frameDropFiles_3)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")

        self.horizontalLayout_42.addWidget(self.frameDropFiles_3)

        self.framePasteJson_3 = QFrame(self.frameJsonOptions_3)
        self.framePasteJson_3.setObjectName(u"framePasteJson_3")
        self.framePasteJson_3.setMinimumSize(QSize(350, 0))
        self.framePasteJson_3.setFrameShape(QFrame.StyledPanel)
        self.framePasteJson_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.framePasteJson_3)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frameJson_3 = QFrame(self.framePasteJson_3)
        self.frameJson_3.setObjectName(u"frameJson_3")
        self.frameJson_3.setFrameShape(QFrame.StyledPanel)
        self.frameJson_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frameJson_3)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.boxJsonLoader_3 = QPlainTextEdit(self.frameJson_3)
        self.boxJsonLoader_3.setObjectName(u"boxJsonLoader_3")
        sizePolicy2.setHeightForWidth(self.boxJsonLoader_3.sizePolicy().hasHeightForWidth())
        self.boxJsonLoader_3.setSizePolicy(sizePolicy2)
        self.boxJsonLoader_3.setAutoFillBackground(True)
        self.boxJsonLoader_3.setStyleSheet(u"")

        self.horizontalLayout_44.addWidget(self.boxJsonLoader_3)


        self.verticalLayout_16.addWidget(self.frameJson_3)

        self.frameUploadExisting_3 = QFrame(self.framePasteJson_3)
        self.frameUploadExisting_3.setObjectName(u"frameUploadExisting_3")
        self.frameUploadExisting_3.setFrameShape(QFrame.StyledPanel)
        self.frameUploadExisting_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frameUploadExisting_3)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.buttonUploadJson_3 = QPushButton(self.frameUploadExisting_3)
        self.buttonUploadJson_3.setObjectName(u"buttonUploadJson_3")
        sizePolicy3.setHeightForWidth(self.buttonUploadJson_3.sizePolicy().hasHeightForWidth())
        self.buttonUploadJson_3.setSizePolicy(sizePolicy3)

        self.horizontalLayout_45.addWidget(self.buttonUploadJson_3)

        self.buttonExistingJson_3 = QPushButton(self.frameUploadExisting_3)
        self.buttonExistingJson_3.setObjectName(u"buttonExistingJson_3")
        self.buttonExistingJson_3.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_45.addWidget(self.buttonExistingJson_3)


        self.verticalLayout_16.addWidget(self.frameUploadExisting_3)


        self.horizontalLayout_42.addWidget(self.framePasteJson_3)

        self.frameMenuImage_3 = QFrame(self.frameJsonOptions_3)
        self.frameMenuImage_3.setObjectName(u"frameMenuImage_3")
        self.frameMenuImage_3.setMinimumSize(QSize(250, 0))
        self.frameMenuImage_3.setSizeIncrement(QSize(0, 0))
        self.frameMenuImage_3.setStyleSheet(u"")
        self.frameMenuImage_3.setFrameShape(QFrame.Box)
        self.frameMenuImage_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frameMenuImage_3)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.LabelMenuImage_3 = QLabel(self.frameMenuImage_3)
        self.LabelMenuImage_3.setObjectName(u"LabelMenuImage_3")

        self.verticalLayout_17.addWidget(self.LabelMenuImage_3)

        self.menuImage_3 = QLabel(self.frameMenuImage_3)
        self.menuImage_3.setObjectName(u"menuImage_3")
        self.menuImage_3.setFrameShape(QFrame.Box)
        self.menuImage_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.menuImage_3)


        self.horizontalLayout_42.addWidget(self.frameMenuImage_3)

        self.frameLoadAll_3 = QFrame(self.frameJsonOptions_3)
        self.frameLoadAll_3.setObjectName(u"frameLoadAll_3")
        self.frameLoadAll_3.setFrameShape(QFrame.StyledPanel)
        self.frameLoadAll_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frameLoadAll_3)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer_5 = QSpacerItem(20, 134, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_5)

        self.buttonLoadAll_3 = QPushButton(self.frameLoadAll_3)
        self.buttonLoadAll_3.setObjectName(u"buttonLoadAll_3")
        self.buttonLoadAll_3.setMinimumSize(QSize(0, 35))

        self.verticalLayout_18.addWidget(self.buttonLoadAll_3)


        self.horizontalLayout_42.addWidget(self.frameLoadAll_3)


        self.verticalLayout_4.addWidget(self.frameJsonOptions_3)

        self.verticalSpacer_6 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.tabWidget.addTab(self.slot3, "")
        self.slot4 = QWidget()
        self.slot4.setObjectName(u"slot4")
        self.verticalLayout_5 = QVBoxLayout(self.slot4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frameHeader_4 = QFrame(self.slot4)
        self.frameHeader_4.setObjectName(u"frameHeader_4")
        self.frameHeader_4.setMinimumSize(QSize(0, 50))
        self.frameHeader_4.setMaximumSize(QSize(16777215, 50))
        self.frameHeader_4.setStyleSheet(u"")
        self.frameHeader_4.setFrameShape(QFrame.Box)
        self.frameHeader_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frameHeader_4)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.nameOfSlot_4 = QLabel(self.frameHeader_4)
        self.nameOfSlot_4.setObjectName(u"nameOfSlot_4")

        self.horizontalLayout_61.addWidget(self.nameOfSlot_4)

        self.horizontalSpacer_20 = QSpacerItem(944, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_20)


        self.verticalLayout_5.addWidget(self.frameHeader_4)

        self.frameMainTax_4 = QFrame(self.slot4)
        self.frameMainTax_4.setObjectName(u"frameMainTax_4")
        self.frameMainTax_4.setMinimumSize(QSize(0, 150))
        self.frameMainTax_4.setMaximumSize(QSize(16777215, 150))
        self.frameMainTax_4.setFrameShape(QFrame.StyledPanel)
        self.frameMainTax_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frameMainTax_4)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.frameTax_4 = QFrame(self.frameMainTax_4)
        self.frameTax_4.setObjectName(u"frameTax_4")
        self.frameTax_4.setMinimumSize(QSize(300, 0))
        self.frameTax_4.setMaximumSize(QSize(16777215, 150))
        self.frameTax_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frameTax_4.setFrameShape(QFrame.Box)
        self.frameTax_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frameTax_4)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.labelTaxFrame_4 = QLabel(self.frameTax_4)
        self.labelTaxFrame_4.setObjectName(u"labelTaxFrame_4")

        self.verticalLayout_23.addWidget(self.labelTaxFrame_4)

        self.frameTaxType_4 = QFrame(self.frameTax_4)
        self.frameTaxType_4.setObjectName(u"frameTaxType_4")
        self.frameTaxType_4.setMinimumSize(QSize(0, 25))
        self.frameTaxType_4.setFrameShape(QFrame.StyledPanel)
        self.frameTaxType_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frameTaxType_4)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.labelTaxType_4 = QLabel(self.frameTaxType_4)
        self.labelTaxType_4.setObjectName(u"labelTaxType_4")
        self.labelTaxType_4.setMinimumSize(QSize(150, 0))
        self.labelTaxType_4.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_57.addWidget(self.labelTaxType_4)

        self.labelTaxIncluded_4 = QLabel(self.frameTaxType_4)
        self.labelTaxIncluded_4.setObjectName(u"labelTaxIncluded_4")

        self.horizontalLayout_57.addWidget(self.labelTaxIncluded_4)


        self.verticalLayout_23.addWidget(self.frameTaxType_4)

        self.frameDisplayTax_4 = QFrame(self.frameTax_4)
        self.frameDisplayTax_4.setObjectName(u"frameDisplayTax_4")
        self.frameDisplayTax_4.setMinimumSize(QSize(0, 25))
        self.frameDisplayTax_4.setFrameShape(QFrame.StyledPanel)
        self.frameDisplayTax_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frameDisplayTax_4)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.labelDisplayTax_4 = QLabel(self.frameDisplayTax_4)
        self.labelDisplayTax_4.setObjectName(u"labelDisplayTax_4")
        self.labelDisplayTax_4.setMinimumSize(QSize(150, 0))
        self.labelDisplayTax_4.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_58.addWidget(self.labelDisplayTax_4)

        self.labelTrueFalseTax_4 = QLabel(self.frameDisplayTax_4)
        self.labelTrueFalseTax_4.setObjectName(u"labelTrueFalseTax_4")

        self.horizontalLayout_58.addWidget(self.labelTrueFalseTax_4)


        self.verticalLayout_23.addWidget(self.frameDisplayTax_4)

        self.frameNameNewTax_4 = QFrame(self.frameTax_4)
        self.frameNameNewTax_4.setObjectName(u"frameNameNewTax_4")
        self.frameNameNewTax_4.setMinimumSize(QSize(0, 25))
        self.frameNameNewTax_4.setFrameShape(QFrame.StyledPanel)
        self.frameNameNewTax_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frameNameNewTax_4)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.labelNewTax_4 = QLabel(self.frameNameNewTax_4)
        self.labelNewTax_4.setObjectName(u"labelNewTax_4")
        self.labelNewTax_4.setMinimumSize(QSize(150, 0))
        self.labelNewTax_4.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_59.addWidget(self.labelNewTax_4)

        self.labelPercentageNewTax_4 = QLabel(self.frameNameNewTax_4)
        self.labelPercentageNewTax_4.setObjectName(u"labelPercentageNewTax_4")
        self.labelPercentageNewTax_4.setMinimumSize(QSize(100, 0))
        self.labelPercentageNewTax_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_59.addWidget(self.labelPercentageNewTax_4)

        self.horizontalSpacer_17 = QSpacerItem(163, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_17)

        self.buttonRemoveTax_4 = QPushButton(self.frameNameNewTax_4)
        self.buttonRemoveTax_4.setObjectName(u"buttonRemoveTax_4")
        self.buttonRemoveTax_4.setMinimumSize(QSize(100, 0))
        self.buttonRemoveTax_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_59.addWidget(self.buttonRemoveTax_4)


        self.verticalLayout_23.addWidget(self.frameNameNewTax_4)

        self.frameButtonAddTax_4 = QFrame(self.frameTax_4)
        self.frameButtonAddTax_4.setObjectName(u"frameButtonAddTax_4")
        self.frameButtonAddTax_4.setMinimumSize(QSize(0, 25))
        self.frameButtonAddTax_4.setFrameShape(QFrame.StyledPanel)
        self.frameButtonAddTax_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frameButtonAddTax_4)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_18)

        self.buttonAddTax_4 = QPushButton(self.frameButtonAddTax_4)
        self.buttonAddTax_4.setObjectName(u"buttonAddTax_4")
        self.buttonAddTax_4.setMinimumSize(QSize(100, 0))
        self.buttonAddTax_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_60.addWidget(self.buttonAddTax_4, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_23.addWidget(self.frameButtonAddTax_4)


        self.horizontalLayout_56.addWidget(self.frameTax_4)

        self.horizontalSpacer_19 = QSpacerItem(536, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_19)


        self.verticalLayout_5.addWidget(self.frameMainTax_4)

        self.frameJsonOptions_4 = QFrame(self.slot4)
        self.frameJsonOptions_4.setObjectName(u"frameJsonOptions_4")
        sizePolicy.setHeightForWidth(self.frameJsonOptions_4.sizePolicy().hasHeightForWidth())
        self.frameJsonOptions_4.setSizePolicy(sizePolicy)
        self.frameJsonOptions_4.setMinimumSize(QSize(0, 50))
        self.frameJsonOptions_4.setMaximumSize(QSize(16777215, 200))
        self.frameJsonOptions_4.setFrameShape(QFrame.StyledPanel)
        self.frameJsonOptions_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frameJsonOptions_4)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frameDropFiles_4 = QFrame(self.frameJsonOptions_4)
        self.frameDropFiles_4.setObjectName(u"frameDropFiles_4")
        sizePolicy1.setHeightForWidth(self.frameDropFiles_4.sizePolicy().hasHeightForWidth())
        self.frameDropFiles_4.setSizePolicy(sizePolicy1)
        self.frameDropFiles_4.setMinimumSize(QSize(300, 0))
        self.frameDropFiles_4.setFrameShape(QFrame.StyledPanel)
        self.frameDropFiles_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frameDropFiles_4)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")

        self.horizontalLayout_52.addWidget(self.frameDropFiles_4)

        self.framePasteJson_4 = QFrame(self.frameJsonOptions_4)
        self.framePasteJson_4.setObjectName(u"framePasteJson_4")
        self.framePasteJson_4.setMinimumSize(QSize(350, 0))
        self.framePasteJson_4.setFrameShape(QFrame.StyledPanel)
        self.framePasteJson_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.framePasteJson_4)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frameJson_4 = QFrame(self.framePasteJson_4)
        self.frameJson_4.setObjectName(u"frameJson_4")
        self.frameJson_4.setFrameShape(QFrame.StyledPanel)
        self.frameJson_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frameJson_4)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.boxJsonLoader_4 = QPlainTextEdit(self.frameJson_4)
        self.boxJsonLoader_4.setObjectName(u"boxJsonLoader_4")
        sizePolicy2.setHeightForWidth(self.boxJsonLoader_4.sizePolicy().hasHeightForWidth())
        self.boxJsonLoader_4.setSizePolicy(sizePolicy2)
        self.boxJsonLoader_4.setAutoFillBackground(True)
        self.boxJsonLoader_4.setStyleSheet(u"")

        self.horizontalLayout_54.addWidget(self.boxJsonLoader_4)


        self.verticalLayout_20.addWidget(self.frameJson_4)

        self.frameUploadExisting_4 = QFrame(self.framePasteJson_4)
        self.frameUploadExisting_4.setObjectName(u"frameUploadExisting_4")
        self.frameUploadExisting_4.setFrameShape(QFrame.StyledPanel)
        self.frameUploadExisting_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frameUploadExisting_4)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.buttonUploadJson_4 = QPushButton(self.frameUploadExisting_4)
        self.buttonUploadJson_4.setObjectName(u"buttonUploadJson_4")
        sizePolicy3.setHeightForWidth(self.buttonUploadJson_4.sizePolicy().hasHeightForWidth())
        self.buttonUploadJson_4.setSizePolicy(sizePolicy3)

        self.horizontalLayout_55.addWidget(self.buttonUploadJson_4)

        self.buttonExistingJson_4 = QPushButton(self.frameUploadExisting_4)
        self.buttonExistingJson_4.setObjectName(u"buttonExistingJson_4")
        self.buttonExistingJson_4.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_55.addWidget(self.buttonExistingJson_4)


        self.verticalLayout_20.addWidget(self.frameUploadExisting_4)


        self.horizontalLayout_52.addWidget(self.framePasteJson_4)

        self.frameMenuImage_4 = QFrame(self.frameJsonOptions_4)
        self.frameMenuImage_4.setObjectName(u"frameMenuImage_4")
        self.frameMenuImage_4.setMinimumSize(QSize(250, 0))
        self.frameMenuImage_4.setSizeIncrement(QSize(0, 0))
        self.frameMenuImage_4.setStyleSheet(u"")
        self.frameMenuImage_4.setFrameShape(QFrame.Box)
        self.frameMenuImage_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frameMenuImage_4)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.LabelMenuImage_4 = QLabel(self.frameMenuImage_4)
        self.LabelMenuImage_4.setObjectName(u"LabelMenuImage_4")

        self.verticalLayout_21.addWidget(self.LabelMenuImage_4)

        self.menuImage_4 = QLabel(self.frameMenuImage_4)
        self.menuImage_4.setObjectName(u"menuImage_4")
        self.menuImage_4.setFrameShape(QFrame.Box)
        self.menuImage_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.menuImage_4)


        self.horizontalLayout_52.addWidget(self.frameMenuImage_4)

        self.frameLoadAll_4 = QFrame(self.frameJsonOptions_4)
        self.frameLoadAll_4.setObjectName(u"frameLoadAll_4")
        self.frameLoadAll_4.setFrameShape(QFrame.StyledPanel)
        self.frameLoadAll_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frameLoadAll_4)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalSpacer_7 = QSpacerItem(20, 134, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_7)

        self.buttonLoadAll_4 = QPushButton(self.frameLoadAll_4)
        self.buttonLoadAll_4.setObjectName(u"buttonLoadAll_4")
        self.buttonLoadAll_4.setMinimumSize(QSize(0, 35))

        self.verticalLayout_22.addWidget(self.buttonLoadAll_4)


        self.horizontalLayout_52.addWidget(self.frameLoadAll_4)


        self.verticalLayout_5.addWidget(self.frameJsonOptions_4)

        self.verticalSpacer_8 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)

        self.tabWidget.addTab(self.slot4, "")
        self.slot5 = QWidget()
        self.slot5.setObjectName(u"slot5")
        self.verticalLayout_6 = QVBoxLayout(self.slot5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frameHeader_5 = QFrame(self.slot5)
        self.frameHeader_5.setObjectName(u"frameHeader_5")
        self.frameHeader_5.setMinimumSize(QSize(0, 50))
        self.frameHeader_5.setMaximumSize(QSize(16777215, 50))
        self.frameHeader_5.setStyleSheet(u"")
        self.frameHeader_5.setFrameShape(QFrame.Box)
        self.frameHeader_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frameHeader_5)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.nameOfSlot_5 = QLabel(self.frameHeader_5)
        self.nameOfSlot_5.setObjectName(u"nameOfSlot_5")

        self.horizontalLayout_71.addWidget(self.nameOfSlot_5)

        self.horizontalSpacer_24 = QSpacerItem(944, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_71.addItem(self.horizontalSpacer_24)


        self.verticalLayout_6.addWidget(self.frameHeader_5)

        self.frameMainTax_5 = QFrame(self.slot5)
        self.frameMainTax_5.setObjectName(u"frameMainTax_5")
        self.frameMainTax_5.setMinimumSize(QSize(0, 150))
        self.frameMainTax_5.setMaximumSize(QSize(16777215, 150))
        self.frameMainTax_5.setFrameShape(QFrame.StyledPanel)
        self.frameMainTax_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frameMainTax_5)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frameTax_5 = QFrame(self.frameMainTax_5)
        self.frameTax_5.setObjectName(u"frameTax_5")
        self.frameTax_5.setMinimumSize(QSize(300, 0))
        self.frameTax_5.setMaximumSize(QSize(16777215, 150))
        self.frameTax_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frameTax_5.setFrameShape(QFrame.Box)
        self.frameTax_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frameTax_5)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.labelTaxFrame_5 = QLabel(self.frameTax_5)
        self.labelTaxFrame_5.setObjectName(u"labelTaxFrame_5")

        self.verticalLayout_27.addWidget(self.labelTaxFrame_5)

        self.frameTaxType_5 = QFrame(self.frameTax_5)
        self.frameTaxType_5.setObjectName(u"frameTaxType_5")
        self.frameTaxType_5.setMinimumSize(QSize(0, 25))
        self.frameTaxType_5.setFrameShape(QFrame.StyledPanel)
        self.frameTaxType_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frameTaxType_5)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.labelTaxType_5 = QLabel(self.frameTaxType_5)
        self.labelTaxType_5.setObjectName(u"labelTaxType_5")
        self.labelTaxType_5.setMinimumSize(QSize(150, 0))
        self.labelTaxType_5.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_67.addWidget(self.labelTaxType_5)

        self.labelTaxIncluded_5 = QLabel(self.frameTaxType_5)
        self.labelTaxIncluded_5.setObjectName(u"labelTaxIncluded_5")

        self.horizontalLayout_67.addWidget(self.labelTaxIncluded_5)


        self.verticalLayout_27.addWidget(self.frameTaxType_5)

        self.frameDisplayTax_5 = QFrame(self.frameTax_5)
        self.frameDisplayTax_5.setObjectName(u"frameDisplayTax_5")
        self.frameDisplayTax_5.setMinimumSize(QSize(0, 25))
        self.frameDisplayTax_5.setFrameShape(QFrame.StyledPanel)
        self.frameDisplayTax_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frameDisplayTax_5)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.labelDisplayTax_5 = QLabel(self.frameDisplayTax_5)
        self.labelDisplayTax_5.setObjectName(u"labelDisplayTax_5")
        self.labelDisplayTax_5.setMinimumSize(QSize(150, 0))
        self.labelDisplayTax_5.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_68.addWidget(self.labelDisplayTax_5)

        self.labelTrueFalseTax_5 = QLabel(self.frameDisplayTax_5)
        self.labelTrueFalseTax_5.setObjectName(u"labelTrueFalseTax_5")

        self.horizontalLayout_68.addWidget(self.labelTrueFalseTax_5)


        self.verticalLayout_27.addWidget(self.frameDisplayTax_5)

        self.frameNameNewTax_5 = QFrame(self.frameTax_5)
        self.frameNameNewTax_5.setObjectName(u"frameNameNewTax_5")
        self.frameNameNewTax_5.setMinimumSize(QSize(0, 25))
        self.frameNameNewTax_5.setFrameShape(QFrame.StyledPanel)
        self.frameNameNewTax_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frameNameNewTax_5)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.labelNewTax_5 = QLabel(self.frameNameNewTax_5)
        self.labelNewTax_5.setObjectName(u"labelNewTax_5")
        self.labelNewTax_5.setMinimumSize(QSize(150, 0))
        self.labelNewTax_5.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_69.addWidget(self.labelNewTax_5)

        self.labelPercentageNewTax_5 = QLabel(self.frameNameNewTax_5)
        self.labelPercentageNewTax_5.setObjectName(u"labelPercentageNewTax_5")
        self.labelPercentageNewTax_5.setMinimumSize(QSize(100, 0))
        self.labelPercentageNewTax_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_69.addWidget(self.labelPercentageNewTax_5)

        self.horizontalSpacer_21 = QSpacerItem(163, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer_21)

        self.buttonRemoveTax_5 = QPushButton(self.frameNameNewTax_5)
        self.buttonRemoveTax_5.setObjectName(u"buttonRemoveTax_5")
        self.buttonRemoveTax_5.setMinimumSize(QSize(100, 0))
        self.buttonRemoveTax_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_69.addWidget(self.buttonRemoveTax_5)


        self.verticalLayout_27.addWidget(self.frameNameNewTax_5)

        self.frameButtonAddTax_5 = QFrame(self.frameTax_5)
        self.frameButtonAddTax_5.setObjectName(u"frameButtonAddTax_5")
        self.frameButtonAddTax_5.setMinimumSize(QSize(0, 25))
        self.frameButtonAddTax_5.setFrameShape(QFrame.StyledPanel)
        self.frameButtonAddTax_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frameButtonAddTax_5)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_22)

        self.buttonAddTax_5 = QPushButton(self.frameButtonAddTax_5)
        self.buttonAddTax_5.setObjectName(u"buttonAddTax_5")
        self.buttonAddTax_5.setMinimumSize(QSize(100, 0))
        self.buttonAddTax_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_70.addWidget(self.buttonAddTax_5, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_27.addWidget(self.frameButtonAddTax_5)


        self.horizontalLayout_66.addWidget(self.frameTax_5)

        self.horizontalSpacer_23 = QSpacerItem(536, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_23)


        self.verticalLayout_6.addWidget(self.frameMainTax_5)

        self.frameJsonOptions_5 = QFrame(self.slot5)
        self.frameJsonOptions_5.setObjectName(u"frameJsonOptions_5")
        sizePolicy.setHeightForWidth(self.frameJsonOptions_5.sizePolicy().hasHeightForWidth())
        self.frameJsonOptions_5.setSizePolicy(sizePolicy)
        self.frameJsonOptions_5.setMinimumSize(QSize(0, 50))
        self.frameJsonOptions_5.setMaximumSize(QSize(16777215, 200))
        self.frameJsonOptions_5.setFrameShape(QFrame.StyledPanel)
        self.frameJsonOptions_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frameJsonOptions_5)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.frameDropFiles_5 = QFrame(self.frameJsonOptions_5)
        self.frameDropFiles_5.setObjectName(u"frameDropFiles_5")
        sizePolicy1.setHeightForWidth(self.frameDropFiles_5.sizePolicy().hasHeightForWidth())
        self.frameDropFiles_5.setSizePolicy(sizePolicy1)
        self.frameDropFiles_5.setMinimumSize(QSize(300, 0))
        self.frameDropFiles_5.setFrameShape(QFrame.StyledPanel)
        self.frameDropFiles_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frameDropFiles_5)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")

        self.horizontalLayout_62.addWidget(self.frameDropFiles_5)

        self.framePasteJson_5 = QFrame(self.frameJsonOptions_5)
        self.framePasteJson_5.setObjectName(u"framePasteJson_5")
        self.framePasteJson_5.setMinimumSize(QSize(350, 0))
        self.framePasteJson_5.setFrameShape(QFrame.StyledPanel)
        self.framePasteJson_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.framePasteJson_5)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frameJson_5 = QFrame(self.framePasteJson_5)
        self.frameJson_5.setObjectName(u"frameJson_5")
        self.frameJson_5.setFrameShape(QFrame.StyledPanel)
        self.frameJson_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frameJson_5)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.boxJsonLoader_5 = QPlainTextEdit(self.frameJson_5)
        self.boxJsonLoader_5.setObjectName(u"boxJsonLoader_5")
        sizePolicy2.setHeightForWidth(self.boxJsonLoader_5.sizePolicy().hasHeightForWidth())
        self.boxJsonLoader_5.setSizePolicy(sizePolicy2)
        self.boxJsonLoader_5.setAutoFillBackground(True)
        self.boxJsonLoader_5.setStyleSheet(u"")

        self.horizontalLayout_64.addWidget(self.boxJsonLoader_5)


        self.verticalLayout_24.addWidget(self.frameJson_5)

        self.frameUploadExisting_5 = QFrame(self.framePasteJson_5)
        self.frameUploadExisting_5.setObjectName(u"frameUploadExisting_5")
        self.frameUploadExisting_5.setFrameShape(QFrame.StyledPanel)
        self.frameUploadExisting_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frameUploadExisting_5)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.buttonUploadJson_5 = QPushButton(self.frameUploadExisting_5)
        self.buttonUploadJson_5.setObjectName(u"buttonUploadJson_5")
        sizePolicy3.setHeightForWidth(self.buttonUploadJson_5.sizePolicy().hasHeightForWidth())
        self.buttonUploadJson_5.setSizePolicy(sizePolicy3)

        self.horizontalLayout_65.addWidget(self.buttonUploadJson_5)

        self.buttonExistingJson_5 = QPushButton(self.frameUploadExisting_5)
        self.buttonExistingJson_5.setObjectName(u"buttonExistingJson_5")
        self.buttonExistingJson_5.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_65.addWidget(self.buttonExistingJson_5)


        self.verticalLayout_24.addWidget(self.frameUploadExisting_5)


        self.horizontalLayout_62.addWidget(self.framePasteJson_5)

        self.frameMenuImage_5 = QFrame(self.frameJsonOptions_5)
        self.frameMenuImage_5.setObjectName(u"frameMenuImage_5")
        self.frameMenuImage_5.setMinimumSize(QSize(250, 0))
        self.frameMenuImage_5.setSizeIncrement(QSize(0, 0))
        self.frameMenuImage_5.setStyleSheet(u"")
        self.frameMenuImage_5.setFrameShape(QFrame.Box)
        self.frameMenuImage_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frameMenuImage_5)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.LabelMenuImage_5 = QLabel(self.frameMenuImage_5)
        self.LabelMenuImage_5.setObjectName(u"LabelMenuImage_5")

        self.verticalLayout_25.addWidget(self.LabelMenuImage_5)

        self.menuImage_5 = QLabel(self.frameMenuImage_5)
        self.menuImage_5.setObjectName(u"menuImage_5")
        self.menuImage_5.setFrameShape(QFrame.Box)
        self.menuImage_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.menuImage_5)


        self.horizontalLayout_62.addWidget(self.frameMenuImage_5)

        self.frameLoadAll_5 = QFrame(self.frameJsonOptions_5)
        self.frameLoadAll_5.setObjectName(u"frameLoadAll_5")
        self.frameLoadAll_5.setFrameShape(QFrame.StyledPanel)
        self.frameLoadAll_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frameLoadAll_5)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSpacer_9 = QSpacerItem(20, 134, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_9)

        self.buttonLoadAll_5 = QPushButton(self.frameLoadAll_5)
        self.buttonLoadAll_5.setObjectName(u"buttonLoadAll_5")
        self.buttonLoadAll_5.setMinimumSize(QSize(0, 35))

        self.verticalLayout_26.addWidget(self.buttonLoadAll_5)


        self.horizontalLayout_62.addWidget(self.frameLoadAll_5)


        self.verticalLayout_6.addWidget(self.frameJsonOptions_5)

        self.verticalSpacer_10 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_10)

        self.tabWidget.addTab(self.slot5, "")

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

        self.tabWidget.setCurrentIndex(4)


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
        self.buttonUploadJson_2.setText(QCoreApplication.translate("MainWindow", u"UPLOAD JSON", None))
        self.buttonExistingJson_2.setText(QCoreApplication.translate("MainWindow", u"EXISTING JSON", None))
        self.LabelMenuImage_2.setText(QCoreApplication.translate("MainWindow", u"MENU IMAGE", None))
        self.menuImage_2.setText(QCoreApplication.translate("MainWindow", u"IMAGE", None))
        self.buttonLoadAll_2.setText(QCoreApplication.translate("MainWindow", u"LOAD ALL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.slot2), QCoreApplication.translate("MainWindow", u"Slot 2", None))
        self.nameOfSlot_3.setText(QCoreApplication.translate("MainWindow", u"NAME OF THE SLOT", None))
        self.labelTaxFrame_3.setText(QCoreApplication.translate("MainWindow", u"Tax Rates", None))
        self.labelTaxType_3.setText(QCoreApplication.translate("MainWindow", u"Tax Type:", None))
        self.labelTaxIncluded_3.setText(QCoreApplication.translate("MainWindow", u"IncludedInBasePrice", None))
        self.labelDisplayTax_3.setText(QCoreApplication.translate("MainWindow", u"Display Tax:", None))
        self.labelTrueFalseTax_3.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.labelNewTax_3.setText(QCoreApplication.translate("MainWindow", u"Name of New Tax", None))
        self.labelPercentageNewTax_3.setText(QCoreApplication.translate("MainWindow", u"6.000%", None))
        self.buttonRemoveTax_3.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        self.buttonAddTax_3.setText(QCoreApplication.translate("MainWindow", u"ADD NEW", None))
        self.buttonUploadJson_3.setText(QCoreApplication.translate("MainWindow", u"UPLOAD JSON", None))
        self.buttonExistingJson_3.setText(QCoreApplication.translate("MainWindow", u"EXISTING JSON", None))
        self.LabelMenuImage_3.setText(QCoreApplication.translate("MainWindow", u"MENU IMAGE", None))
        self.menuImage_3.setText(QCoreApplication.translate("MainWindow", u"IMAGE", None))
        self.buttonLoadAll_3.setText(QCoreApplication.translate("MainWindow", u"LOAD ALL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.slot3), QCoreApplication.translate("MainWindow", u"Slot 3", None))
        self.nameOfSlot_4.setText(QCoreApplication.translate("MainWindow", u"NAME OF THE SLOT", None))
        self.labelTaxFrame_4.setText(QCoreApplication.translate("MainWindow", u"Tax Rates", None))
        self.labelTaxType_4.setText(QCoreApplication.translate("MainWindow", u"Tax Type:", None))
        self.labelTaxIncluded_4.setText(QCoreApplication.translate("MainWindow", u"IncludedInBasePrice", None))
        self.labelDisplayTax_4.setText(QCoreApplication.translate("MainWindow", u"Display Tax:", None))
        self.labelTrueFalseTax_4.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.labelNewTax_4.setText(QCoreApplication.translate("MainWindow", u"Name of New Tax", None))
        self.labelPercentageNewTax_4.setText(QCoreApplication.translate("MainWindow", u"6.000%", None))
        self.buttonRemoveTax_4.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        self.buttonAddTax_4.setText(QCoreApplication.translate("MainWindow", u"ADD NEW", None))
        self.buttonUploadJson_4.setText(QCoreApplication.translate("MainWindow", u"UPLOAD JSON", None))
        self.buttonExistingJson_4.setText(QCoreApplication.translate("MainWindow", u"EXISTING JSON", None))
        self.LabelMenuImage_4.setText(QCoreApplication.translate("MainWindow", u"MENU IMAGE", None))
        self.menuImage_4.setText(QCoreApplication.translate("MainWindow", u"IMAGE", None))
        self.buttonLoadAll_4.setText(QCoreApplication.translate("MainWindow", u"LOAD ALL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.slot4), QCoreApplication.translate("MainWindow", u"P\u00e1gina", None))
        self.nameOfSlot_5.setText(QCoreApplication.translate("MainWindow", u"NAME OF THE SLOT", None))
        self.labelTaxFrame_5.setText(QCoreApplication.translate("MainWindow", u"Tax Rates", None))
        self.labelTaxType_5.setText(QCoreApplication.translate("MainWindow", u"Tax Type:", None))
        self.labelTaxIncluded_5.setText(QCoreApplication.translate("MainWindow", u"IncludedInBasePrice", None))
        self.labelDisplayTax_5.setText(QCoreApplication.translate("MainWindow", u"Display Tax:", None))
        self.labelTrueFalseTax_5.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.labelNewTax_5.setText(QCoreApplication.translate("MainWindow", u"Name of New Tax", None))
        self.labelPercentageNewTax_5.setText(QCoreApplication.translate("MainWindow", u"6.000%", None))
        self.buttonRemoveTax_5.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        self.buttonAddTax_5.setText(QCoreApplication.translate("MainWindow", u"ADD NEW", None))
        self.buttonUploadJson_5.setText(QCoreApplication.translate("MainWindow", u"UPLOAD JSON", None))
        self.buttonExistingJson_5.setText(QCoreApplication.translate("MainWindow", u"EXISTING JSON", None))
        self.LabelMenuImage_5.setText(QCoreApplication.translate("MainWindow", u"MENU IMAGE", None))
        self.menuImage_5.setText(QCoreApplication.translate("MainWindow", u"IMAGE", None))
        self.buttonLoadAll_5.setText(QCoreApplication.translate("MainWindow", u"LOAD ALL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.slot5), QCoreApplication.translate("MainWindow", u"P\u00e1gina", None))
        self.menuOME.setTitle(QCoreApplication.translate("MainWindow", u"OME", None))
    # retranslateUi

