# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginScreen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from functions import resource_path

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(350, 400)
        self.centralwidget = QWidget(LoginScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.506, y2:1, stop:0 rgba(69, 45, 93, 255), stop:1 rgba(35, 38, 79, 255));\n"
"	border-radius: 10px;\n"
"	color: rgb(240,240,240);\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.igLogo = QLabel(self.dropShadowFrame)
        self.igLogo.setObjectName(u"igLogo")
        self.igLogo.setGeometry(QRect(65, 20, 75, 75))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.igLogo.sizePolicy().hasHeightForWidth())
        self.igLogo.setSizePolicy(sizePolicy)
        self.igLogo.setPixmap(QPixmap(resource_path("assets/ig_logo.png")))
        self.igLogo.setScaledContents(True)
        self.igLogo.setAlignment(Qt.AlignCenter)
        self.createdByLbl = QLabel(self.dropShadowFrame)
        self.createdByLbl.setObjectName(u"createdByLbl")
        self.createdByLbl.setGeometry(QRect(-1, 340, 331, 20))
        font = QFont()
        font.setFamily(u"Gotham Pro Light")
        font.setStyleStrategy(QFont.PreferAntialias)
        self.createdByLbl.setFont(font)
        self.createdByLbl.setStyleSheet(u"background-color: rgb(0,0,0,0);\n"
"")
        self.createdByLbl.setTextFormat(Qt.AutoText)
        self.createdByLbl.setAlignment(Qt.AlignCenter)
        self.createdByLbl.setOpenExternalLinks(True)
        self.usernameLbl = QLabel(self.dropShadowFrame)
        self.usernameLbl.setObjectName(u"usernameLbl")
        self.usernameLbl.setGeometry(QRect(50, 130, 80, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.usernameLbl.setFont(font1)
        self.usernameLbl.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.usernameTxt = QLineEdit(self.dropShadowFrame)
        self.usernameTxt.setObjectName(u"usernameTxt")
        self.usernameTxt.setGeometry(QRect(130, 133, 150, 25))
        font2 = QFont()
        font2.setPointSize(10)
        self.usernameTxt.setFont(font2)
        self.usernameTxt.setStyleSheet(u"QLineEdit{\n"
"	border-radius:10px;\n"
"}")
        self.usernameTxt.setAlignment(Qt.AlignCenter)
        self.passwordLbl = QLabel(self.dropShadowFrame)
        self.passwordLbl.setObjectName(u"passwordLbl")
        self.passwordLbl.setGeometry(QRect(50, 180, 80, 30))
        self.passwordLbl.setFont(font1)
        self.passwordLbl.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.passwordTxt = QLineEdit(self.dropShadowFrame)
        self.passwordTxt.setObjectName(u"passwordTxt")
        self.passwordTxt.setGeometry(QRect(130, 183, 150, 25))
        self.passwordTxt.setFont(font2)
        self.passwordTxt.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 10px;\n"
"}")
        self.passwordTxt.setEchoMode(QLineEdit.Password)
        self.passwordTxt.setAlignment(Qt.AlignCenter)
        self.passwordTxt.setDragEnabled(True)
        self.loginBtn = QPushButton(self.dropShadowFrame)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(50, 230, 230, 30))
        font3 = QFont()
        font3.setFamily(u"Gotham Pro Black")
        font3.setPointSize(10)
        self.loginBtn.setFont(font3)
        self.loginBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginBtn.setAcceptDrops(False)
        self.loginBtn.setLayoutDirection(Qt.LeftToRight)
        self.loginBtn.setAutoFillBackground(False)
        self.loginBtn.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(62, 67, 153, 255), stop:1 rgba(136, 37, 147, 255));\n"
"border-radius: 15px;\n"
"color: white;\n"
"}")
        icon = QIcon()
        icon.addFile(resource_path("assets/login.png"), QSize(), QIcon.Normal, QIcon.On)
        self.loginBtn.setIcon(icon)
        self.closeBtn = QPushButton(self.dropShadowFrame)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setGeometry(QRect(300, 10, 16, 16))
        self.closeBtn.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"border-radius: 8px;\n"
"background-color: rgb(255, 76, 76);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 76, 76, 150);\n"
"}")
        self.minimizeBtn = QPushButton(self.dropShadowFrame)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setGeometry(QRect(280, 10, 16, 16))
        self.minimizeBtn.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 255, 142)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 142, 150);\n"
"}")
        self.igBotLbl = QLabel(self.dropShadowFrame)
        self.igBotLbl.setObjectName(u"igBotLbl")
        self.igBotLbl.setGeometry(QRect(145, 20, 120, 75))
        sizePolicy.setHeightForWidth(self.igBotLbl.sizePolicy().hasHeightForWidth())
        self.igBotLbl.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamily(u"Gotham Pro")
        font4.setPointSize(14)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.igBotLbl.setFont(font4)
        self.igBotLbl.setFocusPolicy(Qt.ClickFocus)
        self.igBotLbl.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.igBotLbl.setAlignment(Qt.AlignCenter)
        self.showPass = QPushButton(self.dropShadowFrame)
        self.showPass.setObjectName(u"showPass")
        self.showPass.setGeometry(QRect(284, 180, 30, 30))
        self.showPass.setCursor(QCursor(Qt.PointingHandCursor))
        self.showPass.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon1 = QIcon()
        icon1.addFile(resource_path("assets/show_pass.png"), QSize(), QIcon.Normal, QIcon.On)
        self.showPass.setIcon(icon1)
        self.showPass.setIconSize(QSize(30, 30))
        self.showPass.setCheckable(False)

        self.horizontalLayout.addWidget(self.dropShadowFrame)

        LoginScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginScreen)

        QMetaObject.connectSlotsByName(LoginScreen)
    # setupUi

    def retranslateUi(self, LoginScreen):
        LoginScreen.setWindowTitle(QCoreApplication.translate("LoginScreen", u"MainWindow", None))
        self.igLogo.setText("")
        self.createdByLbl.setText(QCoreApplication.translate("LoginScreen", u"<a href=\"http://www.github.com/urielexis64\"><font color=white>Created by urielexis64</a></font>", None))
        self.usernameLbl.setText(QCoreApplication.translate("LoginScreen", u"Username", None))
        self.usernameTxt.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Username", None))
        self.passwordLbl.setText(QCoreApplication.translate("LoginScreen", u"Password", None))
        self.passwordTxt.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"Password", None))
        self.loginBtn.setText(QCoreApplication.translate("LoginScreen", u"LOGIN", None))
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("LoginScreen", u"close", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("LoginScreen", u"minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
        self.igBotLbl.setText(QCoreApplication.translate("LoginScreen", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">IG </span><span style=\" font-size:18pt;\">BOT</span></p></body></html>", None))
        self.showPass.setText("")
    # retranslateUi