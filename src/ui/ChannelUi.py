# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChannelUi.ui'
#
# Created: Mon Apr 28 06:30:04 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Channel(object):
    def setupUi(self, Channel):
        Channel.setObjectName(_fromUtf8("Channel"))
        Channel.resize(303, 350)
        self.gridLayout = QtGui.QGridLayout(Channel)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(Channel)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 0, 2, 5, 1)
        spacerItem = QtGui.QSpacerItem(0, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 5, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(0, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 5, 1)
        self.line_3 = QtGui.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 0, 7, 5, 1)
        self.spin_set = QtGui.QSpinBox(self.groupBox)
        self.spin_set.setMaximum(250)
        self.spin_set.setObjectName(_fromUtf8("spin_set"))
        self.gridLayout_2.addWidget(self.spin_set, 4, 3, 1, 1)
        self.lbl_imon = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_imon.sizePolicy().hasHeightForWidth())
        self.lbl_imon.setSizePolicy(sizePolicy)
        self.lbl_imon.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lbl_imon.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_imon.setObjectName(_fromUtf8("lbl_imon"))
        self.gridLayout_2.addWidget(self.lbl_imon, 0, 6, 2, 1)
        self.lbl_pmon = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_pmon.sizePolicy().hasHeightForWidth())
        self.lbl_pmon.setSizePolicy(sizePolicy)
        self.lbl_pmon.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lbl_pmon.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pmon.setObjectName(_fromUtf8("lbl_pmon"))
        self.gridLayout_2.addWidget(self.lbl_pmon, 0, 8, 2, 1)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 0, 4, 5, 1)
        self.lbl_set = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_set.sizePolicy().hasHeightForWidth())
        self.lbl_set.setSizePolicy(sizePolicy)
        self.lbl_set.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lbl_set.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_set.setObjectName(_fromUtf8("lbl_set"))
        self.gridLayout_2.addWidget(self.lbl_set, 0, 3, 2, 1)
        self.lbl_max = QtGui.QLabel(self.groupBox)
        self.lbl_max.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_max.setObjectName(_fromUtf8("lbl_max"))
        self.gridLayout_2.addWidget(self.lbl_max, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.slider_iset = QtGui.QSlider(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_iset.sizePolicy().hasHeightForWidth())
        self.slider_iset.setSizePolicy(sizePolicy)
        self.slider_iset.setMaximum(250)
        self.slider_iset.setOrientation(QtCore.Qt.Vertical)
        self.slider_iset.setObjectName(_fromUtf8("slider_iset"))
        self.horizontalLayout_3.addWidget(self.slider_iset)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 3, 2, 1)
        self.radio_CP = QtGui.QRadioButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_CP.sizePolicy().hasHeightForWidth())
        self.radio_CP.setSizePolicy(sizePolicy)
        self.radio_CP.setObjectName(_fromUtf8("radio_CP"))
        self.gridLayout_2.addWidget(self.radio_CP, 4, 8, 1, 1)
        self.radio_CC = QtGui.QRadioButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_CC.sizePolicy().hasHeightForWidth())
        self.radio_CC.setSizePolicy(sizePolicy)
        self.radio_CC.setObjectName(_fromUtf8("radio_CC"))
        self.gridLayout_2.addWidget(self.radio_CC, 4, 6, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.slider_imax = QtGui.QSlider(self.groupBox)
        self.slider_imax.setMaximum(250)
        self.slider_imax.setOrientation(QtCore.Qt.Vertical)
        self.slider_imax.setObjectName(_fromUtf8("slider_imax"))
        self.horizontalLayout_4.addWidget(self.slider_imax)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.progbar_imon = QtGui.QProgressBar(self.groupBox)
        self.progbar_imon.setMaximum(250)
        self.progbar_imon.setProperty("value", 0)
        self.progbar_imon.setOrientation(QtCore.Qt.Vertical)
        self.progbar_imon.setObjectName(_fromUtf8("progbar_imon"))
        self.horizontalLayout_5.addWidget(self.progbar_imon)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 6, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.progbar_pmon = QtGui.QProgressBar(self.groupBox)
        self.progbar_pmon.setMaximum(250)
        self.progbar_pmon.setProperty("value", 0)
        self.progbar_pmon.setOrientation(QtCore.Qt.Vertical)
        self.progbar_pmon.setObjectName(_fromUtf8("progbar_pmon"))
        self.horizontalLayout_6.addWidget(self.progbar_pmon)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 2, 8, 1, 1)
        self.spin_max = QtGui.QSpinBox(self.groupBox)
        self.spin_max.setMaximum(250)
        self.spin_max.setObjectName(_fromUtf8("spin_max"))
        self.gridLayout_2.addWidget(self.spin_max, 4, 1, 1, 1)
        self.lbl_limit_dbg = QtGui.QLabel(self.groupBox)
        self.lbl_limit_dbg.setObjectName(_fromUtf8("lbl_limit_dbg"))
        self.gridLayout_2.addWidget(self.lbl_limit_dbg, 5, 1, 1, 1)
        self.lbl_set_dbg = QtGui.QLabel(self.groupBox)
        self.lbl_set_dbg.setObjectName(_fromUtf8("lbl_set_dbg"))
        self.gridLayout_2.addWidget(self.lbl_set_dbg, 5, 3, 1, 1)
        self.lbl_imon_dbg = QtGui.QLabel(self.groupBox)
        self.lbl_imon_dbg.setObjectName(_fromUtf8("lbl_imon_dbg"))
        self.gridLayout_2.addWidget(self.lbl_imon_dbg, 5, 6, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Channel)
        QtCore.QMetaObject.connectSlotsByName(Channel)

    def retranslateUi(self, Channel):
        Channel.setWindowTitle(_translate("Channel", "Form", None))
        self.groupBox.setTitle(_translate("Channel", "Channel [n]", None))
        self.spin_set.setSuffix(_translate("Channel", "mA", None))
        self.lbl_imon.setText(_translate("Channel", "<html><head/><body><p>I<span style=\" vertical-align:sub;\">mon</span></p></body></html>", None))
        self.lbl_pmon.setText(_translate("Channel", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">mon</span></p></body></html>", None))
        self.lbl_set.setText(_translate("Channel", "<html><head/><body><p>I<span style=\" vertical-align:sub;\">Set</span></p></body></html>", None))
        self.lbl_max.setText(_translate("Channel", "<html><head/><body><p>I<span style=\" vertical-align:sub;\">max</span></p></body></html>", None))
        self.radio_CP.setToolTip(_translate("Channel", "Enable constant-power mode", None))
        self.radio_CP.setText(_translate("Channel", "CP", None))
        self.radio_CC.setToolTip(_translate("Channel", "Enable constant-current mode", None))
        self.radio_CC.setText(_translate("Channel", "CC", None))
        self.progbar_imon.setFormat(_translate("Channel", "%v mA", None))
        self.progbar_pmon.setFormat(_translate("Channel", "%v mW", None))
        self.spin_max.setSuffix(_translate("Channel", "mA", None))
        self.lbl_limit_dbg.setText(_translate("Channel", "TextLabel", None))
        self.lbl_set_dbg.setText(_translate("Channel", "TextLabel", None))
        self.lbl_imon_dbg.setText(_translate("Channel", "TextLabel", None))

