#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 4/8/14 2:14 PM 2013
@author: <'Ronny Eichler'> ronny.eichler@gmail.com

"""

import sys
import logging
from PyQt4 import QtGui, QtCore
from ui import MainWindowUi, icons_rc
from ui.ChannelWidget import ChannelWidget
from core.fl593fl import FL593FL
# try:
#     from lib.pyqtgraph import QtGui, QtCore  # ALL HAIL LUKE!
#     import lib.pyqtgraph as pg
# except ImportError:
#     pg = None

NO_EXIT_CONFIRMATION = False
__version__ = '0.1'


class Main(QtGui.QMainWindow):
    _device_ref = None

    def __init__(self, app, *args, **kwargs):
        QtGui.QMainWindow.__init__(self)
        self.log = logging.getLogger(__name__)
        self.app = app
        self.ui = MainWindowUi.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionReset.triggered.connect(self.reset_device)
        self.connect(self.ui.actionQuit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        # Channel widgets
        self.channel_widgets = []

        # Control widget
        self.ui.push_REN.toggled.connect(self.toggle_remote_enable)

        self.stopwatch = QtCore.QElapsedTimer()
        self.stopwatch.start()
        self.gui_refresh_interval = 16  # conservative 100 ms for starters, aka 10 Hz refresh rate
        self.elapsed = self.gui_refresh_interval if self.gui_refresh_interval > 0 else 30
        QtCore.QTimer.singleShot(0, self.initialize)  # fires when event loop starts

    def initialize(self):
        """Set up device and representations once UI was initiated."""
        self.log.debug("Initializing...")

        if self._device_ref is None:
            try:
                self._device_ref = FL593FL()
            except Exception, e:
                raise e

        assert self.device is not None

        self.channel_widgets = [ChannelWidget(self, n) for n in range(1, self.device.channel_count+1)]
        for widget in self.channel_widgets:
            self.ui.layout_channels.addWidget(widget)
            widget.initialize(self.device.channels[widget.num_channel])

        if self.device.model is not None:
            self.ui.lbl_dev_name.setText(self.device.model)
        if self.device.fwver is not None:
            self.ui.lbl_fw_ver.setText(self.device.fwver)
        if self.device.serial is not None:
            self.ui.lbl_serial_num.setText(self.device.serial)

        if self.device is not None:
            # start main refresh loop
            self.refresh()

    def refresh(self):
        """Main loop processing/updating."""

        # update rate display (smoothed)
        self.elapsed = 0.8*self.elapsed + 0.2*self.stopwatch.restart()
        self.ui.lbl_fps.setText('{0:.0f} Hz'.format(1000./self.elapsed))

        # have the device update itself
        self.device.update()

        # Control channel items
        self.refresh_enable_flags()

        # Laser channel widgets
        for widget in self.channel_widgets:
            widget.refresh()

        # start timer for next refresh
        #self.log.debug('Next loop shot')
        QtCore.QTimer.singleShot(self.gui_refresh_interval, self.refresh)

    def refresh_enable_flags(self):
        """Update enable flag indicators for local, external and remote flags."""
        #self.log.debug('Refreshing enable flags')

        self.toggle_laser_warning(self.device.control.output_enable)

        self.set_enable_icon(self.ui.lbl_external_icon, self.device.control.external_enable)
        self.set_enable_icon(self.ui.lbl_output_icon, self.device.control.output_enable)
        self.set_enable_icon(self.ui.lbl_local_icon, self.device.control.local_enable)
        self.ui.push_REN.setChecked(self.device.control.remote_enable)

    @property
    def device(self):
        """Getter for device handle."""
        return self._device_ref

    def reset_device(self):
        """Reset device (bus). """
        self.device.reset()

    def toggle_remote_enable(self, state):
        """Toggle the state of the remote enable flag when toggling the checkbutton."""
        self.log.info('Setting remote enable {0:s}'.format('ON' if state else 'OFF'))
        self.device.control.remote_enable = state

    def toggle_laser_warning(self, state):
        if self.ui.lbl_laser_warning.isEnabled() != state:
            self.ui.lbl_laser_warning.setEnabled(state)

    @staticmethod
    def set_enable_icon(widget, state):
        """Set pixmap of label with ON or OFF marker from the icons_rc.qrc file.

        Imported from ui.icons_rc."""
        #self.log.debug('Setting flag {0:b} for {1:s}'.format(state, str(widget)))
        if state:
            widget.setPixmap(QtGui.QPixmap(MainWindowUi._fromUtf8(":/icons/enabled_true.png")))
        else:
            widget.setPixmap(QtGui.QPixmap(MainWindowUi._fromUtf8(":/icons/enabled_false.png")))

    def closeEvent(self, event):
        """This party sucks. The moment I find my pants I'm out of here!"""
        if NO_EXIT_CONFIRMATION:
            reply = QtGui.QMessageBox.Yes
        else:
            reply = QtGui.QMessageBox.question(self, 'Exiting...', 'Are you sure?',
                                               QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            if self.device is not None:
                self.device.close()
            event.accept()
        else:
            event.ignore()


#############################################################
def main(*args, **kwargs):
    app = QtGui.QApplication([])
    # identifiers for QSettings persistent application settings
    app.setOrganizationName('battaglia_lab')
    app.setOrganizationDomain('science.ru.nl')
    app.setApplicationName('FL593FL')

    window = Main(app, *args, **kwargs)
    window.show()
    window.raise_()  # needed on OSX?

    sys.exit(app.exec_())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Command line parsing
    import argparse
    parser = argparse.ArgumentParser(prog='PyFL593FL Qt GUI')
    parser.add_argument('-d', '--DEBUG', action='store_true', 
                        help='Debug mode. Actually, only disables exit confirmation.')
    parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=__version__))
    cli_args = parser.parse_args()

    if cli_args.DEBUG:
        NO_EXIT_CONFIRMATION = True 

    # Let's roll
    main()