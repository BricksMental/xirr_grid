import random

from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QPen


class XirrGrid(QGraphicsView):

    def __init__(self, x, y, width, height, num_columns, num_rows, parent=None):
        super().__init__(parent=parent)
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

        rect = QGraphicsRectItem(0, 0, self.rect_width, self.rect_height)

        rect.setPen(pen)


        # Set the origin (position) of the rectangle in the scene.
        rect.setPos(column*self.rect_width, row*self.rect_height)

        if random.choice([True, False]):
            rect.setBrush(Qt.red)

        self.grid_scene.addItem(rect)



