# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gao/Desktop/Tianhua_Guo_Homework/Seocnd/random_walk_window.ui'
#
# Created: Tue Mar  5 16:13:24 2013
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(884, 491)
        MainWindow.setMinimumSize(QtCore.QSize(884, 0))
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Random Walk Simulator", None, QtGui.QApplication.UnicodeUTF8))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 691, 431))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.central_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.central_layout.setSpacing(0)
        self.central_layout.setMargin(0)
        self.central_layout.setObjectName(_fromUtf8("central_layout"))
        self.information_widget = QtGui.QTabWidget(self.verticalLayoutWidget)
        self.information_widget.setObjectName(_fromUtf8("information_widget"))
        self.conf_tab = QtGui.QWidget()
        self.conf_tab.setObjectName(_fromUtf8("conf_tab"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.conf_tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 591, 181))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.conf_layout = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.conf_layout.setMargin(0)
        self.conf_layout.setObjectName(_fromUtf8("conf_layout"))
        self.starting_number_box = QtGui.QGroupBox(self.gridLayoutWidget_3)
        self.starting_number_box.setTitle(QtGui.QApplication.translate("MainWindow", "Starting Number", None, QtGui.QApplication.UnicodeUTF8))
        self.starting_number_box.setObjectName(_fromUtf8("starting_number_box"))
        self.starting_number_label = QtGui.QLabel(self.starting_number_box)
        self.starting_number_label.setGeometry(QtCore.QRect(40, 30, 171, 20))
        self.starting_number_label.setText(QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.starting_number_label.setObjectName(_fromUtf8("starting_number_label"))
        self.conf_layout.addWidget(self.starting_number_box, 0, 0, 1, 1)
        self.random_walk_box = QtGui.QGroupBox(self.gridLayoutWidget_3)
        self.random_walk_box.setTitle(QtGui.QApplication.translate("MainWindow", "Random Walk Number", None, QtGui.QApplication.UnicodeUTF8))
        self.random_walk_box.setObjectName(_fromUtf8("random_walk_box"))
        self.random_walk_label = QtGui.QLabel(self.random_walk_box)
        self.random_walk_label.setGeometry(QtCore.QRect(50, 30, 171, 20))
        self.random_walk_label.setText(QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.random_walk_label.setObjectName(_fromUtf8("random_walk_label"))
        self.conf_layout.addWidget(self.random_walk_box, 0, 1, 1, 1)
        self.nagetive_range_box = QtGui.QGroupBox(self.gridLayoutWidget_3)
        self.nagetive_range_box.setTitle(QtGui.QApplication.translate("MainWindow", "Nagetive Range", None, QtGui.QApplication.UnicodeUTF8))
        self.nagetive_range_box.setObjectName(_fromUtf8("nagetive_range_box"))
        self.nagetive_range_label = QtGui.QLabel(self.nagetive_range_box)
        self.nagetive_range_label.setGeometry(QtCore.QRect(40, 30, 171, 20))
        self.nagetive_range_label.setText(QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.nagetive_range_label.setObjectName(_fromUtf8("nagetive_range_label"))
        self.conf_layout.addWidget(self.nagetive_range_box, 1, 0, 1, 1)
        self.positive_range_box = QtGui.QGroupBox(self.gridLayoutWidget_3)
        self.positive_range_box.setTitle(QtGui.QApplication.translate("MainWindow", "Positive Range", None, QtGui.QApplication.UnicodeUTF8))
        self.positive_range_box.setObjectName(_fromUtf8("positive_range_box"))
        self.positive_range_label = QtGui.QLabel(self.positive_range_box)
        self.positive_range_label.setGeometry(QtCore.QRect(50, 30, 171, 20))
        self.positive_range_label.setText(QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.positive_range_label.setObjectName(_fromUtf8("positive_range_label"))
        self.conf_layout.addWidget(self.positive_range_box, 1, 1, 1, 1)
        self.random_walk_distance_box = QtGui.QGroupBox(self.gridLayoutWidget_3)
        self.random_walk_distance_box.setTitle(QtGui.QApplication.translate("MainWindow", "Random Walk Distance", None, QtGui.QApplication.UnicodeUTF8))
        self.random_walk_distance_box.setObjectName(_fromUtf8("random_walk_distance_box"))
        self.random_walk_distance_label = QtGui.QLabel(self.random_walk_distance_box)
        self.random_walk_distance_label.setGeometry(QtCore.QRect(40, 26, 171, 21))
        self.random_walk_distance_label.setText(QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.random_walk_distance_label.setObjectName(_fromUtf8("random_walk_distance_label"))
        self.conf_layout.addWidget(self.random_walk_distance_box, 2, 0, 1, 1)
        self.information_widget.addTab(self.conf_tab, _fromUtf8(""))
        self.graph_tab = QtGui.QWidget()
        self.graph_tab.setObjectName(_fromUtf8("graph_tab"))
        self.information_widget.addTab(self.graph_tab, _fromUtf8(""))
        self.result_tab = QtGui.QWidget()
        self.result_tab.setObjectName(_fromUtf8("result_tab"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.result_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 661, 381))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.result_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.result_layout.setMargin(0)
        self.result_layout.setObjectName(_fromUtf8("result_layout"))
        self.result_table = RandomWalkTable(self.verticalLayoutWidget_2)
        self.result_table.setObjectName(_fromUtf8("result_table"))
        self.result_table.setColumnCount(0)
        self.result_table.setRowCount(0)
        self.result_layout.addWidget(self.result_table)
        self.information_widget.addTab(self.result_tab, _fromUtf8(""))
        self.statistics_tab = QtGui.QWidget()
        self.statistics_tab.setObjectName(_fromUtf8("statistics_tab"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.statistics_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 581, 241))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.statistics_layout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.statistics_layout.setMargin(0)
        self.statistics_layout.setObjectName(_fromUtf8("statistics_layout"))
        self.tenth_percentile_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.tenth_percentile_label.setText(QtGui.QApplication.translate("MainWindow", "10\'th percentile", None, QtGui.QApplication.UnicodeUTF8))
        self.tenth_percentile_label.setObjectName(_fromUtf8("tenth_percentile_label"))
        self.statistics_layout.addWidget(self.tenth_percentile_label, 3, 0, 1, 1)
        self.mean_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.mean_label.setText(QtGui.QApplication.translate("MainWindow", "Mean value", None, QtGui.QApplication.UnicodeUTF8))
        self.mean_label.setObjectName(_fromUtf8("mean_label"))
        self.statistics_layout.addWidget(self.mean_label, 5, 0, 1, 1)
        self.standard_deviation_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.standard_deviation_label.setText(QtGui.QApplication.translate("MainWindow", "Standard Deviation", None, QtGui.QApplication.UnicodeUTF8))
        self.standard_deviation_label.setObjectName(_fromUtf8("standard_deviation_label"))
        self.statistics_layout.addWidget(self.standard_deviation_label, 6, 0, 1, 1)
        self.maximum_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.maximum_label.setText(QtGui.QApplication.translate("MainWindow", "Minimum Value", None, QtGui.QApplication.UnicodeUTF8))
        self.maximum_label.setObjectName(_fromUtf8("maximum_label"))
        self.statistics_layout.addWidget(self.maximum_label, 1, 0, 1, 1)
        self.minimum_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.minimum_value.setText(_fromUtf8(""))
        self.minimum_value.setObjectName(_fromUtf8("minimum_value"))
        self.statistics_layout.addWidget(self.minimum_value, 1, 1, 1, 1)
        self.tenth_percentile_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.tenth_percentile_value.setText(_fromUtf8(""))
        self.tenth_percentile_value.setObjectName(_fromUtf8("tenth_percentile_value"))
        self.statistics_layout.addWidget(self.tenth_percentile_value, 3, 1, 1, 1)
        self.mean_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.mean_value.setText(_fromUtf8(""))
        self.mean_value.setObjectName(_fromUtf8("mean_value"))
        self.statistics_layout.addWidget(self.mean_value, 5, 1, 1, 1)
        self.standard_deviation_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.standard_deviation_value.setText(_fromUtf8(""))
        self.standard_deviation_value.setObjectName(_fromUtf8("standard_deviation_value"))
        self.statistics_layout.addWidget(self.standard_deviation_value, 6, 1, 1, 1)
        self.minimum_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.minimum_label.setText(QtGui.QApplication.translate("MainWindow", "Macimum Value", None, QtGui.QApplication.UnicodeUTF8))
        self.minimum_label.setObjectName(_fromUtf8("minimum_label"))
        self.statistics_layout.addWidget(self.minimum_label, 2, 0, 1, 1)
        self.maximum_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.maximum_value.setText(_fromUtf8(""))
        self.maximum_value.setObjectName(_fromUtf8("maximum_value"))
        self.statistics_layout.addWidget(self.maximum_value, 2, 1, 1, 1)
        self.ninetieth_percentile_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.ninetieth_percentile_label.setText(QtGui.QApplication.translate("MainWindow", "90\'th percentile", None, QtGui.QApplication.UnicodeUTF8))
        self.ninetieth_percentile_label.setObjectName(_fromUtf8("ninetieth_percentile_label"))
        self.statistics_layout.addWidget(self.ninetieth_percentile_label, 4, 0, 1, 1)
        self.ninetieth_percentile_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.ninetieth_percentile_value.setText(_fromUtf8(""))
        self.ninetieth_percentile_value.setObjectName(_fromUtf8("ninetieth_percentile_value"))
        self.statistics_layout.addWidget(self.ninetieth_percentile_value, 4, 1, 1, 1)
        self.dimension_statistics_box = QtGui.QComboBox(self.statistics_tab)
        self.dimension_statistics_box.setGeometry(QtCore.QRect(20, 20, 91, 23))
        self.dimension_statistics_box.setObjectName(_fromUtf8("dimension_statistics_box"))
        self.dimension_statistics_box.addItem(_fromUtf8(""))
        self.dimension_statistics_box.setItemText(0, QtGui.QApplication.translate("MainWindow", "First D", None, QtGui.QApplication.UnicodeUTF8))
        self.dimension_statistics_box.addItem(_fromUtf8(""))
        self.dimension_statistics_box.setItemText(1, QtGui.QApplication.translate("MainWindow", "Second D", None, QtGui.QApplication.UnicodeUTF8))
        self.step_statistics_box = QtGui.QComboBox(self.statistics_tab)
        self.step_statistics_box.setGeometry(QtCore.QRect(140, 20, 161, 23))
        self.step_statistics_box.setToolTip(QtGui.QApplication.translate("MainWindow", "if the number is not int. Then it will be rounded.", None, QtGui.QApplication.UnicodeUTF8))
        self.step_statistics_box.setObjectName(_fromUtf8("step_statistics_box"))
        self.step_statistics_box.addItem(_fromUtf8(""))
        self.step_statistics_box.setItemText(0, QtGui.QApplication.translate("MainWindow", "10% of random step", None, QtGui.QApplication.UnicodeUTF8))
        self.step_statistics_box.addItem(_fromUtf8(""))
        self.step_statistics_box.setItemText(1, QtGui.QApplication.translate("MainWindow", "20% of random step", None, QtGui.QApplication.UnicodeUTF8))
        self.step_statistics_box.addItem(_fromUtf8(""))
        self.step_statistics_box.setItemText(2, QtGui.QApplication.translate("MainWindow", "30% of random step", None, QtGui.QApplication.UnicodeUTF8))
        self.step_statistics_box.addItem(_fromUtf8(""))
        self.step_statistics_box.setItemText(3, QtGui.QApplication.translate("MainWindow", "40% of random step", None, QtGui.QApplication.UnicodeUTF8))
        self.step_statistics_box.addItem(_fromUtf8(""))
        self.step_statistics_box.setItemText(4, QtGui.QApplication.translate("MainWindow", "50% of random step", None, QtGui.QApplication.UnicodeUTF8))
        self.step_statistics_box.addItem(_fromUtf8(""))
        self.step_statistics_box.setItemText(5, QtGui.QApplication.translate("MainWindow", "60% of random step", None, QtGui.QApplication.UnicodeUTF8))
        self.step_statistics_box.addItem(_fromUtf8(""))
        self.step_statistics_box.setItemText(6, QtGui.QApplication.translate("MainWindow", "70% of random step", None, QtGui.QApplication.UnicodeUTF8))
        self.step_statistics_box.addItem(_fromUtf8(""))
        self.step_statistics_box.setItemText(7, QtGui.QApplication.translate("MainWindow", "80% of random step", None, QtGui.QApplication.UnicodeUTF8))
        self.step_statistics_box.addItem(_fromUtf8(""))
        self.step_statistics_box.setItemText(8, QtGui.QApplication.translate("MainWindow", "90% of random step", None, QtGui.QApplication.UnicodeUTF8))
        self.step_statistics_box.addItem(_fromUtf8(""))
        self.step_statistics_box.setItemText(9, QtGui.QApplication.translate("MainWindow", "100% of random step", None, QtGui.QApplication.UnicodeUTF8))
        self.information_widget.addTab(self.statistics_tab, _fromUtf8(""))
        self.central_layout.addWidget(self.information_widget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.preference_widget = QtGui.QDockWidget(MainWindow)
        self.preference_widget.setMinimumSize(QtCore.QSize(168, 449))
        self.preference_widget.setMaximumSize(QtCore.QSize(168, 449))
        self.preference_widget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.DockWidgetVerticalTitleBar)
        self.preference_widget.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.preference_widget.setObjectName(_fromUtf8("preference_widget"))
        self.preference_widget_contents = QtGui.QWidget()
        self.preference_widget_contents.setObjectName(_fromUtf8("preference_widget_contents"))
        self.dimension_box = QtGui.QGroupBox(self.preference_widget_contents)
        self.dimension_box.setGeometry(QtCore.QRect(0, 10, 120, 71))
        self.dimension_box.setTitle(QtGui.QApplication.translate("MainWindow", "Dimension", None, QtGui.QApplication.UnicodeUTF8))
        self.dimension_box.setObjectName(_fromUtf8("dimension_box"))
        self.dimension_value = QtGui.QComboBox(self.dimension_box)
        self.dimension_value.setGeometry(QtCore.QRect(10, 30, 101, 23))
        self.dimension_value.setObjectName(_fromUtf8("dimension_value"))
        self.dimension_value.addItem(_fromUtf8(""))
        self.dimension_value.setItemText(0, QtGui.QApplication.translate("MainWindow", "One D", None, QtGui.QApplication.UnicodeUTF8))
        self.dimension_value.addItem(_fromUtf8(""))
        self.dimension_value.setItemText(1, QtGui.QApplication.translate("MainWindow", "Two D", None, QtGui.QApplication.UnicodeUTF8))
        self.preference_widget.setWidget(self.preference_widget_contents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.preference_widget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_new = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./res/new_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./res/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_new.setIcon(icon)
        self.action_new.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_new.setObjectName(_fromUtf8("action_new"))
        self.action_edit = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./res/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_edit.setIcon(icon1)
        self.action_edit.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_edit.setObjectName(_fromUtf8("action_edit"))
        self.action_start = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./res/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_start.setIcon(icon2)
        self.action_start.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.action_start.setObjectName(_fromUtf8("action_start"))
        self.action_clear = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./res/reset.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_clear.setIcon(icon3)
        self.action_clear.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.action_clear.setObjectName(_fromUtf8("action_clear"))
        self.action_stop = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("./res/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_stop.setIcon(icon4)
        self.action_stop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.action_stop.setObjectName(_fromUtf8("action_stop"))
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_new)
        self.toolBar.addAction(self.action_edit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_start)
        self.toolBar.addAction(self.action_stop)
        self.toolBar.addAction(self.action_clear)

        self.retranslateUi(MainWindow)
        self.information_widget.setCurrentIndex(1)
        QtCore.QObject.connect(self.dimension_value, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.change_dimension)
        QtCore.QObject.connect(self.dimension_statistics_box, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.refresh_statistics_tab)
        QtCore.QObject.connect(self.step_statistics_box, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.refresh_statistics_tab)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.information_widget.setTabText(self.information_widget.indexOf(self.conf_tab), QtGui.QApplication.translate("MainWindow", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.information_widget.setTabText(self.information_widget.indexOf(self.graph_tab), QtGui.QApplication.translate("MainWindow", "Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.information_widget.setTabText(self.information_widget.indexOf(self.result_tab), QtGui.QApplication.translate("MainWindow", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.information_widget.setTabText(self.information_widget.indexOf(self.statistics_tab), QtGui.QApplication.translate("MainWindow", "Statistics", None, QtGui.QApplication.UnicodeUTF8))

from random_walk_table import RandomWalkTable

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

