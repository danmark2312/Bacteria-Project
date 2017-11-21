"""
This script creates a GUI for the user to use in connection with analyzing
data of bacteria growth rate at certain temperatures

It consists of the class, App, that is called in the end of the script.

App has multiple functions that creates a UI, binds buttons to functions,
filters data if needed and prints texts to display windows

Emil Ballermann (s174393) & Simon Moe Sørensen (s174420)
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from functions.dataLoad import dataLoad
from functions.dataPlot import dataPlot
from functions.dataStatistics import dataStatistics

class App():
    #Run this when class is run
    def __init__(self):
        #Initial variables
        self.dataLoaded = False #Set data as not loaded
        self.bacActive = "All bacteria selected"
        self.bacList = np.array([1,2,3,4])
        self.growthActive = "No active growth rate range filter"
        self.tempActive = "No active temperature range filter"
        #Configure UI
        self.setupUi(MainWindow)
        #Adding functionality to program
        #The following lines connects the buttons and inputs with functions
        #Dataload
        self.dataload_input.returnPressed.connect(self.dataloadUI) #On enter
        self.dataload_btn.clicked.connect(self.dataloadUI) #On click load data
        #Show data
        self.showdata_btn.clicked.connect(self.showdataUI)
        #Show statistics
        self.stat_btn.clicked.connect(self.statisticsUI)
        #Show plots
        self.plot_btn.clicked.connect(self.showplotsUI)

        #FILTERS
        self.bacList = [1,2,3,4]

        #Checkboxes
        self.bac1_chk.stateChanged.connect(self.filterBac)
        self.bac2_chk.stateChanged.connect(self.filterBac)

        #On state change, do filters
        self.bac1_chk.stateChanged.connect(self.filterBac) #on state change
        self.bac2_chk.stateChanged.connect(self.filterBac)
        self.bac3_chk.stateChanged.connect(self.filterBac)
        self.bac4_chk.stateChanged.connect(self.filterBac)
        self.bacteria_clear.clicked.connect(self.filterBacClear)
        #Growth Range
        self.growth_btn.clicked.connect(self.filterGrowthRange) #on click
        self.growthto_input.returnPressed.connect(self.filterGrowthRange) #on enter
        self.growthfrom_input.returnPressed.connect(self.filterGrowthRange) #on enter
        #Temp range
        self.temp_btn.clicked.connect(self.filterTempRange) #on click
        self.tempto_input.returnPressed.connect(self.filterTempRange) #on enter
        self.tempfrom_input.returnPressed.connect(self.filterTempRange) #on enter
        #Range Clear
        self.range_clear.clicked.connect(self.filterRangeClear)
        #Hide filters
        self.bacteria_box.hide()
        self.filterdata_box.hide()

    #Filter for bacteria
    def filterBac(self):
        bacStr = ["Salmonella enterica","Bacillus cereus","Listeria",
              "Brochothrix thermosphacta"]

        #Check if menu (bacteria chosen) is in bacList
        if bac in self.bacList:
            self.bacList = self.bacList[self.bacList != bac] #Remove from array
        else:
            self.bacList = np.append(self.bacList,bac) #Add to array

        bacActive = np.array(bacStr)[self.bacList-1] #Active bacteria filter

        self.print_(str(self.bacList))

        if len(bacActive) == 0:
            bacActive = "No active bacteria filter"
        return

    #Get conditions for bacteria filter
    def filterBac(self):
        bacStr = ["Salmonella enterica","Bacillus cereus","Listeria",
              "Brochothrix thermosphacta"] #List of bacteria names
        sender = MainWindow.sender() #get sender
        if self.dataLoaded:
            bac = sender.property("bacId") #Set bac to property of sender
            #Check if bacId (bacteria clicked) is in bacList
            if bac in self.bacList:
                self.bacList = self.bacList[self.bacList != bac] #Remove from array
                self.displayPrint("Removed {} from filter".format(bacStr[bac-1]))
            else:
                self.bacList = np.append(self.bacList,bac) #Add to array
                self.displayPrint("Added {} to filter".format(bacStr[bac-1]))

            self.bacActive = np.array(bacStr)[self.bacList-1] #Active bacteria filter. List of strings
            #If user removed all bacteria, remove filter, since there is no logic
            #in analyzing empty data.
            if len(self.bacActive) == 0:
                self.bacActive = "No bacteria selected. Using all bacteria"
            #If all baceria is added, state so and don't filter, to save resources
            elif len(self.bacActive) == 4:
                self.bacActive = "All bacteria selected"
            #Filter data
            self.setFilter()
        else:
            self.displayPrint("Error: No data has been loaded")

    #Get conditions for growth rate range filter
    def filterGrowthRange(self):
        if self.dataLoaded:
            r1 = self.growthfrom_input.text() #Lower limit
            r2 = self.growthto_input.text() #Upper limit
            #Check correct input
            try:
                r1,r2 = float(r1),float(r2)
                #Make sure there are values
                if (r1 or r2) > 0:
                    self.growthActive = [min(r1,r2),max(r1,r2)] #Set active growth filter
                    self.growthfrom_input.setPlaceholderText(str(r1)) #Set placeholder to current filter
                    self.growthto_input.setPlaceholderText(str(r2)) #Set placeholder to current filter
                    #Filter data
                    self.setFilter()
                    self.displayPrint("Added growth rate range filter")
                elif (r1 and r2) <= 0:
                    self.growthActive = "No active growth rate range filter"
                else:
                    self.displayPrint("Please fill in BOTH of the limits")
            except ValueError:
                self.displayPrint("Growth rate range can ONLY be an integer or float, ex: [0.02, 1.00, 1, 4] NOT: [Hello, bye, %!#]")
        else:
            self.displayPrint("Error: No data has been loaded")

    #Get conditions for temperature range filter
    def filterTempRange(self):
        if self.dataLoaded:
            r1 = self.tempfrom_input.text() #Lower limit
            r2 = self.tempto_input.text() #Upper limit
            #Check correct input
            try:
                r1,r2 = int(r1),int(r2)
                #Make sure there are correct values
                if (r1 or r2) > 0:
                    self.tempActive = [min(r1,r2),max(r1,r2)] #Set active temp filter
                    self.tempfrom_input.setPlaceholderText(str(r1)) #Set placeholder
                    self.tempto_input.setPlaceholderText(str(r2)) #Set placeholder
                    #Filter data
                    self.setFilter()
                    self.displayPrint("Added temperature range filter")
                elif (r1 and r2) <= 0:
                    self.tempActive = "No active temperature range filter"
                else:
                    self.displayPrint("Please fill in BOTH of the limits")
            except ValueError:
                self.displayPrint("Temperature range can ONLY be an integer, ex: 15, 45. NOT: [Hello, bye, %!#]")

        else:
            self.displayPrint("Error: No data has been loaded")

    #Uses the specified filters to filter the data
    def setFilter(self):
        #Use mask and range_ to filter data if filter is active (specific type)
        if type(self.bacActive) != str: #For bacteria
            mask = np.in1d(self.dataOld[:,2],self.bacList) #Where each value of bacList is in dataOld
            self.data = self.dataOld[mask] #Masking from unfiltered data
        else:
            self.data = self.dataOld #Data is the same as old

        if type(self.growthActive) != str: #For growth rate range
            growthRange = ((self.growthActive[0] < self.data[:,1]) & (self.data[:,1] < self.growthActive[1]))
            self.data = self.data[growthRange] #Data is filtered for growth rate range

        if type(self.tempActive) != str: #For temperature range
            tempRange = ((self.tempActive[0] < self.data[:,0]) & (self.data[:,0] < self.tempActive[1]))
            self.data = self.data[tempRange] #Data is filtered for temperature range
        self.filterPrint() #Print filter

    #Clears all of the range filters
    def filterRangeClear(self):
        #Filters clear
        self.growthActive = "No active growth rate range filter"
        self.tempActive = "No active temperature range filter"
        self.setFilter()
        #UI clear
        self.tempto_input.setText("")
        self.tempto_input.setPlaceholderText("Ex: 45")
        self.tempfrom_input.setText("")
        self.tempfrom_input.setPlaceholderText("Ex: 25")
        self.growthto_input.setText("")
        self.growthto_input.setPlaceholderText("Ex: 0.09")
        self.growthfrom_input.setText("")
        self.growthfrom_input.setPlaceholderText("Ex: 0.02")

    #Resets the bacteria filters
    def filterBacClear(self):
        #UI clear
        self.bac1_chk.setChecked(True)
        self.bac2_chk.setChecked(True)
        self.bac3_chk.setChecked(True)
        self.bac4_chk.setChecked(True)
        #Filters clear
        self.bacActive = "All bacteria selected"
        self.bacList = np.array([1,2,3,4])

    #Load data
    def dataloadUI(self):
        filename = self.dataload_input.text()
        #Get correct filename
        try:
            self.data,msg_errors = dataLoad(filename) #Load data
            self.dataOld = np.copy(self.data) #Copy data
            #Print message
            if len(msg_errors) == 0:
                msg_errors = "No erroneous lines!"
            self.displayPrint(msg_errors)
            self.dataLoaded = True # Set data as loaded
            #Show filters
            self.bacteria_box.show()
            self.filterdata_box.show()
            self.filterPrint()
            #Add filters
            self.setFilter()
            #Print succes msg
            self.displayPrint(("Data loaded succesfully from {}").format(filename))

        except FileNotFoundError:
            self.displayPrint("File not found, please try again")

    #Print statistics
    def statisticsUI(self):
        if self.dataLoaded:
            #Initial variables
            statStr = ["Mean Temperature","Mean Growth rate","Std Temperature",
                       "Std Growth rate","Mean Cold Growth rate",
                       "Mean Hot Growth rate", "Min Growth rate", "Max Growth rate",
                       "Min Temperature", "Max Temperature","Rows"]
            table_values = []
            #Create list of statistics
            for i in range(len(statStr)):
                statList = dataStatistics(self.data,statStr[i])
                table_values.append(statList)

            #Round table_values
            table_values = [ round(elem,3) for elem in table_values ]
            #Preferably we wouldn't consider hardcoding, however there was no
            #other solution, that wouldn't completely change the layout of the app
            msg_table=("""=====================  ====================
Statistic                                               Values
=====================  ====================
Mean Temperature                            {}
Mean Growth rate                              {}
Std Temperature                               {}
Std Growth rate                                 {}
Mean Cold Growth rate                      {}
Mean Hot Growth rate                       {}
Min | Max Growth rate                      {} | {}
Min | Max Temperature                     {} | {}
Rows                                                  {}
=====================  ====================""".format(*tuple(table_values)))
            self.displayPrint(msg_table) #Print table

        else:
            self.displayPrint("Error: No data has been loaded")

    #Show plots
    def showplotsUI(self):
        if self.dataLoaded:
            self.displayPrint("Generating plots...Done!")
            dataPlot(self.data)
        else:
            self.displayPrint("Error: No data has been loaded")

    #Show data
    def showdataUI(self):
        if self.dataLoaded:
            np.set_printoptions(suppress=True)
            self.displayPrint("Printing data...")
            self.displayPrint(str(self.data))
            self.displayPrint("Data printed")
        else:
            self.displayPrint("Error: No data has been loaded")

    #print text into display_window
    def displayPrint(self,text):
        self.display_window.insertPlainText("""---------------------------------------------------------------------
{}\n---------------------------------------------------------------------\n""".format(text))
        self.display_window.ensureCursorVisible() #Stay at bottom of window

    #Print text into filter_window
    def filterPrint(self):
        self.filter_window.clear()
        self.filter_window.insertPlainText("""\n\n=======================================
                                       ACTIVE FILTERS\n\n""")

        #Print active bacteria
        self.filter_window.insertPlainText("Bacteria filters: ")
        if type(self.bacActive) != str:
            self.filter_window.insertPlainText("\n")
            for elem in self.bacActive:
                self.filter_window.insertPlainText("""- {}\n""".format(elem))
        else:
            self.filter_window.insertPlainText("{}\n".format(self.bacActive))

        #Print active growth rate range filters
        self.filter_window.insertPlainText("\nGrowth rate range filter: ")
        if type(self.growthActive) != str:
            self.filter_window.insertPlainText("\n             From: {} | To: {}\n".format(self.growthActive[0],self.growthActive[1]))
        else:
            self.filter_window.insertPlainText("{}\n".format(self.growthActive))

        #Print active temperature filter
        self.filter_window.insertPlainText("\nTemperature range filter: ")
        if type(self.tempActive) != str:
            self.filter_window.insertPlainText("\n             From: {} | To: {}\n".format(self.tempActive[0],self.tempActive[1]))
        else:
            self.filter_window.insertPlainText("{}\n".format(self.tempActive))

        self.filter_window.insertPlainText("\n=======================================")


    ####################
    #Most of the code below this point has been generated by Qt Designer
    ####################

    #The lines should be easy to read, such as:
    #self.dataload_box.setObjectName("dataload_box")
    #Sets the objectname of a groupbox to dataload_box
    def setupUi(self, MainWindow):
        #Initalization of main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('resources/icon.png'))
        MainWindow.resize(420*2.12, 666) #Dank memes :)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        #Welcome label and header of program, separated with line
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setObjectName("welcome_label")
        self.verticalLayout.addWidget(self.welcome_label, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        #Frame for content of program
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(1000000, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #Frame containing the dataload and commands
        self.command_frame = QtWidgets.QFrame(self.frame)
        self.command_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.command_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.command_frame.setObjectName("command_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.command_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dataload_box = QtWidgets.QGroupBox(self.command_frame)
        self.dataload_box.setObjectName("dataload_box")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.dataload_box)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dataload_label = QtWidgets.QLabel(self.dataload_box)
        self.dataload_label.setObjectName("dataload_label")
        self.horizontalLayout_2.addWidget(self.dataload_label)
        #Dataload box
        self.dataload_input = QtWidgets.QLineEdit(self.dataload_box)
        self.dataload_input.setMinimumSize(QtCore.QSize(104, 21))
        self.dataload_input.setText("")
        self.dataload_input.setObjectName("dataload_input")
        self.horizontalLayout_2.addWidget(self.dataload_input)
        #The dataload button
        self.dataload_btn = QtWidgets.QPushButton(self.dataload_box)
        self.dataload_btn.setObjectName("dataload_btn")
        #Layout and lines
        self.horizontalLayout_2.addWidget(self.dataload_btn)
        self.verticalLayout_3.addWidget(self.dataload_box)
        self.line_5 = QtWidgets.QFrame(self.command_frame)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        #command_box
        self.command_box = QtWidgets.QGroupBox(self.command_frame)
        self.command_box.setObjectName("command_box")
        self.gridLayout = QtWidgets.QGridLayout(self.command_box)
        self.gridLayout.setObjectName("gridLayout")
        #Statistics button
        self.stat_btn = QtWidgets.QPushButton(self.command_box)
        self.stat_btn.setObjectName("stat_btn")
        self.gridLayout.addWidget(self.stat_btn, 0, 0, 1, 1)
        #show data button
        self.showdata_btn = QtWidgets.QPushButton(self.command_box)
        self.showdata_btn.setObjectName("showdata_btn")
        self.gridLayout.addWidget(self.showdata_btn, 0, 2, 1, 1)
        #plot button
        self.plot_btn = QtWidgets.QPushButton(self.command_box)
        self.plot_btn.setObjectName("plot_btn")
        self.gridLayout.addWidget(self.plot_btn, 0, 1, 1, 1)
        #Layouts and lines
        self.verticalLayout_3.addWidget(self.command_box)
        self.horizontalLayout.addWidget(self.command_frame)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        #Filter box
        self.filterdata_box = QtWidgets.QGroupBox(self.frame)
        self.filterdata_box.setMaximumSize(QtCore.QSize(350, 340))
        self.filterdata_box.setObjectName("filterdata_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.filterdata_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        #Bacteria box
        self.bacteria_box = QtWidgets.QGroupBox(self.filterdata_box)
        self.bacteria_box.setObjectName("bacteria_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bacteria_box)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        #Check boxes
        self.bac1_chk = QtWidgets.QCheckBox(self.bacteria_box)
        self.bac1_chk.setChecked(True)
        self.bac1_chk.setObjectName("bac1_chk")
        self.bac1_chk.setProperty("bacId",1)
        self.verticalLayout_2.addWidget(self.bac1_chk)
        self.bac2_chk = QtWidgets.QCheckBox(self.bacteria_box)
        self.bac2_chk.setChecked(True)
        self.bac2_chk.setObjectName("bac2_chk")
        self.bac2_chk.setProperty("bacId",2)
        self.verticalLayout_2.addWidget(self.bac2_chk)
        self.bac3_chk = QtWidgets.QCheckBox(self.bacteria_box)
        self.bac3_chk.setChecked(True)
        self.bac3_chk.setObjectName("bac3_chk")
        self.bac3_chk.setProperty("bacId",3)
        self.verticalLayout_2.addWidget(self.bac3_chk)
        self.bac4_chk = QtWidgets.QCheckBox(self.bacteria_box)
        self.bac4_chk.setChecked(True)
        self.bac4_chk.setObjectName("bac4_chk")
        self.bac4_chk.setProperty("bacId",4)
        self.verticalLayout_2.addWidget(self.bac4_chk)
        self.gridLayout_2.addWidget(self.bacteria_box, 1, 0, 1, 1)
        #Range filter box
        self.range_box = QtWidgets.QGroupBox(self.filterdata_box)
        self.range_box.setMaximumSize(QtCore.QSize(166, 242))
        self.range_box.setObjectName("range_box")
        self.formLayout = QtWidgets.QFormLayout(self.range_box)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        #Growth rate filter
        self.growth_label = QtWidgets.QLabel(self.range_box)
        self.growth_label.setObjectName("growth_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.growth_label)
        self.growthfrom_label = QtWidgets.QLabel(self.range_box)
        self.growthfrom_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.growthfrom_label.setObjectName("growthfrom_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.growthfrom_label)
        self.growthto_label = QtWidgets.QLabel(self.range_box)
        self.growthto_label.setObjectName("growthto_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.growthto_label)
        self.growthfrom_input = QtWidgets.QLineEdit(self.range_box)
        self.growthfrom_input.setMinimumSize(QtCore.QSize(70, 21))
        self.growthfrom_input.setMaximumSize(QtCore.QSize(70, 21))
        self.growthfrom_input.setClearButtonEnabled(False)
        self.growthfrom_input.setObjectName("growthfrom_input")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.growthfrom_input)
        self.growthto_input = QtWidgets.QLineEdit(self.range_box)
        self.growthto_input.setMinimumSize(QtCore.QSize(70, 21))
        self.growthto_input.setMaximumSize(QtCore.QSize(70, 21))
        self.growthto_input.setObjectName("growthto_input")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.growthto_input)
        self.growth_btn = QtWidgets.QPushButton(self.range_box)
        self.growth_btn.setMinimumSize(QtCore.QSize(142, 24))
        self.growth_btn.setObjectName("growth_btn")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.growth_btn)
        self.line_4 = QtWidgets.QFrame(self.range_box)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.line_4)
        #Temp filter
        self.temp_label = QtWidgets.QLabel(self.range_box)
        self.temp_label.setObjectName("temp_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.temp_label)
        self.tempfrom_label = QtWidgets.QLabel(self.range_box)
        self.tempfrom_label.setObjectName("tempfrom_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.tempfrom_label)
        self.tempto_label = QtWidgets.QLabel(self.range_box)
        self.tempto_label.setObjectName("tempto_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.tempto_label)
        self.tempfrom_input = QtWidgets.QLineEdit(self.range_box)
        self.tempfrom_input.setMinimumSize(QtCore.QSize(70, 21))
        self.tempfrom_input.setMaximumSize(QtCore.QSize(70, 21))
        self.tempfrom_input.setObjectName("tempfrom_input")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.tempfrom_input)
        self.tempto_input = QtWidgets.QLineEdit(self.range_box)
        self.tempto_input.setMinimumSize(QtCore.QSize(70, 21))
        self.tempto_input.setMaximumSize(QtCore.QSize(70, 21))
        self.tempto_input.setText("")
        self.tempto_input.setObjectName("tempto_input")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.tempto_input)
        self.temp_btn = QtWidgets.QPushButton(self.range_box)
        self.temp_btn.setMinimumSize(QtCore.QSize(142, 24))
        self.temp_btn.setObjectName("temp_btn")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.temp_btn)
        self.gridLayout_2.addWidget(self.range_box, 1, 1, 1, 1)
        #Clear filter buttons
        self.bacteria_clear = QtWidgets.QPushButton(self.filterdata_box)
        self.bacteria_clear.setObjectName("bacteria_clear")
        self.gridLayout_2.addWidget(self.bacteria_clear, 2, 0, 1, 1)
        self.range_clear = QtWidgets.QPushButton(self.filterdata_box)
        self.range_clear.setObjectName("range_clear")
        self.gridLayout_2.addWidget(self.range_clear, 2, 1, 1, 1)
        self.horizontalLayout.addWidget(self.filterdata_box)
        self.verticalLayout.addWidget(self.frame)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        #Display window
        self.display_box = QtWidgets.QGroupBox(self.centralwidget)
        self.display_box.setObjectName("display_box")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.display_box)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.display_window = QtWidgets.QPlainTextEdit(self.display_box)
        self.display_window.setReadOnly(True)
        self.display_window.setObjectName("display_window")
        self.display_window.setTextInteractionFlags(QtCore.Qt.NoTextInteraction) #Can't mark text
        self.horizontalLayout_5.addWidget(self.display_window)
        self.line_6 = QtWidgets.QFrame(self.display_box)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_5.addWidget(self.line_6)
        #Filtering window
        self.filter_window = QtWidgets.QPlainTextEdit(self.display_box)
        self.filter_window.setMaximumSize(QtCore.QSize(325, 1000000))
        self.filter_window.setAcceptDrops(False)
        self.filter_window.setAutoFillBackground(False)
        self.filter_window.setReadOnly(True)
        self.filter_window.setObjectName("filter_window")
        self.horizontalLayout_5.addWidget(self.filter_window)
        self.verticalLayout.addWidget(self.display_box)
        MainWindow.setCentralWidget(self.centralwidget)
        #Menu and status bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Run retranslateUI function
        self.retranslateUi(MainWindow)

        #Set tab order
        MainWindow.setTabOrder(self.dataload_input, self.dataload_btn)
        MainWindow.setTabOrder(self.dataload_btn, self.stat_btn)
        MainWindow.setTabOrder(self.stat_btn, self.plot_btn)
        MainWindow.setTabOrder(self.plot_btn, self.showdata_btn)
        MainWindow.setTabOrder(self.showdata_btn, self.bac1_chk)
        MainWindow.setTabOrder(self.bac1_chk, self.bac2_chk)
        MainWindow.setTabOrder(self.bac2_chk, self.bac3_chk)
        MainWindow.setTabOrder(self.bac3_chk, self.bac4_chk)
        MainWindow.setTabOrder(self.bac4_chk, self.bacteria_clear)
        MainWindow.setTabOrder(self.bacteria_clear, self.growthfrom_input)
        MainWindow.setTabOrder(self.growthfrom_input, self.growthto_input)
        MainWindow.setTabOrder(self.growthto_input, self.growth_btn)
        MainWindow.setTabOrder(self.growth_btn, self.tempfrom_input)
        MainWindow.setTabOrder(self.tempfrom_input, self.tempto_input)
        MainWindow.setTabOrder(self.tempto_input, self.temp_btn)
        MainWindow.setTabOrder(self.temp_btn, self.range_clear)
        MainWindow.setTabOrder(self.range_clear, self.display_window)
        MainWindow.setTabOrder(self.display_window, self.filter_window)

    #This function sets the displaynames, placeholdertexts, tooltips and so on
    #It practically adds names to empty boxes
    #Keep in mind the setToolTip function takes an html-syntaxed input
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bacteria Data Analysis"))
        self.welcome_label.setText(_translate("MainWindow", "Welcome to the Bacteria Data Analysis Program"))
        self.dataload_box.setTitle(_translate("MainWindow", "Dataload"))
        self.dataload_label.setText(_translate("MainWindow", "Enter the name of the datafile:"))
        self.dataload_input.setToolTip(_translate("MainWindow", "<html><head/><body><p>Please enter a filename</p></body></html>"))
        self.dataload_input.setStatusTip(_translate("MainWindow", "Enter the name of the datafile"))
        self.dataload_input.setPlaceholderText(_translate("MainWindow", "Ex: test.txt"))
        self.dataload_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Loads the datafile given to the left</p></body></html>"))
        self.dataload_btn.setStatusTip(_translate("MainWindow", "Click to load data from filename"))
        self.dataload_btn.setText(_translate("MainWindow", "Load Data"))
        self.command_box.setTitle(_translate("MainWindow", "Commands"))
        self.stat_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Displays statistics based on current data</p></body></html>"))
        self.stat_btn.setStatusTip(_translate("MainWindow", "Click to display statistics of current data"))
        self.stat_btn.setText(_translate("MainWindow", "Display statistics"))
        self.showdata_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Shows current data</p></body></html>"))
        self.showdata_btn.setStatusTip(_translate("MainWindow", "Click to show current data"))
        self.showdata_btn.setText(_translate("MainWindow", "Show data"))
        self.plot_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Generates plots on current data</p></body></html>"))
        self.plot_btn.setStatusTip(_translate("MainWindow", "Click to generate plots of current data"))
        self.plot_btn.setText(_translate("MainWindow", "Generate plots"))
        self.filterdata_box.setTitle(_translate("MainWindow", "Filter Data"))
        self.bacteria_box.setTitle(_translate("MainWindow", "Bacteria"))
        self.bac1_chk.setToolTip(_translate("MainWindow", "<html><head/><body><p>Press to activate or deactive filter</p></body></html>"))
        self.bac1_chk.setStatusTip(_translate("MainWindow", "Click to add/remove filter"))
        self.bac1_chk.setText(_translate("MainWindow", "Salmonella enterica"))
        self.bac2_chk.setToolTip(_translate("MainWindow", "<html><head/><body><p>Press to activate or deactive filter</p></body></html>"))
        self.bac2_chk.setStatusTip(_translate("MainWindow", "Click to add/remove filter"))
        self.bac2_chk.setText(_translate("MainWindow", "Bacillus cereus"))
        self.bac3_chk.setToolTip(_translate("MainWindow", "<html><head/><body><p>Press to activate or deactive filter</p></body></html>"))
        self.bac3_chk.setStatusTip(_translate("MainWindow", "Click to add/remove filter"))
        self.bac3_chk.setText(_translate("MainWindow", "Listeria"))
        self.bac4_chk.setToolTip(_translate("MainWindow", "<html><head/><body><p>Press to activate or deactive filter</p></body></html>"))
        self.bac4_chk.setStatusTip(_translate("MainWindow", "Click to add/remove filter"))
        self.bac4_chk.setText(_translate("MainWindow", "Brochothrix thermosphacta"))
        self.range_box.setTitle(_translate("MainWindow", "Range"))
        self.growth_label.setToolTip(_translate("MainWindow", "<html><head/><body><p>Filter for growth rate</p></body></html>"))
        self.growth_label.setText(_translate("MainWindow", "Growth rate"))
        self.growthto_label.setText(_translate("MainWindow", "Upper limit"))
        self.growthto_input.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter upper limit</p></body></html>"))
        self.growthto_input.setStatusTip(_translate("MainWindow", "Enter an upper limit for the range"))
        self.growthto_input.setPlaceholderText(_translate("MainWindow", "Ex: 0.09"))
        self.growth_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Press to add filter with limits stated above</p></body></html>"))
        self.growth_btn.setStatusTip(_translate("MainWindow", "Press button to add growth rate filter"))
        self.growth_btn.setText(_translate("MainWindow", "Add growth rate filter"))
        self.temp_label.setToolTip(_translate("MainWindow", "<html><head/><body><p>Filter for temperature</p></body></html>"))
        self.temp_label.setText(_translate("MainWindow", "Temperature"))
        self.tempfrom_label.setText(_translate("MainWindow", "Lower limit"))
        self.tempto_label.setText(_translate("MainWindow", "Upper limit"))
        self.tempfrom_input.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter lower limit</p></body></html>"))
        self.tempfrom_input.setStatusTip(_translate("MainWindow", "Enter a lower limit for the range"))
        self.tempfrom_input.setPlaceholderText(_translate("MainWindow", "Ex: 25"))
        self.temp_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Press to add filter with limits stated above</p></body></html>"))
        self.temp_btn.setStatusTip(_translate("MainWindow", "Press button to add temperature filter"))
        self.temp_btn.setText(_translate("MainWindow", "Add temperature filter"))
        self.growthfrom_label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Goat</p></body></html>"))
        self.growthfrom_label.setText(_translate("MainWindow", "Lower limit"))
        self.growthfrom_input.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter lower limit</p></body></html>"))
        self.growthfrom_input.setStatusTip(_translate("MainWindow", "Enter a lower limit for the range"))
        self.growthfrom_input.setPlaceholderText(_translate("MainWindow", "Ex: 0.02"))
        self.tempto_input.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter upper limit</p></body></html>"))
        self.tempto_input.setStatusTip(_translate("MainWindow", "Enter an upper limit for the range"))
        self.tempto_input.setPlaceholderText(_translate("MainWindow", "Ex: 45"))
        self.bacteria_clear.setToolTip(_translate("MainWindow", "<html><head/><body><p>Reset bacteria</p></body></html>"))
        self.bacteria_clear.setStatusTip(_translate("MainWindow", "Reset bacteria filters"))
        self.bacteria_clear.setText(_translate("MainWindow", "Reset Bacteria Filter"))
        self.range_clear.setToolTip(_translate("MainWindow", "<html><head/><body><p>Clear all ranges</p></body></html>"))
        self.range_clear.setStatusTip(_translate("MainWindow", "Clear all ranges"))
        self.range_clear.setText(_translate("MainWindow", "Clear Range Filters"))
        self.display_box.setTitle(_translate("MainWindow", "Display Window"))
        self.display_window.setToolTip(_translate("MainWindow", "<html><head/><body><p>Any information will be printed here</p></body></html>"))
        self.display_window.setStatusTip(_translate("MainWindow", "Shows any printed information"))
        self.display_window.setPlaceholderText(_translate("MainWindow", "No information printed"))
        self.filter_window.setToolTip(_translate("MainWindow", "<html><head/><body><p>This shows the active filters</p></body></html>"))
        self.filter_window.setStatusTip(_translate("MainWindow", "Shows current filters"))
        self.filter_window.setPlaceholderText(_translate("MainWindow", "No currently active filters"))

#If file is run as main program, call the class and display a GUI
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) #Syntax for pyqt
    MainWindow = QtWidgets.QMainWindow() #Define the mainwindow
    ui = App() #Call the class which runs the __init__
    MainWindow.show() #Show the program
    sys.exit(app.exec_()) #Quit nicely
