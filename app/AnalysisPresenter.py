from PyQt5 import QtCore, QtWidgets
from app.AnalysisECG import AnalysisView
from app.TotalAnalysisPresenter import TotalAnalysisPresenter
from app.AnalyticConstants import *
from app.HandlerECG import *
import logging


class AnalysisPresenter(QtWidgets.QMainWindow):

    def __init__(self, presenter, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.presenter = presenter
        self.secondWin = None
        self.ui = AnalysisView()
        self.ui.setupUi(self)
        self.add_params()
        self.message = ''

    def add_params(self):
        handler = HandlerECG(self.presenter.N)
        if self.presenter.person != '':
            record, annotation = handler.get_Inform_from_Person(self.presenter.person)
        else:
            self.presenter.person = self.presenter.array_of_patients[0]
            record, annotation = handler.get_Inform_from_Person(self.presenter.array_of_patients[0])

        logging.info(record.__dict__)
        ECG, Filter_ECG, Pana_Tompkinsa_QRS = handler.Pana_Tompkinsa(record.p_signal, record.fs)

        self.ui.filter_ecg.plot(self.presenter.f_x, Filter_ECG).setPen(color=(200, 200, 255), width=1)
        self.ui.filter_ecg.setLabel('left', 'FILTER ECG')
        self.ui.filter_ecg.setLabel('bottom', 'Time (ms)')
        self.ui.ecg.plot(self.presenter.f_x, ECG).setPen(color=(200, 200, 255), width=1)
        self.ui.ecg.setLabel('left', 'ECG')
        self.ui.ecg.setLabel('bottom', 'Time (ms)')
        self.ui.QRS_view.plot(self.presenter.f_x, Pana_Tompkinsa_QRS).setPen(color=(200, 200, 255), width=2)
        self.ui.QRS_view.setLabel('left', 'QRS')
        self.ui.QRS_view.setLabel('bottom', 'Time (ms)')
        self.ui.person.setText(self.presenter.person)
        index = record.comments[1].rfind(':')
        index_end = len(record.comments[1])
        self.ui.sex.setText(record.comments[1][index + 1:index_end])
        index = record.comments[0].rfind(':')
        index_end = len(record.comments[0])
        self.ui.age.setText(record.comments[0][index + 1:index_end])
        index = record.comments[2].rfind(':')
        index_end = len(record.comments[2])
        self.ui.data.setText(record.comments[2][index + 1:index_end])

        self.ui.person.setReadOnly(True)
        self.ui.sex.setReadOnly(True)
        self.ui.age.setReadOnly(True)
        self.ui.data.setReadOnly(True)

        peaks, M, D, SCO, coefficient_cov, m, amplitude, delta_x, index, vri, iarp, sib = handler.static_analysis_ECG(
            record)

        self.ui.M.setText(str('%.3f' % M) + 'c')
        self.ui.sco.setText(str('%.3f' % SCO) + 'c')
        self.ui.delta_x.setText(str('%.3f' % delta_x) + 'c')
        self.ui.mo.setText(str('%.3f' % m) + 'c')
        self.ui.A_mo.setText(str('%.3f' % amplitude) + '%')
        self.ui.VPR.setText(str('%.0f' % vri) + ' ед')

        self.ui.IVR.setText(str('%.0f' % index) + '  ед')
        self.ui.PAPR.setText(str('%.0f' % iarp) + ' ед')
        self.ui.v.setText(str('%.3f' % coefficient_cov) + '%')
        self.ui.INB.setText(str('  ' + '%.0f' % sib) + ' ед')

        self.ui.M.setReadOnly(True)
        self.ui.sco.setReadOnly(True)
        self.ui.delta_x.setReadOnly(True)
        self.ui.mo.setReadOnly(True)
        self.ui.A_mo.setReadOnly(True)
        self.ui.VPR.setReadOnly(True)
        self.ui.bpm.setReadOnly(True)
        self.ui.IVR.setReadOnly(True)
        self.ui.PAPR.setReadOnly(True)
        self.ui.v.setReadOnly(True)
        self.ui.INB.setReadOnly(True)

        p = np.zeros(len(peaks))
        for i in range(len(peaks)):
            p[i] = Pana_Tompkinsa_QRS[int(peaks[i])]

        bpm = handler.beats_per_minute(M)
        self.ui.bpm.setText(str('%.0f' % bpm) + ' уд. в минуту')
        self.ui.QRS_view.plot(peaks, p, pen=None, symbol='star', symbolSize=16, symbolBrush=(217, 83, 25))
        self.presenter.full_analysis = function_analysis(peaks, M, D, SCO, coefficient_cov, m, amplitude, delta_x,
                                                         index, vri, iarp,
                                                         sib, bpm)

        self.ui.full_analysis.clicked.connect(self.open_total_analysis_page)

    def open_total_analysis_page(self):
        self.secondWin = TotalAnalysisPresenter(self.presenter, self)
        self.secondWin.show()
