from TrainController import *

class Vital_Failure(TrainController):    
    def Control_Emergency_Brake(self):
            if TrainController.ui.Ebrake.isChecked() == True:
                enable = True
                #emit(1) brake signal to tanvi
            else:
                enable = False
            
            TrainController.ui.buttonMan.setDisabled(enable)
            TrainController.ui.buttonMan.setDisabled(enable)
            TrainController.ui.buttonDoorL.setDisabled(enable)
            TrainController.ui.buttonDoorR.setDisabled(enable)
            TrainController.ui.temp.setDisabled(enable)
            TrainController.ui.buttonHDoff.setDisabled(enable)
            TrainController.ui.buttonHDon.setDisabled(enable)
            TrainController.ui.IntLightSld.setDisabled(enable)
            TrainController.ui.lineEditAnn.setDisabled(enable)
            TrainController.ui.vertSliderPow.setValue(0)
            TrainController.ui.vertSliderBrk.setValue(0)
            TrainController.ui.vertSliderBrk.setDisabled(enable)
            TrainController.ui.vertSliderPow.setDisabled(enable)
            TrainController.ui.inputKi.setDisabled(enable)
            TrainController.ui.inputKp.setDisabled(enable)


    def Control_Signal_Failure(self,sig_fail):
            if(sig_fail == True):
                TrainController.ui.SigFail.setStyleSheet("color: red;\n"
                                            "background-color: rgb(255, 255, 255);")
                TrainController.ui.vertSliderPow.setValue(0)
                TrainController.ui.vertSliderBrk.setValue(1)
                TrainController.ui.vertSliderPow.setDisabled(True)
                TrainController.ui.vertSliderBrk.setDisabled(True)
            else:
                TrainController.ui.SigFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                        "background-color: rgb(255, 255, 255);")
                TrainController.ui.vertSliderPow.setDisabled(False)
                TrainController.ui.vertSliderBrk.setDisabled(False)


    def Control_Power_Failure(self,pwr_fail):
            if pwr_fail == True:
                TrainController.ui.PwrFail.setStyleSheet("color: red;\n"
                                            "background-color: rgb(255, 255, 255);")
                TrainController.ui.vertSliderPow.setValue(0)
                TrainController.ui.vertSliderBrk.setValue(1)
                TrainController.ui.vertSliderPow.setDisabled(True)
                TrainController.ui.vertSliderBrk.setDisabled(True)
            else:
                TrainController.ui.PwrFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                        "background-color: rgb(255, 255, 255);")
                TrainController.ui.vertSliderPow.setDisabled(False)
                TrainController.ui.vertSliderBrk.setDisabled(False)


    def Control_Brake_Failure(self,brk_fail):
            if(brk_fail == True):
                TrainController.ui.BrkFail.setStyleSheet("color: red;\n"
                                        "background-color: rgb(255, 255, 255);")
                TrainController.ui.Ebrake.setChecked(True)
            #DISABLE
            else:
                TrainController.ui.BrkFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                        "background-color: rgb(255, 255, 255);")