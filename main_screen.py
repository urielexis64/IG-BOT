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

import sys
import time, threading
import Utilities as utils
from functions import resource_path

from ui_main_screen import Ui_MainScreen

ut = 0

activeBtnStyle ="QPushButton {\ncolor: rgb(255, 255, 255);\nbackground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(67, 102, 201, 255), stop:0.517045 rgba(186, 49, 181, 255), stop:1 rgba(230, 71, 110, 255));\nborder: 0px solid;\n}\nQPushButton:hover {\nbackground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(67, 102, 201, 255), stop:0.517045 rgba(186, 49, 181, 255), stop:1 rgba(230, 71, 110, 255));\n}" 
                
inactiveBtnStyle="QPushButton {\ncolor: rgb(255, 255, 255);\nbackground-color: rgb(35,35,35);\nborder: 0px solid;\n}\nQPushButton:hover {\nbackground-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(67, 102, 201, 255), stop:0.517045 rgba(186, 49, 181, 255), stop:1 rgba(230, 71, 110, 255));\n}"

class MainScreen(QMainWindow):

    def __init__(self, username, driver):
        QMainWindow.__init__(self)
        self.ui = Ui_MainScreen()
        self.ui.setupUi(self)
        self.driver = driver

        global ut
        ut = utils.Utilities(driver)

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
        self.ui.likeBtn.clicked.connect(lambda: ut.like(self.ui.linkPostTxt.text()))
        self.ui.chooseBtn.clicked.connect(chooseFile)
        self.ui.usernameLbl.setText(username)

        self.ui.likeBtnSection.setChecked(True)
        self.ui.likeBtnSection.clicked.connect(lambda: self.changeSectionBtnState(self.ui.likeBtnSection))
        self.ui.messageBtnSection.clicked.connect(lambda: self.changeSectionBtnState(self.ui.messageBtnSection))
        self.ui.followBtnSection.clicked.connect(lambda: self.changeSectionBtnState(self.ui.followBtnSection))
        self.ui.commentBtnSection.clicked.connect(lambda: self.changeSectionBtnState(self.ui.commentBtnSection))

        def moveWindow(e):
            # Detect if the window is  normal size
            if self.isMaximized() == False:  # Not maximized
                # Move window only when window is normal size
                # if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    # Move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.topBar.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def changeSectionBtnState(self, btn):
        #Reset all the buttons
        self.ui.likeBtnSection.setStyleSheet(inactiveBtnStyle)
        self.ui.messageBtnSection.setStyleSheet(inactiveBtnStyle)
        self.ui.followBtnSection.setStyleSheet(inactiveBtnStyle)
        self.ui.commentBtnSection.setStyleSheet(inactiveBtnStyle)
        self.ui.likeBtnSection.setChecked(False)
        self.ui.messageBtnSection.setChecked(False)
        self.ui.followBtnSection.setChecked(False)
        self.ui.commentBtnSection.setChecked(False)

        if(not btn.isChecked()):
            btn.setStyleSheet(activeBtnStyle)
            btn.setChecked(True)
        


def chooseFile():
    path = QFileDialog.getOpenFileName(caption="Open .txt file",filter="TXT Files (*.txt)")[0]
    links = open(path, 'r')
    for link in links:
        ut.like(link)


