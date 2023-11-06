from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot

from xirr_grid.ui.main_window_ui import Ui_MainWindow
from xirr_grid.ui.grid import XirrGrid


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_grid()

    def init_grid(self):
        width = self.width_spin_box.value()
        height = self.height_spin_box.value()
        #self.grid_view.setMaximumSize(width, height)
        #self.grid_view.setMinimumSize(width, height)
        self.grid = XirrGrid(0, 0, width, height, self.columns_spin_box.value(), self.rows_spin_box.value())
        self.grid.show()

    @Slot()
    def on_show_grid_button_clicked(self):
        self.init_grid()
