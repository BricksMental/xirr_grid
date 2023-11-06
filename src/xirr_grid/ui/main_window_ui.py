# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

from xirr_grid.ui.buttons import ColorButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(769, 416)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.gridLayout_3 = QGridLayout(self.main_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.width_spin_box = QSpinBox(self.main_widget)
        self.width_spin_box.setObjectName(u"width_spin_box")
        self.width_spin_box.setMinimum(16)
        self.width_spin_box.setMaximum(4096)
        self.width_spin_box.setValue(640)

        self.gridLayout.addWidget(self.width_spin_box, 0, 0, 1, 1)

        self.width_label = QLabel(self.main_widget)
        self.width_label.setObjectName(u"width_label")

        self.gridLayout.addWidget(self.width_label, 0, 1, 1, 1)

        self.height_spin_box = QSpinBox(self.main_widget)
        self.height_spin_box.setObjectName(u"height_spin_box")
        self.height_spin_box.setMinimum(16)
        self.height_spin_box.setMaximum(4096)
        self.height_spin_box.setValue(480)

        self.gridLayout.addWidget(self.height_spin_box, 0, 2, 1, 1)

        self.height_label = QLabel(self.main_widget)
        self.height_label.setObjectName(u"height_label")

        self.gridLayout.addWidget(self.height_label, 0, 3, 1, 1)

        self.columns_spin_box = QSpinBox(self.main_widget)
        self.columns_spin_box.setObjectName(u"columns_spin_box")
        self.columns_spin_box.setMinimum(1)
        self.columns_spin_box.setMaximum(1024)
        self.columns_spin_box.setValue(8)

        self.gridLayout.addWidget(self.columns_spin_box, 1, 0, 1, 1)

        self.columns_label = QLabel(self.main_widget)
        self.columns_label.setObjectName(u"columns_label")

        self.gridLayout.addWidget(self.columns_label, 1, 1, 1, 1)

        self.rows_spin_box = QSpinBox(self.main_widget)
        self.rows_spin_box.setObjectName(u"rows_spin_box")
        self.rows_spin_box.setMinimum(1)
        self.rows_spin_box.setMaximum(1024)
        self.rows_spin_box.setValue(6)

        self.gridLayout.addWidget(self.rows_spin_box, 1, 2, 1, 1)

        self.rows_label = QLabel(self.main_widget)
        self.rows_label.setObjectName(u"rows_label")

        self.gridLayout.addWidget(self.rows_label, 1, 3, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.cell_label_group_box = QGroupBox(self.main_widget)
        self.cell_label_group_box.setObjectName(u"cell_label_group_box")
        self.gridLayout_2 = QGridLayout(self.cell_label_group_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton = QRadioButton(self.cell_label_group_box)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.cell_label_group_box)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_2.addWidget(self.radioButton_2, 1, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.cell_label_group_box)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_2.addWidget(self.radioButton_3, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.cell_label_group_box, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.background_color_button = ColorButton(self.main_widget)
        self.background_color_button.setObjectName(u"background_color_button")

        self.verticalLayout.addWidget(self.background_color_button)

        self.highlight_color_button = ColorButton(self.main_widget)
        self.highlight_color_button.setObjectName(u"highlight_color_button")

        self.verticalLayout.addWidget(self.highlight_color_button)

        self.grid_color_button = ColorButton(self.main_widget)
        self.grid_color_button.setObjectName(u"grid_color_button")

        self.verticalLayout.addWidget(self.grid_color_button)

        self.text_color_button = ColorButton(self.main_widget)
        self.text_color_button.setObjectName(u"text_color_button")

        self.verticalLayout.addWidget(self.text_color_button)

        self.text_outline_color_button = ColorButton(self.main_widget)
        self.text_outline_color_button.setObjectName(u"text_outline_color_button")

        self.verticalLayout.addWidget(self.text_outline_color_button)


        self.gridLayout_3.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.show_grid_button = QPushButton(self.main_widget)
        self.show_grid_button.setObjectName(u"show_grid_button")

        self.gridLayout_3.addWidget(self.show_grid_button, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.main_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 769, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.width_label.setBuddy(self.width_spin_box)
        self.height_label.setBuddy(self.height_spin_box)
        self.columns_label.setBuddy(self.columns_spin_box)
        self.rows_label.setBuddy(self.rows_spin_box)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"XirrGrid Manager", None))
#if QT_CONFIG(statustip)
        self.main_widget.setStatusTip(QCoreApplication.translate("MainWindow", u"WTF", None))
#endif // QT_CONFIG(statustip)
        self.width_label.setText(QCoreApplication.translate("MainWindow", u"width", None))
        self.height_label.setText(QCoreApplication.translate("MainWindow", u"height", None))
        self.columns_label.setText(QCoreApplication.translate("MainWindow", u"columns", None))
        self.rows_label.setText(QCoreApplication.translate("MainWindow", u"rows", None))
        self.cell_label_group_box.setTitle(QCoreApplication.translate("MainWindow", u"cell labeling style", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"label rows and columns", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"label all cells", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"no labels", None))
        self.background_color_button.setText(QCoreApplication.translate("MainWindow", u"background color", None))
        self.highlight_color_button.setText(QCoreApplication.translate("MainWindow", u"highlight color", None))
        self.grid_color_button.setText(QCoreApplication.translate("MainWindow", u"grid color", None))
        self.text_color_button.setText(QCoreApplication.translate("MainWindow", u"text color", None))
        self.text_outline_color_button.setText(QCoreApplication.translate("MainWindow", u"text outline color", None))
        self.show_grid_button.setText(QCoreApplication.translate("MainWindow", u"show grid", None))
    # retranslateUi

