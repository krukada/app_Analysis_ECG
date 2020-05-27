
from PyQt5 import QtCore, QtWidgets


class TotalAnalysisView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Total Full Analysis ECG")
        MainWindow.resize(841, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 221, 21))
        self.label.setObjectName("label")
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(50, 70, 731, 291))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 841, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Total Full Analysis ECG")
        self.label.setText("Заключение полного анализа ЭКГ")
