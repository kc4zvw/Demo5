#!/usr/bin/env python2.7
#
# $Id: qt_101.py,v 0.2 2016/06/28 13:42:01 kc4zvw Exp kc4zvw $
#
# vim: ts=4:

import sys

from PyQt4 import QtGui, QtCore

#class PrettyGui(QtGui.QWidget):  <-- we changed to QMainWindow for a status bar
class PrettyGui(QtGui.QMainWindow):
    """ Make it Object Oriented """
    def __init__(self):
        super(PrettyGui, self).__init__() # Python2 call base class
        self._init_ui()

    def _init_ui(self):
        """ Setup how our dialog """

        main_widget = QtGui.QWidget()
        self.setCentralWidget(main_widget)
        self.setWindowTitle("Hello World")

        #widget.move(300, 300)

        # Set absolute window size and position
        #self.setGeometry(300, 300, 250, 150)

        self.resize(250, 250)
        self.center()

        exit_action = QtGui.QAction(QtGui.QIcon('exit.png'),
                                                'E&xit',
                                                self)
        exit_action.setShortcut('Ctrl+X')
        exit_action.setStatusTip('Exit the app')
        exit_action.triggered.connect(self.close)
        #exit_action.triggered.connect(QtGui.qApp.quit)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)

        self.stats_bar = self.statusBar()
        self.stats_bar.showMessage("Are you ready for some QT!")
        
        self.text_edit = QtGui.QTextEdit()
        self.text_edit.setText("Hello World from Python/Qt")
        #self.setCentralWidget(text_edit)

        quit_button = QtGui.QPushButton('&Quit')
        quit_button.setToolTip("Quit the application")
        quit_button.resize(quit_button.sizeHint())
        #quit_button.resize(50, 50)
        #quit_button.move(0, 50)

        quit_button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        label = QtGui.QLabel('Special label')
        lcd = QtGui.QLCDNumber()
        lcd.setSegmentStyle(QtGui.QLCDNumber.Flat)
        #QLCDNumber{color:rgb(85, 85, 255);background-color:rgb(0, 170, 255);}
        # get the palette
        palette = lcd.palette()

        # foreground color
        palette.setColor(palette.WindowText, QtGui.QColor(85, 85, 255))
        # background color
        palette.setColor(palette.Background, QtGui.QColor(0, 170, 255))
        # "light" border
        palette.setColor(palette.Light, QtGui.QColor(255, 0, 0))
        # "dark" border
        palette.setColor(palette.Dark, QtGui.QColor(0, 255, 0))

        # set the palette
        lcd.setPalette(palette)

        slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        slider.valueChanged.connect(lcd.display)
        slider.valueChanged.connect(self.slide_me)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(lcd)
        vbox.addWidget(slider)
        vbox.addWidget(self.text_edit)
        vbox.addWidget(quit_button)

        main_widget.setLayout(vbox)

        # This is critical
        self.show()

    def slide_me(self, value):
        current_size = self.frameSize()
        self.text_edit.setText("Too low level is " + str(value))
        self.stats_bar.showMessage("It's current raining outside: {0}".format(value))
        #self.resize(current_size.width() + value, current_size.height())

    def center(self):
        """Automatically center dialog to available Geometry"""
        current_rect = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        current_rect.moveCenter(cp)
        self.move(current_rect.topLeft())

    def closeEvent(self, event):
        """QT: Trigger on the [X] close"""
        reply = QtGui.QMessageBox.question(self,
            'Finished?',
            'Are you really sure?',
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
            QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


""" ============================================================ """

def main():
    """ Main Driver for PrettyGui """
    app = QtGui.QApplication(sys.argv)
    prettygui = PrettyGui()
    exit_code = app.exec_()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()

# End of Script
