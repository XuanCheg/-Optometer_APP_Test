import sys
from random import randint

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QMainWindow, QProgressBar, QDesktopWidget, QMessageBox,
                             QTextBrowser, QLabel, QGraphicsView, QGraphicsPixmapItem, QGraphicsScene)

import optometer

# 图片缩放稍后再做

data = optometer.Optometer()


def randomgraph():
    random_dir = randint(1, 4)
    return random_dir


def img_Product(graph: str, dio: str):
    img = QPixmap()
    path = graph + dio
    img.load(path)
    return img


class Ui_Mainwindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.textBrowser = None
        self.scene = None
        self.OptometerShow = None
        self.ProgressBarRight = None
        self.ProgressBarWrong = None
        self.rand_dir = 0

        self.initUI()

    def initUI(self):
        up = QPushButton("up", self)
        up.setGeometry(QtCore.QRect(14, 420, 91, 51))
        down = QPushButton("down", self)
        down.setGeometry(QtCore.QRect(114, 420, 91, 51))
        left = QPushButton("left", self)
        left.setGeometry(QtCore.QRect(210, 420, 91, 51))
        right = QPushButton("right", self)
        right.setGeometry(QtCore.QRect(314, 420, 91, 51))
        clear = QPushButton("clear", self)
        clear.setGeometry(QtCore.QRect(70, 480, 91, 51))
        unclear = QPushButton("unclear", self)
        unclear.setGeometry(QtCore.QRect(260, 480, 91, 51))
        self.ProgressBarWrong = QProgressBar(self)
        self.ProgressBarWrong.setGeometry(QtCore.QRect(580, 70, 171, 31))
        self.ProgressBarWrong.setRange(0, 5)
        self.ProgressBarWrong.setValue(0)
        self.ProgressBarRight = QProgressBar(self)
        self.ProgressBarRight.setGeometry(QtCore.QRect(580, 160, 171, 31))
        self.ProgressBarRight.setRange(0, 5)
        self.ProgressBarRight.setValue(0)
        lbl_wrong = QLabel(self)
        lbl_wrong.setGeometry(QtCore.QRect(500, 70, 71, 31))
        lbl_wrong.setText("WRONG")
        lbl_right = QLabel(self)
        lbl_right.setGeometry(QtCore.QRect(500, 160, 71, 31))
        lbl_right.setText("RIGHT")
        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(480, 220, 256, 192))
        self.OptometerShow = QGraphicsView(self)
        self.OptometerShow.setGeometry(QtCore.QRect(0, 0, 421, 411))
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 400, 400)
        self.rand_dir = randomgraph()
        self.scene.addPixmap(img_Product("4.6\\", data.Graph[self.rand_dir - 1]))
        self.OptometerShow.setScene(self.scene)
        up.clicked.connect(self.buttonClicked)
        down.clicked.connect(self.buttonClicked)
        left.clicked.connect(self.buttonClicked)
        right.clicked.connect(self.buttonClicked)
        clear.clicked.connect(self.buttonClicked)
        unclear.clicked.connect(self.buttonClicked)

        self.statusBar()
        self.resize(800, 600)
        self.center()
        self.setWindowTitle('Optometer')
        self.setWindowIcon(QIcon("icon.png"))

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, "消息", "你确定要退出吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.ignore()
        else:
            event.ignore()

    def buttonClicked(self):
        sender = self.sender()
        optometer.check(data, self.rand_dir, sender.text(), data.data_set)
        if data.data_set["flag"] == 3:
            data.data_set["diopter"] += 1
            optometer.reset(data.data_set)

        rate = optometer.count_rate(data.data_set)

        if rate > 0.6 and data.data_set["count"] % 5 == 0:
            data.data_set["diopter"] += 1
            optometer.reset(data.data_set)
            data.data_set["break_condition"] = 1
        elif 0.6 > rate >= 0 == data.data_set["count"] % 5:
            data.data_set["diopter"] -= 1
            if data.data_set["break_condition"] == 1:
                tmp1 = str(data.eye_chart_new[data.data_set["diopter"]])
                tmp2 = str(data.eye_chart_old[data.data_set["diopter"]])
                text1 = "您的视力为五分计数" + tmp1 + "度", "您的视力为小数计数" + tmp2 + "度"
                text = text1[0] + text1[1]
                self.textBrowser.setText(text)
                return
            optometer.reset(data.data_set)
        self.ProgressBarWrong.setValue(data.data_set["wrong"])
        self.ProgressBarRight.setValue(data.data_set["correct"])
        self.rand_dir = randomgraph()
        self.scene.addPixmap(img_Product("4.6\\", data.Graph[self.rand_dir - 1]))
        self.OptometerShow.setScene(self.scene)
