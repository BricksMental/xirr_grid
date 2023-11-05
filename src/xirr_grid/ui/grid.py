import random
from enum import Enum

from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsSimpleTextItem, QGraphicsTextItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QPen


class CellLabelType(Enum):
    NONE = None
    ALL = 'ALL'
    HEADERS = 'HEADERS'


class XirrGrid(QGraphicsView):

    def __init__(self, x, y, width, height, num_columns, num_rows, parent=None, title='XirrGrid'):
        super().__init__(parent=parent)
        self.setWindowTitle(title)
        self.grid_scene = QGraphicsScene(x, y, width, height, self)
        self.setScene(self.grid_scene)
        self.num_columns = num_columns
        self.num_rows = num_rows
        self.rect_width = width / num_columns
        self.rect_height = height / num_rows
        self.setBackgroundBrush(Qt.green)
        for column in range(num_columns):
            for row in range(num_rows):
                self.draw_rect(column, row)

    def draw_rect(self, column, row):
        # Define the pen (line)


        rect = XirrGridCell(0, 0, self.rect_width, self.rect_height, column, row)

        # Set the origin (position) of the rectangle in the scene.
        # Set the origin (position) of the rectangle in the scene.
        rect.setPos(column*self.rect_width, row*self.rect_height)

        rect.highlight = random.choice([True, False])

        self.grid_scene.addItem(rect)


class XirrGridCell(QGraphicsRectItem):
    def __init__(self, x: float, y: float, w: float, h: float, column: int, row: int, border_color=Qt.white, border_width=2, parent=None):
        super().__init__(x, y, w, h, parent)
        self.column = column
        self.row = row
        self._highlight = False
        pen = QPen(border_color)
        pen.setWidth(border_width)
        self.setPen(pen)
        self.text_label = QGraphicsSimpleTextItem(parent=self)
        self.text_label.setBrush(border_color)
        self.text_label.setText('HUHU')

    @property
    def highlight(self):
        return self._highlight

    @highlight.setter
    def highlight(self, value):
        self._highlight = value
        print(self.highlight)
        if self._highlight:
            self.setBrush(Qt.red)
        else:
            self.setBrush(Qt.green)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        print(event)
        print(self.column, self.row)
        self.highlight = not self.highlight
