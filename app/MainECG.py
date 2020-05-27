import sys
from app.RegistrationPresenter import *
import qdarkstyle
import logging


class PresenterConstants:
    person = ''
    N = 5000
    f_x = [k for k in range(1, N + 1)]
    full_analysis = ''
    array_of_patients = ['Person_01',
                         'Person_02',
                         'Person_03',
                         'Person_04',
                         'Person_05',
                         'Person_06',
                         'Person_07',
                         'Person_08',
                         'Person_09',
                         'Person_10',
                         'Person_11',
                         'Person_12',
                         'Person_13'
                         ]


# pyqtgraph.examples.run()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    presenter = PresenterConstants()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    application = RegistrationPresenter(presenter)
    application.show()
    sys.exit(app.exec())
