# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog - untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(494, 394)
        Dialog.setStyleSheet(u"background: '#0d1001';\n"
"color: '#deae7a'")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(120, 10, 171, 31))
        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 60, 171, 21))
        self.label_9.setStyleSheet(u"font-size: 17px")
        self.decryption = QCheckBox(Dialog)
        self.buttonGroup = QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.decryption)
        self.decryption.setObjectName(u"decryption")
        self.decryption.setGeometry(QRect(10, 110, 121, 20))
        self.decryption.setStyleSheet(u"font-size: 13px")
        self.encryption = QCheckBox(Dialog)
        self.buttonGroup.addButton(self.encryption)
        self.encryption.setObjectName(u"encryption")
        self.encryption.setGeometry(QRect(10, 90, 111, 20))
        self.encryption.setStyleSheet(u"font-size: 13px")
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(190, 90, 171, 21))
        self.label_11.setStyleSheet(u"font-size: 13px")
        self.alphabet = QLineEdit(Dialog)
        self.alphabet.setObjectName(u"alphabet")
        self.alphabet.setGeometry(QRect(270, 90, 201, 21))
        self.alphabet.setStyleSheet(u"font-size:12px\n"
"")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(190, 120, 71, 21))
        self.label_10.setStyleSheet(u"font-size: 13px")
        self.message = QLineEdit(Dialog)
        self.message.setObjectName(u"message")
        self.message.setGeometry(QRect(270, 120, 201, 20))
        self.message.setStyleSheet(u"font-size:12px\n"
"")
        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(190, 60, 191, 21))
        self.label_13.setStyleSheet(u"font-size: 17px")
        self.power = QLineEdit(Dialog)
        self.power.setObjectName(u"power")
        self.power.setGeometry(QRect(270, 150, 201, 20))
        self.power.setStyleSheet(u"font-size:12px\n"
"")
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(190, 150, 71, 21))
        self.label_12.setStyleSheet(u"font-size: 13px")
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 220, 151, 111))
        self.textBrowser.setStyleSheet(u"font-size:12px\n"
"")
        self.textBrowser_2 = QTextBrowser(Dialog)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(300, 180, 111, 31))
        self.label_14 = QLabel(Dialog)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 190, 191, 21))
        self.label_14.setStyleSheet(u"font-size: 17px")
        self.label_15 = QLabel(Dialog)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(190, 190, 91, 21))
        self.label_15.setStyleSheet(u"font-size: 17px")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 230, 161, 28))
        self.pushButton.setStyleSheet(u"border: 1px solid grey;\n"
"background: whitesmoke;\n"
"color: black;\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u041a\u0432\u0430\u0434\u0440\u0430\u0442 \u041f\u043e\u043b\u0438\u0431\u0438\u0443\u0441\u0430", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b:", None))
        self.decryption.setText(QCoreApplication.translate("Dialog", u"\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.encryption.setText(QCoreApplication.translate("Dialog", u"\u0428\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u0410\u043b\u0444\u0430\u0432\u0438\u0442:", None))
        self.alphabet.setText(QCoreApplication.translate("Dialog", u"abcdefghijklmnopqrstuvwxyz", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435:", None))
        self.message.setText(QCoreApplication.translate("Dialog", u"HelloWorld", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b:", None))
        self.power.setText(QCoreApplication.translate("Dialog", u"25", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c:", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u041a\u0432\u0430\u0434\u0440\u0430\u0442 \u041f\u043e\u043b\u0438\u0431\u0438\u0443\u0441\u0430:", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
    # retranslateUi

