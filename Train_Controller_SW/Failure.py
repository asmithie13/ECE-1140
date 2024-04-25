from Train_Controller_SW.mainControl import Ui_MainWindow

class Vital_Failure():
    
    def __init__(self,ui,ebrake_sig, ebrake_disable_sig):

        self.ui = ui
        self.ebrake_sig = ebrake_sig
        self.ebrake_disable_sig = ebrake_disable_sig
        


    def Control_Emergency_Brake_Internal(self,ebrake_in):
            if self.ui.Ebrake.isChecked() == True:
                enable = True
                self.ebrake_disable_sig.emit(1)
            
            elif ebrake_in == True:
                if self.ui.Ebrake.isChecked() == False:
                    self.ui.Ebrake.toggle()
                enable = True
                self.ebrake_disable_sig.emit(1)
            
            else:
                if self.ui.Ebrake.isChecked() == True:
                    self.ui.Ebrake.toggle()
                enable = False
                self.ebrake_disable_sig.emit(0)

            if(not(self.ui.buttonAuto.isChecked())):
                self.ui.buttonDoorL.setDisabled(enable)
                self.ui.buttonDoorR.setDisabled(enable)
                self.ui.temp.setDisabled(enable)
                self.ui.buttonHDoff.setDisabled(enable)
                self.ui.buttonHDon.setDisabled(enable)
                self.ui.IntLightSld.setDisabled(enable)
                self.ui.lineEditAnn.setDisabled(enable)
                self.ui.vertSliderBrk.setDisabled(enable)
                self.ui.vertSliderPow.setDisabled(enable)
                self.ui.inputKi.setDisabled(enable)
                self.ui.inputKp.setDisabled(enable)

            self.ui.buttonAuto.setDisabled(enable)
            self.ui.buttonMan.setDisabled(enable)
            self.ui.vertSliderPow.setValue(0)
            self.ui.vertSliderBrk.setValue(0)

    def Control_Emergency_Brake_External(self,ebrake_in):
        if ebrake_in == True:
            if self.ui.Ebrake.isChecked() == False:
                self.ui.Ebrake.toggle()
            enable = True
            
        else:
            if self.ui.Ebrake.isChecked() == True:
                self.ui.Ebrake.toggle()
            enable = False

        if(not(self.ui.buttonAuto.isChecked())):
            self.ui.buttonDoorL.setDisabled(enable)
            self.ui.buttonDoorR.setDisabled(enable)
            self.ui.temp.setDisabled(enable)
            self.ui.buttonHDoff.setDisabled(enable)
            self.ui.buttonHDon.setDisabled(enable)
            self.ui.IntLightSld.setDisabled(enable)
            self.ui.lineEditAnn.setDisabled(enable)
            self.ui.vertSliderBrk.setDisabled(enable)
            self.ui.vertSliderPow.setDisabled(enable)
            self.ui.inputKi.setDisabled(enable)
            self.ui.inputKp.setDisabled(enable)

        self.ui.buttonAuto.setDisabled(enable)
        self.ui.buttonMan.setDisabled(enable)
        self.ui.vertSliderPow.setValue(0)
        self.ui.vertSliderBrk.setValue(0)



    def Control_Signal_Failure(self,sig_fail):
            if(sig_fail == True):
                self.ui.SigFail.setStyleSheet("color: red;\n"
                                            "background-color: rgb(255, 255, 255);")
                self.ui.vertSliderPow.setValue(0)
                self.ui.vertSliderBrk.setValue(1)
                self.ui.vertSliderPow.setDisabled(True)
                self.ui.vertSliderBrk.setDisabled(True)
            else:
                self.ui.SigFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                        "background-color: rgb(255, 255, 255);")
                self.ui.vertSliderPow.setDisabled(False)
                self.ui.vertSliderBrk.setDisabled(False)


    def Control_Power_Failure(self,pwr_fail):
            if pwr_fail == True:
                self.ui.PwrFail.setStyleSheet("color: red;\n"
                                            "background-color: rgb(255, 255, 255);")
                self.ui.vertSliderPow.setValue(0)
                self.ui.vertSliderBrk.setValue(1)
                self.ui.vertSliderPow.setDisabled(True)
                self.ui.vertSliderBrk.setDisabled(True)
            else:
                self.ui.PwrFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                        "background-color: rgb(255, 255, 255);")
                self.ui.vertSliderPow.setDisabled(False)
                self.ui.vertSliderBrk.setDisabled(False)


    def Control_Brake_Failure(self,brk_fail):
            if(brk_fail == True):
                self.ui.BrkFail.setStyleSheet("color: red;\n"
                                        "background-color: rgb(255, 255, 255);")
                self.ui.Ebrake.setChecked(True)
            #DISABLE
            else:
                self.ui.BrkFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                        "background-color: rgb(255, 255, 255);")