#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

welcome_page

The welcome page for the main window.

Key components handled within.
 * being pretty and welcoming to new users

"""

#Standard Library Imports
import logging

#PyQt imports
from PyQt4 import QtCore
from PyQt4 import QtGui

from commotion_client.GUI.ui import Ui_welcome_page

class ViewPort(Ui_welcome_page.ViewPort):
    """
    """
    start_report_collection = QtCore.pyqtSignal()
    data_report = QtCore.pyqtSignal(str, dict)
    error_report = QtCore.pyqtSignal(str)
    on_stop = QtCore.pyqtSignal()

    
    def __init__(self, parent=None):
        super().__init__()
        self.log = logging.getLogger("commotion_client."+__name__)
        self.setupUi(self) #run setup function from Ui_main_window
        self._dirty = False

    @property
    def is_dirty(self):
        """The current state of the viewport object """
        return self._dirty
        
    def clean_up(self):
        self.on_stop.emit()

