#!/usr/bin/env python3

import RPi.GPIO as GPIO
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import time
import math

unit = 0.1
led1 = 17
morse = {
    'a': 12,
    'b': 2111,
    'c': 2121,
    'd': 211,
    'e': 1,
    'f': 1121,
    'g': 221,
    'h': 1111,
    'i': 11,
    'j': 1222,
    'k': 212,
    'l': 1211,
    'm': 22,
    'n': 21,
    'o': 222,
    'p': 1221,
    'q': 2212,
    'r': 121,
    's': 111,
    't': 2,
    'u': 112,
    'v': 1112,
    'w': 122,
    'x': 2112,
    'y': 2122,
    'z': 2211,
    '0': 22222,
    '1': 12222,
    '2': 11222,
    '3': 11122,
    '4': 11112,
    '5': 11111,
    '6': 21111,
    '7': 22111,
    '8': 22211,
    '9': 22221,
    '\'': 122221,
    '-': 211112
}

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 320, 250)
    win.setWindowTitle("5-3D")

    field = QtWidgets.QLineEdit(win)
    field.setGeometry(60, 50, 200, 30)
    field.setMaxLength(12)
    field.returnPressed.connect(lambda:send(field.text()))

    button = QtWidgets.QPushButton("Send", win)
    button.setGeometry(110, 100, 100, 30)
    button.pressed.connect(lambda:send(field.text()))

    win.show()
    sys.exit(app.exec_())


def send(message):
    for m in message.lower():
        if (m == ' '):
            time.sleep(4*unit)
        elif m in morse:
            encode(morse[m])
            time.sleep(2*unit)

    time.sleep(4*unit)


def encode(number):
    if (number >= 10):
        encode(math.floor(number / 10))

    if (number % 10 == 1):
        dot()
    elif (number % 10 == 2):
        dash()


def dot():
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(unit)
    GPIO.output(led1, GPIO.LOW)
    time.sleep(unit)


def dash():
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(3*unit)
    GPIO.output(led1, GPIO.LOW)
    time.sleep(unit)


try:
    window()
finally:
    GPIO.cleanup()

