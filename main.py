import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import threading
import login
import Utilities as utils

# Splash Screen
from Ui_LoginScreen import Ui_LoginScreen


class Main (QMainWindow):
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
            if self.isMaximized() == False:  # Not maximized
                # Move window only when window is normal size
                # ###############################################
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
        if(self.passwordStatus == 0):
            self.ui.passwordTxt.setEchoMode(QLineEdit.Normal)
            icon.addFile(u"assets/show_pass2.png",
                         QSize(), QIcon.Normal, QIcon.On)
            self.passwordStatus = 1
        else:
            self.ui.passwordTxt.setEchoMode(QLineEdit.Password)
            icon.addFile(u"assets/show_pass1.png",
                         QSize(), QIcon.Normal, QIcon.On)
            self.passwordStatus = 0
        self.ui.showPass.setIcon(icon)


    def checkLogin(self):
        username = self.ui.usernameTxt.text()
        password = self.ui.passwordTxt.text()

        if(len(username.strip()) == 0 or len(password.strip()) == 0):
            QMessageBox.information(self, 'Advice',
                                        "You forgot to write your account info",
                                        QMessageBox.Ok)
            self.ui.usernameTxt.setFocus()
        else:
            threading.Thread(target=self.signin).start()
        
        
    def signin(self):
        username = self.ui.usernameTxt.text()
        password = self.ui.passwordTxt.text()

        try:
            driver = webdriver.Chrome('..//chromedriver.exe')
            l = login.Login(driver, username, password)
            l.signIn()
            self.close()
        except:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.installEventFilter(window)
    sys.exit(app.exec_())
