class AlarmData(object):

    def __init__(self,chainmochada):
        self.__infCont = chainmochada


    def GPS_HR(self,hex):
        a = int(hex,16)
        b= a/30000.0
        degrees = b//60
        minutes = b%60
        print (degrees, ' degrees and ', round(minutes,4), 'minutes' )
    
    #asignacion de partes del paquete Alarm Data
    def assignarMain(self):
        self.__dateTime = self.__infCont[12:]
        #GPS Information
        self.__cantSatellitesGPS = self.__infCont[12:14]
        self.__latitud = self.__infCont[14:22]
        self.__longitud = self.__infCont[22:30]
        self.__speed = self.__infCont[30:32]
        self.__courseStatus = self.__infCont[32:36]
        #LBS Information
        self.__LBSlength = self.__infCont[36:38]
        self.__MCC = self.__infCont[38:42]
        self.__MNC = self.__infCont[42:44]
        self.__LAC = self.__infCont[44:48]
        self.__CellID = self.__infCont[48:54]
        #statusInformation
        self.__terminalInfCont=self.__infCont[54:56]
        self.__voltageLevel=self.__infCont[56:58]
        self.__GSMsignalStrength=self.__infCont[58:60]
        self.__alarmLanguage=self.__infCont[60:64]



    #Separacion de la fecha
    def dateTime(self):
        self.__Year = "20"+str(int(self.__dateTime[:2],16))
        self.__Month =  str(int(self.__dateTime[2:4],16))
        self.__Day = str(int(self.__dateTime[4:6],16))
        self.__Hour = str(int(self.__dateTime[6:8],16))
        self.__Minute = str(int(self.__dateTime[8:10],16))
        self.__Second = str(int(self.__dateTime[10:12],16))

    def hextobin(self,cadena):
        my_hexdata = cadena
        scale = 16 ## equals to hexadecimal
        num_of_bits = 16
        x = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
        return x  
    
    #infomcion de la direccion en el GPS
    def GPSinfo(self):
        #numero de bits en la informacion de GPS
        self.__lenghtGPSinfo = int(self.__cantSatellitesGPS[1])
        #numeros de satelites
        self.__satellites = int(self.__cantSatellitesGPS[2])
        #informacion de la direccion
        self.__course = self.hextobin(self.__courseStatus)

        if self.__course[2] == '1':
            self.__GPSstatus = "real-time"
        else:
           self.__GPSstatus = "differential position" 
        if self.__course[3] == '1':
            self.__GPSposition = "GPS is positioned"
        else:
           self.__GPSposition = "GPS is not positioned"
        if self.__course[4] == '1':
            self.__GPSlongituddir = "East Longitud"
        else:
           self.__GPSlongituddir = "West Longitud"
        if self.__course[5] == '1':
            self.__GPSlatituddir = "North Latitud"
        else:
           self.__GPSlatituddir = "South Latitud"
        self.__courseDegrees = int(self.__course,10)
        

    #status information formating
    def Statusinfo(self):
        #Terminal information     
        self.__terminalInfCont = self.hextobin(self.__terminalInfCont)
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
           
        #numeros de satelites
        self.__satellites = int(self.__cantSatellitesGPS[2])
        #informacion de la direccion
        self.__course = self.hextobin(self.__courseStatus)

        if self.__course[2] == '1':
            self.__GPSstatus = "real-time"
        else:
           self.__GPSstatus = "differential position" 
        if self.__course[3] == '1':
            self.__GPSposition = "GPS is positioned"
        else:
           self.__GPSposition = "GPS is not positioned"
        if self.__course[4] == '1':
            self.__GPSlongituddir = "East Longitud"
        else:
           self.__GPSlongituddir = "West Longitud"
        if self.__course[5] == '1':
            self.__GPSlatituddir = "North Latitud"
        else:
           self.__GPSlatituddir = "South Latitud"
        self.__courseDegrees = int(self.__course,10)