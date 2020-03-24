# Copyright (c) 2018 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Hook that gets executed every time a new Toolkit API instance is created.
"""

from sgtk import LogManager
from tank import Hook
import sys

log = LogManager.get_logger(__name__)


class TankInit(Hook):
    def execute(self, **kwargs):
        """
        Executed when a new Toolkit API instance is initialized.

        You can access the Toolkit API instance through ``self.parent``.

        The default implementation does nothing.
        """
        pass
        
        # tk = self.sgtk

        # log.debug(tk.project_path)
        
        # log.debug(tk.roots['primary'])
        # tk.roots['primary'] = 'D:\\'
        # log.debug(tk.roots)

        # log.debug('################################################################################### tank')
        # log.debug('################################################################################### tank')
        # log.debug('################################################################################### tank')
        # log.debug('################################################################################### tank')
        # log.debug('################################################################################### tank')
        # log.debug('################################################################################### tank')
        # log.debug('################################################################################### tank')
