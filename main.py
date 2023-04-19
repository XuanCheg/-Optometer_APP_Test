import ui
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ui.Ui_Mainwindow()
    sys.exit(app.exec())
