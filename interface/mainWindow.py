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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
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
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.values = QTableWidget(self.centralwidget)
        if (self.values.columnCount() < 1):
            self.values.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.values.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.values.rowCount() < 10):
            self.values.setRowCount(10)
        self.values.setObjectName(u"values")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.values.sizePolicy().hasHeightForWidth())
        self.values.setSizePolicy(sizePolicy)
        self.values.setRowCount(10)

        self.verticalLayout.addWidget(self.values)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.amount_of_values_to_change = QLineEdit(self.centralwidget)
        self.amount_of_values_to_change.setObjectName(u"amount_of_values_to_change")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.amount_of_values_to_change.sizePolicy().hasHeightForWidth())
        self.amount_of_values_to_change.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.amount_of_values_to_change)

        self.change_amount_of_values = QPushButton(self.centralwidget)
        self.change_amount_of_values.setObjectName(u"change_amount_of_values")

        self.horizontalLayout_2.addWidget(self.change_amount_of_values)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.console = QTextEdit(self.centralwidget)
        self.console.setObjectName(u"console")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy2)
        self.console.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.console)

        self.generate = QPushButton(self.centralwidget)
        self.generate.setObjectName(u"generate")

        self.verticalLayout_4.addWidget(self.generate)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.instrument_error = QLineEdit(self.centralwidget)
        self.instrument_error.setObjectName(u"instrument_error")

        self.gridLayout.addWidget(self.instrument_error, 0, 1, 1, 1)

        self.symbol = QLineEdit(self.centralwidget)
        self.symbol.setObjectName(u"symbol")

        self.gridLayout.addWidget(self.symbol, 1, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.generate_docx = QPushButton(self.centralwidget)
        self.generate_docx.setObjectName(u"generate_docx")

        self.verticalLayout_4.addWidget(self.generate_docx)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PhysicsLabTools", None))
        ___qtablewidgetitem = self.values.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Values", None));
        self.change_amount_of_values.setText(QCoreApplication.translate("MainWindow", u"Change amount of values", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Instrument error :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Symbol :", None))
        self.generate_docx.setText(QCoreApplication.translate("MainWindow", u"Generate .docx", None))
    # retranslateUi

