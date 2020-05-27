from PyQt5 import QtCore, QtWidgets
from app.TotalAnalysisECG import TotalAnalysisView


class TotalAnalysisPresenter(QtWidgets.QMainWindow):

    def __init__(self, presenter, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.presenter = presenter
        self.ui = TotalAnalysisView()
        self.ui.setupUi(self)
        self.ui.text.setText(str(self.presenter.full_analysis))
        self.ui.text.setReadOnly(True)
