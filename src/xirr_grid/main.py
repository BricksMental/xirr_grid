import sys

from PySide6.QtWidgets import QApplication

from xirr_grid.ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.setWindowFlags(Qt.FramelessWindowHint)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
