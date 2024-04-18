from PyQt5 import QtWidgets
from calcul_interface import Ui_MainWindow

class defs_type(Ui_MainWindow):
    def __init__(self, number):
        self.number = number  
    
    def type_function(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        
    def printer(self, number):
        print(number)
        