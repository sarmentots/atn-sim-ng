# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wnd_main_atn_sim.ui'
#
# Created: Fri May  5 10:36:27 2017
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

class Ui_CWndMainATNSim(object):
    def setupUi(self, CWndMainATNSim):
        CWndMainATNSim.setObjectName(_fromUtf8("CWndMainATNSim"))
        CWndMainATNSim.resize(439, 210)
        self.centralwidget = QtGui.QWidget(CWndMainATNSim)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frm_title = QtGui.QFrame(self.centralwidget)
        self.frm_title.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 255);"))
        self.frm_title.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frm_title.setFrameShadow(QtGui.QFrame.Raised)
        self.frm_title.setObjectName(_fromUtf8("frm_title"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frm_title)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lbl_01 = QtGui.QLabel(self.frm_title)
        self.lbl_01.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 255);"))
        self.lbl_01.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_01.setObjectName(_fromUtf8("lbl_01"))
        self.verticalLayout_2.addWidget(self.lbl_01)
        self.lbl_02 = QtGui.QLabel(self.frm_title)
        self.lbl_02.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 255);"))
        self.lbl_02.setObjectName(_fromUtf8("lbl_02"))
        self.verticalLayout_2.addWidget(self.lbl_02)
        self.verticalLayout.addWidget(self.frm_title)
        CWndMainATNSim.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(CWndMainATNSim)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSimulation = QtGui.QMenu(self.menubar)
        self.menuSimulation.setObjectName(_fromUtf8("menuSimulation"))
        self.menuConfiguration = QtGui.QMenu(self.menubar)
        self.menuConfiguration.setObjectName(_fromUtf8("menuConfiguration"))
        self.menuRuntime = QtGui.QMenu(self.menubar)
        self.menuRuntime.setObjectName(_fromUtf8("menuRuntime"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        CWndMainATNSim.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CWndMainATNSim)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CWndMainATNSim.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(CWndMainATNSim)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        CWndMainATNSim.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.act_edit_scenario = QtGui.QAction(CWndMainATNSim)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/network-workgroup.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_edit_scenario.setIcon(icon)
        self.act_edit_scenario.setObjectName(_fromUtf8("act_edit_scenario"))
        self.act_start_session = QtGui.QAction(CWndMainATNSim)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/start-session-2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/start-session-1.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.act_start_session.setIcon(icon1)
        self.act_start_session.setObjectName(_fromUtf8("act_start_session"))
        self.act_stop_session = QtGui.QAction(CWndMainATNSim)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/stop-session.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.act_stop_session.setIcon(icon2)
        self.act_stop_session.setObjectName(_fromUtf8("act_stop_session"))
        self.act_start_dump1090 = QtGui.QAction(CWndMainATNSim)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/dump1090.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.act_start_dump1090.setIcon(icon3)
        self.act_start_dump1090.setObjectName(_fromUtf8("act_start_dump1090"))
        self.act_start_visil = QtGui.QAction(CWndMainATNSim)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/visil.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.act_start_visil.setIcon(icon4)
        self.act_start_visil.setObjectName(_fromUtf8("act_start_visil"))
        self.act_quit = QtGui.QAction(CWndMainATNSim)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/quit.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.act_quit.setIcon(icon5)
        self.act_quit.setObjectName(_fromUtf8("act_quit"))
        self.act_db_edit = QtGui.QAction(CWndMainATNSim)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/db_edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.act_db_edit.setIcon(icon6)
        self.act_db_edit.setObjectName(_fromUtf8("act_db_edit"))
        self.act_scenario_to_xml = QtGui.QAction(CWndMainATNSim)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/scenario-to-xml.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.act_scenario_to_xml.setIcon(icon7)
        self.act_scenario_to_xml.setObjectName(_fromUtf8("act_scenario_to_xml"))
        self.act_scenario_to_exe = QtGui.QAction(CWndMainATNSim)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/scenario-to-exe.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.act_scenario_to_exe.setIcon(icon8)
        self.act_scenario_to_exe.setObjectName(_fromUtf8("act_scenario_to_exe"))
        self.act_add_aircraft = QtGui.QAction(CWndMainATNSim)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/add_aircraft.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.act_add_aircraft.setIcon(icon9)
        self.act_add_aircraft.setObjectName(_fromUtf8("act_add_aircraft"))
        self.act_show_manual = QtGui.QAction(CWndMainATNSim)
        self.act_show_manual.setObjectName(_fromUtf8("act_show_manual"))
        self.act_about = QtGui.QAction(CWndMainATNSim)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/help-about.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.act_about.setIcon(icon10)
        self.act_about.setObjectName(_fromUtf8("act_about"))
        self.act_start_pilot = QtGui.QAction(CWndMainATNSim)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/pilot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/pilot-military.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.act_start_pilot.setIcon(icon11)
        self.act_start_pilot.setObjectName(_fromUtf8("act_start_pilot"))
        self.menuSimulation.addAction(self.act_edit_scenario)
        self.menuSimulation.addSeparator()
        self.menuSimulation.addAction(self.act_start_session)
        self.menuSimulation.addAction(self.act_stop_session)
        self.menuSimulation.addSeparator()
        self.menuSimulation.addAction(self.act_start_dump1090)
        self.menuSimulation.addAction(self.act_start_visil)
        self.menuSimulation.addAction(self.act_start_pilot)
        self.menuSimulation.addSeparator()
        self.menuSimulation.addAction(self.act_quit)
        self.menuConfiguration.addAction(self.act_db_edit)
        self.menuConfiguration.addSeparator()
        self.menuConfiguration.addAction(self.act_scenario_to_xml)
        self.menuConfiguration.addAction(self.act_scenario_to_exe)
        self.menuRuntime.addAction(self.act_add_aircraft)
        self.menuHelp.addAction(self.act_show_manual)
        self.menuHelp.addAction(self.act_about)
        self.menubar.addAction(self.menuSimulation.menuAction())
        self.menubar.addAction(self.menuConfiguration.menuAction())
        self.menubar.addAction(self.menuRuntime.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.act_edit_scenario)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_start_session)
        self.toolBar.addAction(self.act_stop_session)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_start_dump1090)
        self.toolBar.addAction(self.act_start_visil)
        self.toolBar.addAction(self.act_start_pilot)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_db_edit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_scenario_to_xml)
        self.toolBar.addAction(self.act_scenario_to_exe)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_add_aircraft)

        self.retranslateUi(CWndMainATNSim)
        QtCore.QMetaObject.connectSlotsByName(CWndMainATNSim)

    def retranslateUi(self, CWndMainATNSim):
        CWndMainATNSim.setWindowTitle(_translate("CWndMainATNSim", "ATN Simulator", None))
        self.lbl_01.setText(_translate("CWndMainATNSim", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:16pt; font-weight:600; color:#ffff00;\">ATN SIMULATOR</span></p></body></html>", None))
        self.lbl_02.setText(_translate("CWndMainATNSim", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:16pt; font-weight:600; color:#00007f;\">(C) 2017 ICEA </span></p></body></html>", None))
        self.menuSimulation.setTitle(_translate("CWndMainATNSim", "Simulation", None))
        self.menuConfiguration.setTitle(_translate("CWndMainATNSim", "Settings", None))
        self.menuRuntime.setTitle(_translate("CWndMainATNSim", "Runtime", None))
        self.menuHelp.setTitle(_translate("CWndMainATNSim", "Help", None))
        self.toolBar.setWindowTitle(_translate("CWndMainATNSim", "toolBar", None))
        self.act_edit_scenario.setText(_translate("CWndMainATNSim", "Create a scenario", None))
        self.act_start_session.setText(_translate("CWndMainATNSim", "Start ATN simulation", None))
        self.act_stop_session.setText(_translate("CWndMainATNSim", "Stop ATN Simulation", None))
        self.act_start_dump1090.setText(_translate("CWndMainATNSim", "Start ADS-B Viewer", None))
        self.act_start_visil.setText(_translate("CWndMainATNSim", "Start ViSIL", None))
        self.act_quit.setText(_translate("CWndMainATNSim", "Quit", None))
        self.act_db_edit.setText(_translate("CWndMainATNSim", "Manage exercises", None))
        self.act_scenario_to_xml.setText(_translate("CWndMainATNSim", "Export scenario to XML", None))
        self.act_scenario_to_exe.setText(_translate("CWndMainATNSim", "Export scenario to exercise", None))
        self.act_add_aircraft.setText(_translate("CWndMainATNSim", "Add an aircraft ...", None))
        self.act_show_manual.setText(_translate("CWndMainATNSim", "Manual", None))
        self.act_about.setText(_translate("CWndMainATNSim", "About", None))
        self.act_start_pilot.setText(_translate("CWndMainATNSim", "Start Pilot", None))

import wnd_main_atn_sim_rc
