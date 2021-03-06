from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                        QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from selenium import webdriver

import sys
import login
from functions import resource_path

# Login Screen
from Ui_LoginScreen import Ui_LoginScreen
from main_screen import MainScreen


class Main(QMainWindow):
    # To know if showPassword is on or off. 0 = off | 1 = on
    passwordStatus = 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(70, 50, 30, 80))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # adding functions to GUI objects

        self.ui.minimizeBtn.clicked.connect(lambda: self.showMinimized())
        self.ui.closeBtn.clicked.connect(lambda: self.close())
        self.ui.loginBtn.clicked.connect(lambda: self.checkLogin())
        self.ui.showPass.clicked.connect(self.showPassword)

        def moveWindow(e):
            # Detect if the window is  normal size
            if not self.isMaximized():  # Not maximized
                # Move window only when window is normal size
                # if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    # Move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.dropShadowFrame.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def showPassword(self):
        icon = QIcon()
        if self.passwordStatus == 0:
            self.ui.passwordTxt.setEchoMode(QLineEdit.Normal)
            icon.addFile(resource_path("assets/hide_pass.png"),
                         QSize(), QIcon.Normal, QIcon.On)
            self.passwordStatus = 1
        else:
            self.ui.passwordTxt.setEchoMode(QLineEdit.Password)
            icon.addFile(resource_path('assets/show_pass.png'),
                         QSize(), QIcon.Normal, QIcon.On)
            self.passwordStatus = 0
        self.ui.showPass.setIcon(icon)

    def checkLogin(self):
        username = self.ui.usernameTxt.text()
        password = self.ui.passwordTxt.text()

        if len(username.strip()) == 0 or len(password.strip()) == 0:
            QMessageBox.information(self, 'Advice',
                                    "You forgot to write your account info",
                                    QMessageBox.Ok)
            self.ui.usernameTxt.setFocus()
        else:
            self.signin()

    def signin(self):
        username = self.ui.usernameTxt.text()
        password = self.ui.passwordTxt.text()
        try:
            driver = webdriver.Chrome(resource_path('chromedriver.exe'))
            l = login.Login(driver, username, password)
            l.signIn()
            # * we show the Main Screen and close the Login Screen
            self.mainScreen = MainScreen(username, driver)
            self.mainScreen.show()
            self.close()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.installEventFilter(window)
    sys.exit(app.exec_())
