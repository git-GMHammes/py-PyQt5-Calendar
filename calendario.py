# Autor: Gustavo Hammes
# contato@habilidade.com
# Whatsapp: +55 (21) 9 8055-8545
# 
# Python 3.10.4
# pip 22.0.4
# 
# python.exe -m pip install --upgrade pip
# python -m venv .venv
# Source .venv/Scripts/activate 
# pip install PyQt5
# 
from PyQt5 import QtCore, QtGui, QtWidgets 
import sys

class Ui_MainWindow():
    def setupUi(self, MainWindow):
        # set window title 
        MainWindow.setWindowTitle('Calendar')
        # resize window
        MainWindow.resize(501, 422)
        # create central widget area on main window 
        self.centralwidget=QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        # creare calendar widget 
        self.calendar=QtWidgets.QCalendarWidget(self.centralwidget)
        # setGeometry for calendar
        self.calendar.setGeometry(QtCore.QRect(0, 0, 501, 371))
        # label to display selected date
        self.label = QtWidgets.QLabel(self.centralwidget)
        # set label geometry
        self.label.setGeometry(QtCore.QRect(5, 380, 341, 31))
        # set label style
        self.label.setStyleSheet('font: 75 22pt Verdana')
        # set label text
        self.label.setText('Select a date')
        # set changed selection
        self.calendar.selectionChanged.connect(self.date)
        
        
    def date(self):
        #get selected date
        selected_date= self.calendar.selectedDate() 
        # set label text as selected date 
        # #self.label.setText(str(selected_date.topyDate()))
        self.label.setText(str(selected_date.toString()))
        

app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
