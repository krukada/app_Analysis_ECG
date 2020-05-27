from PyQt5 import QtCore, QtWidgets

from pyqtgraph import GraphicsLayoutWidget, PlotWidget
import pyqtgraph as pg

pg.mkPen(color=(200, 200, 255), style=QtCore.Qt.DotLine)


class AnalysisView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 878)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 201, 21))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 271, 16))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 181, 16))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 70, 191, 20))
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 110, 261, 20))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 150, 261, 20))

        self.M = QtWidgets.QTextEdit(self.centralwidget)
        self.M.setGeometry(QtCore.QRect(205, 68, 191, 31))

        self.sco = QtWidgets.QTextEdit(self.centralwidget)
        self.sco.setGeometry(QtCore.QRect(280, 110, 191, 31))

        self.v = QtWidgets.QTextEdit(self.centralwidget)
        self.v.setGeometry(QtCore.QRect(190, 150, 191, 31))

        self.delta_x = QtWidgets.QTextEdit(self.centralwidget)
        self.delta_x.setGeometry(QtCore.QRect(730, 145, 191, 31))

        self.mo = QtWidgets.QTextEdit(self.centralwidget)
        self.mo.setGeometry(QtCore.QRect(700, 65, 191, 31))

        self.A_mo = QtWidgets.QTextEdit(self.centralwidget)
        self.A_mo.setGeometry(QtCore.QRect(780, 105, 191, 31))

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 241, 20))

        self.person = QtWidgets.QTextEdit(self.centralwidget)
        self.person.setGeometry(QtCore.QRect(260, 15, 191, 31))

        self.VPR = QtWidgets.QTextEdit(self.centralwidget)
        self.VPR.setGeometry(QtCore.QRect(1170, 55, 191, 31))

        self.INB = QtWidgets.QTextEdit(self.centralwidget)
        self.INB.setGeometry(QtCore.QRect(1200, 135, 191, 31))

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(910, 60, 261, 20))
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 200, 371, 16))
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(980, 100, 271, 20))

        self.IVR = QtWidgets.QTextEdit(self.centralwidget)
        self.IVR.setGeometry(QtCore.QRect(1250, 95, 181, 31))

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(510, 20, 60, 16))

        self.sex = QtWidgets.QTextEdit(self.centralwidget)
        self.sex.setGeometry(QtCore.QRect(550, 15, 101, 31))

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(666, 20, 62, 16))

        self.age = QtWidgets.QTextEdit(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(740, 15, 101, 31))

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(850, 20, 71, 20))

        self.data = QtWidgets.QTextEdit(self.centralwidget)
        self.data.setGeometry(QtCore.QRect(920, 15, 191, 31))

        self.PAPR = QtWidgets.QTextEdit(self.centralwidget)
        self.PAPR.setGeometry(QtCore.QRect(380, 190, 191, 31))

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(950, 140, 261, 20))
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(600, 190, 141, 20))

        self.bpm = QtWidgets.QTextEdit(self.centralwidget)
        self.bpm.setGeometry(QtCore.QRect(730, 185, 199, 31))

        self.ecg = PlotWidget(self.centralwidget)
        self.ecg.setGeometry(QtCore.QRect(10, 250, 1411, 141))

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(600, 220, 71, 31))

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(530, 400, 171, 20))

        self.filter_ecg = PlotWidget(self.centralwidget)
        self.filter_ecg.setGeometry(QtCore.QRect(10, 420, 1411, 161))

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(550, 580, 211, 21))

        self.QRS_view = PlotWidget(self.centralwidget)
        self.QRS_view.setGeometry(QtCore.QRect(10, 612, 1411, 161))

        self.full_analysis = QtWidgets.QPushButton(self.centralwidget)
        self.full_analysis.setGeometry(QtCore.QRect(460, 780, 341, 61))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(" Full Analysis ECG")
        self.label.setText("Мат.ожидание RR зубцов (M): ")
        self.label_2.setText("Среднеквадратичное отклоднение(СКО):")
        self.label_3.setText("Коэффициент вариации V :")
        self.label_4.setText("Мода распределения (m0):")
        self.label_5.setText("Амплитуда моды распределения (Am0):")
        self.label_6.setText("Вариационный размах (delta X): ")
        self.label_7.setText("Результаты показателей ЭКГ для :")
        self.label_8.setText("Вегетатичный показатель ритма (ВПР):")
        self.label_9.setText("Показатель адекватности процессов регуляции(ПАПР):")
        self.label_10.setText("Индекс вегетатичного ровновесия (ИВР):")
        self.label_11.setText("Пол:")
        self.label_12.setText("Возраст:")
        self.label_13.setText("Дата ЭКГ:")
        self.label_14.setText("Индекс напряжения Баевского(ИНБ):")
        self.label_15.setText("Сердечный ритм:")
        self.label_16.setText("ЭКГ")
        self.label_17.setText("Двойная фильтрация ЭКГ")
        self.label_18.setText("QRS зубцы ЭКГ")
        self.full_analysis.setText("Получить заключение полного анализа ЭКГ")
