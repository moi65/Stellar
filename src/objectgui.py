#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 Emilio Coppola
#
# This file is part of Stellar.
#
# Stellar is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Stellar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Stellar.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


import sys
import os
import shutil

import pygame.mixer
from PyQt4 import QtGui, QtCore


class ObjectGUI(QtGui.QWidget):
  
    def __init__(self, main, FileName, dirname):
        super(ObjectGUI, self).__init__(main)
        
        self.main = main
        self.dirname = dirname
        self.FileName = FileName
        self.initUI()

    def initUI(self):
        
        #Groupbox Container-----------------------------------

        self.ContainerGrid = QtGui.QGridLayout(self.main)
		
        self.LblName = QtGui.QLabel('Name:')
        self.nameEdit = QtGui.QLineEdit(self.FileName)

        self.LblSprite = QtGui.QLabel('Sprite:')
        self.SpriteCombo = QtGui.QComboBox()


        self.NameFrame = QtGui.QFrame()
        self.namelayout = QtGui.QGridLayout()
        self.namelayout.setMargin (0)
        self.namelayout.addWidget(self.LblName,0,0)
        self.namelayout.addWidget(self.nameEdit,0,1)
        self.namelayout.addWidget(self.LblSprite,1,0)
        self.namelayout.addWidget(self.SpriteCombo,1,1)
        
        self.NameFrame.setLayout(self.namelayout)


        
        
        self.cbvisible = QtGui.QCheckBox('Visible', self)
        self.cbsolid = QtGui.QCheckBox('Solid', self)
        self.cbpersis = QtGui.QCheckBox('Persistent', self)
        self.LblDepth = QtGui.QLabel('Depth:')
        self.depthEdit = QtGui.QLineEdit("0")
        self.LblParent = QtGui.QLabel('Parent:')
        self.ParentEdit = QtGui.QLineEdit()
        self.LblMask = QtGui.QLabel('Mask:')
        self.MaskEdit = QtGui.QLineEdit()
        self.Btninfo = QtGui.QPushButton("Show Information")
        self.Btninfo.setIcon(QtGui.QIcon(os.path.join('Data', 'info.png')))
        self.Btnok = QtGui.QPushButton("OK")
        self.Btnok.setIcon(QtGui.QIcon('Data/accept.png'))
        self.temporarything = QtGui.QScrollArea()
        self.temporarything1 = QtGui.QScrollArea()
        self.Btnaddevent = QtGui.QPushButton("Add Event")
        self.Btndelete = QtGui.QPushButton("Delete")
        self.Btnchange = QtGui.QPushButton("Change")
        
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        
        self.ContainerGrid.setSpacing(5)
        self.ContainerGrid.addWidget(self.NameFrame, 0, 0, 1, 2)
        #self.ContainerGrid.addWidget(self.SpriteFrame, 1, 0, 1, 2)
        self.ContainerGrid.addWidget(self.cbvisible, 2, 0)
        self.ContainerGrid.addWidget(self.cbsolid, 2, 1)
        self.ContainerGrid.addWidget(self.cbpersis, 3, 0)
        self.ContainerGrid.addWidget(self.LblDepth, 4, 0)
        self.ContainerGrid.addWidget(self.depthEdit, 4, 1)
        self.ContainerGrid.addWidget(self.LblParent, 5, 0)
        self.ContainerGrid.addWidget(self.ParentEdit, 5, 1)
        self.ContainerGrid.addWidget(self.LblMask, 6, 0)
        self.ContainerGrid.addWidget(self.MaskEdit, 6, 1)
        self.ContainerGrid.addItem(spacerItem)
        self.ContainerGrid.addWidget(self.Btninfo, 7, 0, 1, 2)
        self.ContainerGrid.addWidget(self.Btnok, 8, 0,1,2)
        #---
        self.ContainerGrid.addWidget(self.temporarything, 0, 2,2,7)
        self.ContainerGrid.addWidget(self.Btnaddevent, 2, 2,2,3)
        self.ContainerGrid.addWidget(self.Btndelete, 11, 2)
        self.ContainerGrid.addWidget(self.Btnchange, 11, 3)

        #---
        self.ContainerGrid.addWidget(self.temporarything1, 0, 4,2,7)

        #self.startopen()
