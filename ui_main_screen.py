# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainScreen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        if not MainScreen.objectName():
            MainScreen.setObjectName(u"MainScreen")
        MainScreen.resize(800, 500)
        MainScreen.setMinimumSize(QSize(800, 500))
        MainScreen.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"QFrame#mainFrame{\n"
"	border-radius: 20px;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.mainFrame)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(0, 40))
        self.topBar.setMaximumSize(QSize(16777215, 40))
        self.topBar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.topBar.setFrameShape(QFrame.NoFrame)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.topBar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(80, 40))
        self.frame_toggle.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(62, 67, 153, 255), stop:1 rgba(136, 37, 147, 255));")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.instagramLogo = QPushButton(self.frame_toggle)
        self.instagramLogo.setObjectName(u"instagramLogo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instagramLogo.sizePolicy().hasHeightForWidth())
        self.instagramLogo.setSizePolicy(sizePolicy)
        self.instagramLogo.setFocusPolicy(Qt.NoFocus)
        self.instagramLogo.setAutoFillBackground(False)
        self.instagramLogo.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"assets/ig_logo.png", QSize(), QIcon.Normal, QIcon.On)
        self.instagramLogo.setIcon(icon)
        self.instagramLogo.setIconSize(QSize(32, 32))
#if QT_CONFIG(shortcut)
        self.instagramLogo.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.instagramLogo.setFlat(True)

        self.verticalLayout_2.addWidget(self.instagramLogo)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.topBar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.usernameLbl = QLabel(self.frame_top)
        self.usernameLbl.setObjectName(u"usernameLbl")
        self.usernameLbl.setGeometry(QRect(0, 0, 681, 40))
        font = QFont()
        font.setFamily(u"Gotham Pro Black")
        font.setPointSize(16)
        self.usernameLbl.setFont(font)
        self.usernameLbl.setStyleSheet(u"color: white;\n"
"background-color: rgb(35,35,35);")
        self.usernameLbl.setAlignment(Qt.AlignCenter)
        self.closeBtn = QPushButton(self.frame_top)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setGeometry(QRect(684, 12, 16, 16))
        self.closeBtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 66, 19);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 66, 19,200);\n"
"\n"
"}\n"
"\n"
"")
        self.minimizeBtn = QPushButton(self.frame_top)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setGeometry(QRect(660, 12, 16, 16))
        self.minimizeBtn.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 127,200);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(255, 255, 127);\n"
"border-radius: 8px;\n"
"}")

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout_7.addWidget(self.topBar)

        self.dropShadowFrame = QFrame(self.mainFrame)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"")
        self.dropShadowFrame.setFrameShape(QFrame.NoFrame)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.dropShadowFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.dropShadowFrame)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(80, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border-radius: 10px;")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.likeBtnSection = QPushButton(self.frame_top_menus)
        self.likeBtnSection.setObjectName(u"likeBtnSection")
        self.likeBtnSection.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamily(u"Gotham Pro")
        self.likeBtnSection.setFont(font1)
        self.likeBtnSection.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(67, 102, 201, 255), stop:0.517045 rgba(186, 49, 181, 255), stop:1 rgba(230, 71, 110, 255));;\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(67, 102, 201, 255), stop:0.517045 rgba(186, 49, 181, 255), stop:1 rgba(230, 71, 110, 255));\n"
"}")

        self.verticalLayout_4.addWidget(self.likeBtnSection)

        self.commentBtnSection = QPushButton(self.frame_top_menus)
        self.commentBtnSection.setObjectName(u"commentBtnSection")
        self.commentBtnSection.setMinimumSize(QSize(0, 40))
        self.commentBtnSection.setFont(font1)
        self.commentBtnSection.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(67, 102, 201, 255), stop:0.517045 rgba(186, 49, 181, 255), stop:1 rgba(230, 71, 110, 255));\n"
"}")

        self.verticalLayout_4.addWidget(self.commentBtnSection)

        self.followBtnSection = QPushButton(self.frame_top_menus)
        self.followBtnSection.setObjectName(u"followBtnSection")
        self.followBtnSection.setMinimumSize(QSize(0, 40))
        self.followBtnSection.setFont(font1)
        self.followBtnSection.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(67, 102, 201, 255), stop:0.517045 rgba(186, 49, 181, 255), stop:1 rgba(230, 71, 110, 255));\n"
"}")

        self.verticalLayout_4.addWidget(self.followBtnSection)

        self.messageBtnSection = QPushButton(self.frame_top_menus)
        self.messageBtnSection.setObjectName(u"messageBtnSection")
        self.messageBtnSection.setMinimumSize(QSize(0, 40))
        self.messageBtnSection.setFont(font1)
        self.messageBtnSection.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(67, 102, 201, 255), stop:0.517045 rgba(186, 49, 181, 255), stop:1 rgba(230, 71, 110, 255));\n"
"}")

        self.verticalLayout_4.addWidget(self.messageBtnSection)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.dropShadowFrame)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"QFrame{\n"
"	border-radius:10px;\n"
"}")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.likeSection = QWidget()
        self.likeSection.setObjectName(u"likeSection")
        self.linkPostTxt = QLineEdit(self.likeSection)
        self.linkPostTxt.setObjectName(u"linkPostTxt")
        self.linkPostTxt.setGeometry(QRect(20, 60, 660, 40))
        self.linkPostTxt.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Gotham Pro")
        font2.setPointSize(14)
        self.linkPostTxt.setFont(font2)
        self.linkPostTxt.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.postLinkLbl = QLabel(self.likeSection)
        self.postLinkLbl.setObjectName(u"postLinkLbl")
        self.postLinkLbl.setGeometry(QRect(20, 10, 120, 45))
        font3 = QFont()
        font3.setPointSize(24)
        self.postLinkLbl.setFont(font3)
        self.postLinkLbl.setStyleSheet(u"color: #FFF;\n"
"background-color: rgb(35, 35, 35);\n"
"BORDER-RADIUS: 0PX;")
        self.postLinkLbl.setAlignment(Qt.AlignCenter)
        self.likeBtn = QPushButton(self.likeSection)
        self.likeBtn.setObjectName(u"likeBtn")
        self.likeBtn.setGeometry(QRect(300, 110, 101, 30))
        font4 = QFont()
        font4.setFamily(u"Gotham Pro Black")
        self.likeBtn.setFont(font4)
        self.likeBtn.setStyleSheet(u"color: #FFF;\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(67, 102, 201, 255), stop:0.517045 rgba(186, 49, 181, 255), stop:1 rgba(230, 71, 110, 255));")
        self.chooseFileLbl = QLabel(self.likeSection)
        self.chooseFileLbl.setObjectName(u"chooseFileLbl")
        self.chooseFileLbl.setGeometry(QRect(20, 200, 541, 45))
        self.chooseFileLbl.setFont(font3)
        self.chooseFileLbl.setStyleSheet(u"color: #FFF;\n"
"background-color: rgb(35, 35, 35);\n"
"BORDER-RADIUS: 0PX;")
        self.chooseFileLbl.setAlignment(Qt.AlignCenter)
        self.chooseBtn = QPushButton(self.likeSection)
        self.chooseBtn.setObjectName(u"chooseBtn")
        self.chooseBtn.setGeometry(QRect(20, 260, 141, 31))
        self.chooseBtn.setFont(font4)
        self.chooseBtn.setStyleSheet(u"color: #FFF;\n"
"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(67, 102, 201, 255), stop:0.517045 rgba(186, 49, 181, 255), stop:1 rgba(230, 71, 110, 255));")
        self.stackedWidget.addWidget(self.likeSection)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setPointSize(40)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color: #FFF;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: #FFF;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout_7.addWidget(self.dropShadowFrame)


        self.verticalLayout.addWidget(self.mainFrame)

        MainScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainScreen)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainScreen)
    # setupUi

    def retranslateUi(self, MainScreen):
        MainScreen.setWindowTitle(QCoreApplication.translate("MainScreen", u"MainWindow", None))
        self.instagramLogo.setText("")
        self.usernameLbl.setText(QCoreApplication.translate("MainScreen", u"username", None))
        self.closeBtn.setText("")
        self.minimizeBtn.setText("")
        self.likeBtnSection.setText(QCoreApplication.translate("MainScreen", u"Like", None))
        self.commentBtnSection.setText(QCoreApplication.translate("MainScreen", u"Comment", None))
        self.followBtnSection.setText(QCoreApplication.translate("MainScreen", u"Follow", None))
        self.messageBtnSection.setText(QCoreApplication.translate("MainScreen", u"Message", None))
        self.postLinkLbl.setText(QCoreApplication.translate("MainScreen", u"Post link", None))
        self.likeBtn.setText(QCoreApplication.translate("MainScreen", u"LIKE!", None))
        self.chooseFileLbl.setText(QCoreApplication.translate("MainScreen", u"Choose a txt file (multiple posts likes)", None))
        self.chooseBtn.setText(QCoreApplication.translate("MainScreen", u"CHOOSE FILE", None))
        self.label_2.setText(QCoreApplication.translate("MainScreen", u"PAGE 2", None))
        self.label.setText(QCoreApplication.translate("MainScreen", u"PAGE 3", None))
    # retranslateUi

