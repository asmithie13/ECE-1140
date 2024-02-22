##from test_lauren_ui import *
##from TestBench import *
##from mainControl import *
from TestBench import *




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TestBench()
    ui.setupUi(MainWindow)
    ui.Open_Main_UI()
    MainWindow.show()
    sys.exit(app.exec_())


