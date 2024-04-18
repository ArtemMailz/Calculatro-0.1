from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from calcul_interface import Ui_MainWindow

class ExecpensTarcer(QMainWindow):
    def __init__(self):
        super(ExecpensTarcer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wind = ExecpensTarcer()
    wind.show()
    
    sys.exit(app.exec())