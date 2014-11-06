#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import signal
import os
import subprocess
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class FormWidget(QWidget):

	def __init__(self, parent):
		super(FormWidget, self).__init__(parent)
		self.__layout()

	def __layout(self):
		self.vbox = QVBoxLayout()
		
		self.logText = QTextEdit();
		self.fileListView = QListView()
		self.button = QPushButton('Split videos into frames')

		self.vbox.addWidget(self.fileListView)
		self.vbox.addWidget(self.logText)
		self.vbox.addWidget(self.button)
		self.setLayout(self.vbox)


class VideoSplitter(QMainWindow):

	def __init__(self):
		super(VideoSplitter, self).__init__()
		
		self.initUI()
		
	def initUI(self):      

		self.layout = FormWidget(self)

		self.layout.button.clicked.connect(self.doSplitting)

		self.setCentralWidget(self.layout)
		self.statusBar()

		openFile = QAction(QIcon('open.png'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open new File')
		openFile.triggered.connect(self.showDialog)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)
		
		self.setGeometry(450, 100, 800, 700)
		self.setWindowTitle('Video Splitter')
		self.show()

		
	def showDialog(self):

		fnames = QFileDialog.getOpenFileNames(self, 'Open file', os.environ['HOME'])
		self.model = QStandardItemModel()
		
		self.fileCount = 0
		for fname in fnames:
			item = QStandardItem()
			item.setText(fname)
			item.setCheckable(True)
			item.setCheckState(2)
			self.model.appendRow(item)
			self.fileCount += 1

		self.layout.fileListView.setModel(self.model)

	def doSplitting(self):
		for i in range(0, self.fileCount):
			f = self.model.item(i).text()

			# QProcess object for external ffmpeg/avconv command
	        self.process = QProcess(self)
	        # Just to prevent accidentally running multiple times
	        # Disable the button when process starts, and enable it when it finishes
	        self.process.started.connect(lambda: self.layout.button.setEnabled(False))
	        self.process.finished.connect(lambda: self.layout.button.setEnabled(True))
	        # QProcess emits signals when there is output to be read
	        self.process.readyReadStandardOutput.connect(self.writeLog)
	        self.process.readyReadStandardError.connect(self.writeLog)

	        self.process.start('avconv', ['-i', f, '-r', '1', 'image%03d.jpg'])

	def writeLog(self):
		self.layout.logText.append(str(self.process.readAllStandardOutput()))
		self.layout.logText.append(str(self.process.readAllStandardError()))


def main():
	
	app = QApplication(sys.argv)
	ex = VideoSplitter()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
