from PyQt5 import QtCore, QtWidgets


class RegistrationView(object):
    def setupUi(self, window):
        window.setObjectName('Analysis ECG')
        window.resize(737, 274)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.go_to_analys = QtWidgets.QPushButton(self.centralwidget)
        self.go_to_analys.setGeometry(QtCore.QRect(500, 80, 141, 41))
        self.go_to_analys.setObjectName("go to analysys")
        self.patient = QtWidgets.QLabel(self.centralwidget)
        self.patient.setGeometry(QtCore.QRect(70, 90, 101, 16))
        self.patient.setObjectName("Patient")
        self.massPatient = QtWidgets.QComboBox(self.centralwidget)
        self.massPatient.setGeometry(QtCore.QRect(180, 80, 301, 41))
        self.massPatient.setObjectName("Patient mass")
        self.help_head = QtWidgets.QLabel(self.centralwidget)
        self.help_head.setGeometry(QtCore.QRect(200, 0, 331, 71))
        self.help_head.setObjectName("text heading")
        self.help_text = QtWidgets.QLabel(self.centralwidget)
        self.help_text.setGeometry(QtCore.QRect(170, 130, 341, 16))
        self.help_text.setObjectName("text help")
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 22))
        window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window)
        window.setStatusBar(self.statusbar)

        self.setText(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def setText(self, window):
        window.setWindowTitle("Analysis ECG")
        self.go_to_analys.setText("Применить")
        self.patient.setText("Пациент ECG: ")
        self.help_head.setText("Получить полный Анализ ЭКГ пациента")
        self.help_text.setText("  Bыберите одного пациента и нажмите применить")
