# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(681, 419)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 651, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.manga_site = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.manga_site.setObjectName("manga_site")
        self.manga_site.addItem("")
        self.manga_site.setItemText(0, "")
        self.manga_site.addItem("")
        self.manga_site.addItem("")
        self.manga_site.addItem("")
        self.horizontalLayout.addWidget(self.manga_site)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.manga_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manga_name.sizePolicy().hasHeightForWidth())
        self.manga_name.setSizePolicy(sizePolicy)
        self.manga_name.setObjectName("manga_name")
        self.horizontalLayout.addWidget(self.manga_name)
        self.fetch_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fetch_button.sizePolicy().hasHeightForWidth())
        self.fetch_button.setSizePolicy(sizePolicy)
        self.fetch_button.setObjectName("fetch_button")
        self.horizontalLayout.addWidget(self.fetch_button)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 110, 241, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.chapters = QtWidgets.QLabel(self.gridLayoutWidget)
        self.chapters.setObjectName("chapters")
        self.gridLayout.addWidget(self.chapters, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 150, 241, 31))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.pages = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.pages.setObjectName("pages")
        self.gridLayout_3.addWidget(self.pages, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 230, 211, 29))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.output_format = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_format.sizePolicy().hasHeightForWidth())
        self.output_format.setSizePolicy(sizePolicy)
        self.output_format.setObjectName("output_format")
        self.output_format.addItem("")
        self.output_format.addItem("")
        self.output_format.addItem("")
        self.horizontalLayout_2.addWidget(self.output_format)
        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_button.setEnabled(False)
        self.download_button.setGeometry(QtCore.QRect(570, 230, 99, 27))
        self.download_button.setObjectName("download_button")
        self.total_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.total_bar.setGeometry(QtCore.QRect(20, 310, 651, 23))
        self.total_bar.setProperty("value", 0)
        self.total_bar.setObjectName("total_bar")
        self.chapter_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.chapter_bar.setGeometry(QtCore.QRect(20, 370, 651, 23))
        self.chapter_bar.setProperty("value", 0)
        self.chapter_bar.setObjectName("chapter_bar")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 280, 131, 31))
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 340, 131, 31))
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 80, 591, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 260, 621, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(170, 10, 361, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Fumetti Scraper Gui"))
        self.manga_site.setItemText(1, _translate("mainWindow", "www.mangaeden.com/en/en-manga"))
        self.manga_site.setItemText(2, _translate("mainWindow", "www.mangaeden.com/it/it-manga"))
        self.manga_site.setItemText(3, _translate("mainWindow", "www.mangareader.net"))
        self.label.setText(_translate("mainWindow", "/"))
        self.fetch_button.setText(_translate("mainWindow", "Fetch"))
        self.label_2.setText(_translate("mainWindow", "1) Fetch Manga Url"))
        self.label_3.setText(_translate("mainWindow", "Chapters: "))
        self.chapters.setText(_translate("mainWindow", "?"))
        self.label_7.setText(_translate("mainWindow", "Total Pages:"))
        self.pages.setText(_translate("mainWindow", "?"))
        self.label_4.setText(_translate("mainWindow", "2) Download Manga"))
        self.label_6.setText(_translate("mainWindow", "Output Format"))
        self.output_format.setItemText(0, _translate("mainWindow", "pdf"))
        self.output_format.setItemText(1, _translate("mainWindow", "cbr"))
        self.output_format.setItemText(2, _translate("mainWindow", "jpg"))
        self.download_button.setText(_translate("mainWindow", "Download"))
        self.label_8.setText(_translate("mainWindow", "Total"))
        self.label_9.setText(_translate("mainWindow", "Current Chapter"))
        self.label_5.setText(_translate("mainWindow", "the window could become \"not responding\", don\'t close it, let it fetch data in background"))
        self.label_10.setText(_translate("mainWindow", "the window could become \"not responding\", don\'t close it, let it download data in background"))
        self.label_11.setText(_translate("mainWindow", "select the site page with chapters list"))

