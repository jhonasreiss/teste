import sys
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(800,700)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
    
