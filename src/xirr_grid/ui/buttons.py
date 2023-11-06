from PySide6.QtWidgets import QPushButton, QColorDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class ColorButton(QPushButton):
    
    def __init__(self, parent):
        super().__init__(parent)
        self._color = Qt.green
        self.color_dialog = QColorDialog(self._color, parent=self)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: QColor):
        self._color = color

    def mousePressEvent(self, event):
        self.color_dialog.show()
