class StatusInformation(object):
    def __init__(self,infCont):
        self.procesar(infCont)

    def procesar(self,infCont):
        #status information
        self.__terminalInfCont=infCont[0:2]
        self.__voltageLevel=infCont[2:4]
        self.__GSMsignalStrength=infCont[4:6]
        self.__alarmLanguage=infCont[6:10]
        self.Statusinfo()

    def hextobin(self,cadena):
        my_hexdata = cadena
        scale = 16 ## equals to hexadecimal
        num_of_bits = 16
        x = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
        return x  
    

#status information formating
    def Statusinfo(self):
        #Terminal information     
        if self.__voltageLevel == '00':
            self.__voltageLevel  = "No power(shutdown)"
        elif self.__voltageLevel == '01':
            self.__voltageLevel  = "Extreme Low Battery"
        elif self.__voltageLevel == '02':
            self.__voltageLevel  = "Very Low Battery"
        elif self.__voltageLevel == '03':
            self.__voltageLevel  = "Low Battery"
        elif self.__voltageLevel == '04':
            self.__voltageLevel  = "Medium"
        elif self.__voltageLevel == '05':
            self.__voltageLevel  = "High"
        elif self.__voltageLevel == '06':
            self.__voltageLevel  = "Very High"
        else:
            self.__voltageLevel  = "FORMAT ERROR"
           
        
    def information(self):
        return "Status Information Data Packet " + self.__terminalInfCont+"\n"+"Voltage Level: "+self.__voltageLevel+" GSM Signal Strength: "+self.__GSMsignalStrength+"\n"+"Alarm/Language: "+self.__alarmLanguage+"\n"+"¡QUAK!"
