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

		self.toolbar = QToolBar();
		self.toolbar.addAction(QIcon.fromTheme('list-add'), 'Add Videos')
		self.toolbar.addAction(QIcon.fromTheme('edit-clear'), 'Clear Video List')
		self.help = QLabel('Welcome to Video Splitter. To get started, add videos to the list using the button above.')
		self.fileListView = QListView()
		self.logText = QTextEdit();
		self.button = QPushButton('Split videos into frames')

		self.vbox.addWidget(self.toolbar)
		self.vbox.addWidget(self.help)
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
		self.layout.toolbar.actionTriggered.connect(self.actionClicked)

		self.setCentralWidget(self.layout)
		self.statusBar()

		self.errorDialog = QMessageBox(2, 'Can\'t write frames', 'The folder in which one or more of your videos resides is not writeable. Please check you own the folder, and it is not read-only.')

		self.setGeometry(450, 100, 800, 700)
		self.setWindowTitle('Video Splitter')
		self.show()

	def actionClicked(self, action):
		a = action.text()
		if a == 'Add Videos':
			self.showDialog()
		elif a == 'Clear Video List':
			self.clearList()

	def clearList(self):
		self.model.clear()

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
			f = self.model.item(i)

			if f.checkState() != 2:
				continue;

			fin = f.text()

			outdir = str(fin)+'-frames'
			fname = '%s-image%%03d.jpg' % fin
			print outdir
			print os.path.isdir(outdir)
			if not os.path.isdir(outdir):
				try:
					os.mkdir(outdir)
				except OSError:
					if not os.path.isdir(outdir):
						self.showPermissionDialog()
						raise

			print fname

			# QProcess object for external ffmpeg/avconv command
			self.process = QProcess(self)
			# Just to prevent accidentally running multiple times
			# Disable the button when process starts, and enable it when it finishes
			self.process.started.connect(lambda: self.layout.button.setEnabled(False))
			self.process.finished.connect(lambda: self.layout.button.setEnabled(True))
			# QProcess emits signals when there is output to be read
			self.process.readyReadStandardOutput.connect(self.writeLog)
			self.process.readyReadStandardError.connect(self.writeLog)

			self.process.start('avconv', ['-i', fin, '-r', '1', os.path.join(outdir, fname)])

	def showPermissionDialog(self):
		self.errorDialog.show()

	def writeLog(self):
		self.layout.logText.append(str(self.process.readAllStandardOutput()))
		self.layout.logText.append(str(self.process.readAllStandardError()))

	def confirmQuit(self):
		self.quit()

	def quit(self):
		sys.exit()


def main():

	app = QApplication(sys.argv)
	ex = VideoSplitter()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
