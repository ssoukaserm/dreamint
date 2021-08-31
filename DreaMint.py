# ----------------------- Importing Libraries ------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

# ----------------------- Setting the look of the Window and layouts ------------------------------

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(310, 470)
        MainWindow.setStyleSheet(u"background-color: rgb(29, 37, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

# ----------------------- Allow only numerical numbers ------------------------------
        validator = QRegExpValidator(QRegExp("^(-?\d+)(\.\d+)?$"))

# ----------------------- Price Box label ------------------------------
        self.price_box_label = QtWidgets.QLabel(self.centralwidget)
        self.price_box_label.setGeometry(QtCore.QRect(10, 50, 311, 31))
        self.price_box_label.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 15pt \"Gill Sans MT\";")
        self.price_box_label.setObjectName("price_box_label")

# ----------------------- Number of Assets label ------------------------------
        self.asset_label = QtWidgets.QLabel(self.centralwidget)
        self.asset_label.setGeometry(QtCore.QRect(9, 160, 361, 21))
        self.asset_label.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 15pt \"Gill Sans MT\";")
        self.asset_label.setObjectName("asset_label")

# ----------------------- Appearance of GO button ------------------------------
        self.calc_asset_button = QtWidgets.QPushButton(self.centralwidget)
        self.calc_asset_button.setGeometry(QtCore.QRect(10, 260, 291, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calc_asset_button.sizePolicy().hasHeightForWidth())
        self.calc_asset_button.setSizePolicy(sizePolicy)
        self.calc_asset_button.setStyleSheet("QPushButton{\n"
        "color: rgb(255, 255, 255);\n"
        "font: 20pt \"Gill Sans MT\";\n"
        "border-color: rgb(106, 106, 106);\n"
        "border-width :3px;\n"
        "border-style:solid;\n"
        "background-color: rgb(0, 85, 127);\n"
        "\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "	background-color: rgb(0, 106, 255);\n"
        "}\n"
        "\n"
        "")
        self.calc_asset_button.setObjectName("calc_asset_button")

# ----------------------- Appearance of Profit Box ------------------------------
        self.profit_box = QtWidgets.QLabel(self.centralwidget)
        self.profit_box.setGeometry(QtCore.QRect(10, 360, 291, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profit_box.sizePolicy().hasHeightForWidth())
        self.profit_box.setSizePolicy(sizePolicy)
        self.profit_box.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 25pt \"Gill Sans MT\";\n"
        "border-color: rgb(255, 255, 255);\n"
        "border-width :2px;\n"
        "border-style:solid;\n"
        "background-color: rgb(31, 31, 31);\n"
        "color: rgb(255, 255, 255);\n"
        "border-color: rgb(66, 66, 66);")
        self.profit_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.profit_box.setObjectName("profit_box")

# ----------------------- Label properties of DreaMint label ------------------------------
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(20, 0, 321, 40))
        self.main_label.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 20pt \"Gill Sans MT\";")
        self.main_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.main_label.setObjectName("main_label")

# ----------------------- Label properties of version label ------------------------------
        self.version_label = QtWidgets.QLabel(self.centralwidget)
        self.version_label.setGeometry(QtCore.QRect(120, 425, 168, 21))
        self.version_label.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 10pt \"Gill Sans MT\";")
        self.version_label.setObjectName("version_label")

# ----------------------- Label properties of profit label ------------------------------
        self.profit_label = QtWidgets.QLabel(self.centralwidget)
        self.profit_label.setGeometry(QtCore.QRect(10, 330, 84, 28))
        self.profit_label.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 15pt \"Gill Sans MT\";")
        self.profit_label.setObjectName("profit_label")

# ----------------------- Price Box Field ------------------------------
        self.price_box = QtWidgets.QLineEdit(self.centralwidget)
        self.price_box.setGeometry(QtCore.QRect(10, 90, 291, 61))
        self.price_box.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 25pt \"Gill Sans MT\";\n"
        "border-color: rgb(255, 255, 255);\n"
        "border-width :2px;\n"
        "border-style:solid;\n"
        "background-color: rgb(31, 31, 31);\n"
        "color: rgb(255, 255, 255);\n"
        "border-color: rgb(66, 66, 66);")
        self.price_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.price_box.setObjectName("price_box")
        self.price_box.setValidator(validator)

# ----------------------- Asset Box Field ------------------------------
        self.asset_box = QtWidgets.QLineEdit(self.centralwidget)
        self.asset_box.setGeometry(QtCore.QRect(10, 190, 291, 61))
        self.asset_box.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 25pt \"Gill Sans MT\";\n"
        "border-color: rgb(255, 255, 255);\n"
        "border-width :2px;\n"
        "border-style:solid;\n"
        "background-color: rgb(31, 31, 31);\n"
        "color: rgb(255, 255, 255);\n"
        "border-color: rgb(66, 66, 66);")
        self.asset_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.asset_box.setObjectName("asset_box")
        self.asset_box.setValidator(validator)
        MainWindow.setCentralWidget(self.centralwidget)


# ----------------------- Status Bar/Main Window ------------------------------
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# ----------------------- Setting Labels of Fields/Buttons ------------------------------
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DreaMint Calculator"))
        self.price_box_label.setText(_translate("MainWindow", "Price of Crypto/Stock"))
        self.asset_label.setText(_translate("MainWindow", "# of Coins/Stock"))
        self.calc_asset_button.setText(_translate("MainWindow", "GO"))
        self.profit_box.setText(_translate("MainWindow", "$0.00"))
        self.main_label.setText(_translate("MainWindow", "DreaMint Calculator"))
        self.version_label.setText(_translate("MainWindow", "VERSION 1.0"))
        self.profit_label.setText(_translate("MainWindow", "Profit"))
        self.price_box.setPlaceholderText(_translate("MainWindow", "0"))
        self.asset_box.setPlaceholderText(_translate("MainWindow", "0"))

# ----------------------- Defining what GO button does ------------------------------
        self.calc_asset_button.clicked.connect(self.calculate_profit)

# ----------------------- Calculating price with asset ------------------------------

    # Calculating price and assets by clicking button
    def calculate_profit(self):
        price = float(self.price_box.text())
        assets = float(self.asset_box.text())
        total_price = float(price) * float(assets)
        total_price_string = "${:,.2f}".format(total_price)
        self.profit_box.setText(total_price_string)


# ----------- Creating PYQT5 app, windows, and proper termination of app ------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
