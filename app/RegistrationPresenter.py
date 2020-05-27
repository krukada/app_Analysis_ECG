from PyQt5 import QtWidgets
from app.RegistrationView import RegistrationView
from app.AnalysisPresenter import AnalysisPresenter


class RegistrationPresenter(QtWidgets.QMainWindow):

    def __init__(self, presenter):
        super(RegistrationPresenter, self).__init__()
        self.presenter = presenter
        self.secondWin = None
        self.ui = RegistrationView()
        self.ui.setupUi(self)
        self.ui.massPatient.addItems(self.presenter.array_of_patients)
        self.ui.massPatient.activated[str].connect(self.save_selected_patient)
        self.ui.go_to_analys.clicked.connect(self.open_analysis_page)

    def open_analysis_page(self):
        self.secondWin = AnalysisPresenter(self.presenter, self)
        self.secondWin.show()

    def save_selected_patient(self, text):
        self.presenter.person = text
