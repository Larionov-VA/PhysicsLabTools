# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(827, 640)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.value_1 = QLineEdit(self.centralwidget)
        self.value_1.setObjectName(u"value_1")

        self.gridLayout.addWidget(self.value_1, 1, 0, 1, 1)

        self.value_3 = QLineEdit(self.centralwidget)
        self.value_3.setObjectName(u"value_3")

        self.gridLayout.addWidget(self.value_3, 1, 2, 1, 1)

        self.value_2 = QLineEdit(self.centralwidget)
        self.value_2.setObjectName(u"value_2")

        self.gridLayout.addWidget(self.value_2, 1, 1, 1, 1)

        self.value_4 = QLineEdit(self.centralwidget)
        self.value_4.setObjectName(u"value_4")

        self.gridLayout.addWidget(self.value_4, 1, 3, 1, 1)

        self.value_5 = QLineEdit(self.centralwidget)
        self.value_5.setObjectName(u"value_5")

        self.gridLayout.addWidget(self.value_5, 1, 4, 1, 1)

        self.text_1 = QLabel(self.centralwidget)
        self.text_1.setObjectName(u"text_1")

        self.gridLayout.addWidget(self.text_1, 0, 0, 1, 1)

        self.text_2 = QLabel(self.centralwidget)
        self.text_2.setObjectName(u"text_2")

        self.gridLayout.addWidget(self.text_2, 0, 1, 1, 1)

        self.text_3 = QLabel(self.centralwidget)
        self.text_3.setObjectName(u"text_3")

        self.gridLayout.addWidget(self.text_3, 0, 2, 1, 1)

        self.text_4 = QLabel(self.centralwidget)
        self.text_4.setObjectName(u"text_4")

        self.gridLayout.addWidget(self.text_4, 0, 3, 1, 1)

        self.text_5 = QLabel(self.centralwidget)
        self.text_5.setObjectName(u"text_5")

        self.gridLayout.addWidget(self.text_5, 0, 4, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.console = QTextEdit(self.centralwidget)
        self.console.setObjectName(u"console")

        self.verticalLayout_3.addWidget(self.console)

        self.status = QLabel(self.centralwidget)
        self.status.setObjectName(u"status")

        self.verticalLayout_3.addWidget(self.status)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 827, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.text_1.setText(QCoreApplication.translate("MainWindow", u"Value 1", None))
        self.text_2.setText(QCoreApplication.translate("MainWindow", u"Value 2", None))
        self.text_3.setText(QCoreApplication.translate("MainWindow", u"Value 3", None))
        self.text_4.setText(QCoreApplication.translate("MainWindow", u"Value 4", None))
        self.text_5.setText(QCoreApplication.translate("MainWindow", u"Value 5", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate answer", None))
        self.console.setPlaceholderText("")
        self.status.setText("")
    # retranslateUi

