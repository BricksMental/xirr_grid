import random

from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QPen


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
        pen = QPen(Qt.white)
        pen.setWidth(2)

        rect = XirrGridCell(0, 0, self.rect_width, self.rect_height, column, row)

        rect.setPen(pen)


        # Set the origin (position) of the rectangle in the scene.
        # Set the origin (position) of the rectangle in the scene.
        rect.setPos(column*self.rect_width, row*self.rect_height)

        rect.highlight = random.choice([True, False])

        self.grid_scene.addItem(rect)


class XirrGridCell(QGraphicsRectItem):
    def __init__(self, x: float, y: float, w: float, h: float, column: int, row: int, parent=None):
        super().__init__(x, y, w, h, parent)
        self.column = column
        self.row = row
        self._highlight = False

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
