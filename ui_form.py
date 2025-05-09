# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDial, QLCDNumber,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.Button_Off = QPushButton(Widget)
        self.Button_Off.setObjectName(u"Button_Off")
        self.Button_Off.setGeometry(QRect(100, 310, 83, 29))
        self.servo_control_slide = QSlider(Widget)
        self.servo_control_slide.setObjectName(u"servo_control_slide")
        self.servo_control_slide.setGeometry(QRect(90, 430, 160, 18))
        self.servo_control_slide.setOrientation(Qt.Orientation.Horizontal)
        self.Led_Off = QPushButton(Widget)
        self.Led_Off.setObjectName(u"Led_Off")
        self.Led_Off.setGeometry(QRect(10, 210, 83, 29))
        self.checkBlue = QCheckBox(Widget)
        self.checkBlue.setObjectName(u"checkBlue")
        self.checkBlue.setGeometry(QRect(100, 250, 93, 26))
        self.Led_On = QPushButton(Widget)
        self.Led_On.setObjectName(u"Led_On")
        self.Led_On.setGeometry(QRect(10, 170, 83, 29))
        self.Button_On = QPushButton(Widget)
        self.Button_On.setObjectName(u"Button_On")
        self.Button_On.setGeometry(QRect(0, 310, 83, 29))
        self.set_180 = QCheckBox(Widget)
        self.set_180.setObjectName(u"set_180")
        self.set_180.setGeometry(QRect(220, 480, 93, 26))
        self.servo_control_rotate = QDial(Widget)
        self.servo_control_rotate.setObjectName(u"servo_control_rotate")
        self.servo_control_rotate.setGeometry(QRect(10, 400, 50, 64))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 380, 91, 20))
        self.checkYellow = QCheckBox(Widget)
        self.checkYellow.setObjectName(u"checkYellow")
        self.checkYellow.setGeometry(QRect(100, 210, 101, 26))
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 0, 91, 20))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 130, 91, 20))
        self.flashButton = QPushButton(Widget)
        self.flashButton.setObjectName(u"flashButton")
        self.flashButton.setGeometry(QRect(480, 30, 83, 29))
        self.browseButton = QPushButton(Widget)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setGeometry(QRect(370, 30, 83, 29))
        self.set_90 = QCheckBox(Widget)
        self.set_90.setObjectName(u"set_90")
        self.set_90.setGeometry(QRect(120, 480, 93, 26))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 290, 311, 20))
        self.set_0 = QCheckBox(Widget)
        self.set_0.setObjectName(u"set_0")
        self.set_0.setGeometry(QRect(20, 480, 93, 26))
        self.sketchPathEdit = QLineEdit(Widget)
        self.sketchPathEdit.setObjectName(u"sketchPathEdit")
        self.sketchPathEdit.setGeometry(QRect(210, 30, 121, 28))
        self.flashStatusLabel = QLabel(Widget)
        self.flashStatusLabel.setObjectName(u"flashStatusLabel")
        self.flashStatusLabel.setGeometry(QRect(0, 60, 331, 51))
        self.flashStatusLabel.setWordWrap(True)
        self.checkRed = QCheckBox(Widget)
        self.checkRed.setObjectName(u"checkRed")
        self.checkRed.setGeometry(QRect(100, 170, 93, 26))
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(470, 130, 91, 20))
        self.Light_sensor_On = QPushButton(Widget)
        self.Light_sensor_On.setObjectName(u"Light_sensor_On")
        self.Light_sensor_On.setGeometry(QRect(400, 170, 83, 29))
        self.Light_sensor_Off = QPushButton(Widget)
        self.Light_sensor_Off.setObjectName(u"Light_sensor_Off")
        self.Light_sensor_Off.setGeometry(QRect(510, 170, 83, 29))
        self.startDataButton = QPushButton(Widget)
        self.startDataButton.setObjectName(u"startDataButton")
        self.startDataButton.setGeometry(QRect(400, 210, 191, 31))
        self.stopDataButton = QPushButton(Widget)
        self.stopDataButton.setObjectName(u"stopDataButton")
        self.stopDataButton.setGeometry(QRect(400, 250, 191, 31))
        self.sensorValue = QLCDNumber(Widget)
        self.sensorValue.setObjectName(u"sensorValue")
        self.sensorValue.setGeometry(QRect(410, 310, 171, 51))
        self.status_label = QLabel(Widget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(370, 70, 381, 41))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.Button_Off.setText(QCoreApplication.translate("Widget", u"Button_OFF", None))
        self.Led_Off.setText(QCoreApplication.translate("Widget", u"LED_OFF", None))
        self.checkBlue.setText(QCoreApplication.translate("Widget", u"Blue (D4)", None))
        self.Led_On.setText(QCoreApplication.translate("Widget", u"LED_ON", None))
        self.Button_On.setText(QCoreApplication.translate("Widget", u"Button_ON", None))
        self.set_180.setText(QCoreApplication.translate("Widget", u"180", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Servo Control", None))
        self.checkYellow.setText(QCoreApplication.translate("Widget", u"Yellow (D8)", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Flash Control", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"LED Control", None))
        self.flashButton.setText(QCoreApplication.translate("Widget", u"Flash", None))
        self.browseButton.setText(QCoreApplication.translate("Widget", u"Browse", None))
        self.set_90.setText(QCoreApplication.translate("Widget", u"90", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Buzzer Control through push button", None))
        self.set_0.setText(QCoreApplication.translate("Widget", u"0", None))
        self.sketchPathEdit.setText(QCoreApplication.translate("Widget", u"Select Sketch File", None))
        self.flashStatusLabel.setText("")
        self.checkRed.setText(QCoreApplication.translate("Widget", u"Red (D13)", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"LDR Control", None))
        self.Light_sensor_On.setText(QCoreApplication.translate("Widget", u"LDR_On", None))
        self.Light_sensor_Off.setText(QCoreApplication.translate("Widget", u"LDR_OFF", None))
        self.startDataButton.setText(QCoreApplication.translate("Widget", u"Start Data Collection", None))
        self.stopDataButton.setText(QCoreApplication.translate("Widget", u"Stop Data Collection", None))
        self.status_label.setText(QCoreApplication.translate("Widget", u"Status", None))
    # retranslateUi

