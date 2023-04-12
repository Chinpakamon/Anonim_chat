import os
import sys
import rsa
import time
import shelve
import socket
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from des import *

# Мониторинг входящих сообщений
class message_monitor(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __ini__(self, server_socket, private_key, parent=None):
        pass