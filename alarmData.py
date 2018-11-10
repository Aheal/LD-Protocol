class LocationData(object):

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
        self.__cantSatellitesGPS = self.__infCont[13:15]
        self.__latitud = self.__infCont[15:23]
        self.__longitud = self.__infCont[23:31]
        self.__speed = self.__infCont[31:33]
        self.__courseStatus = self.__infCont[33:37]
        #LBS Information
        self.__LBSlength = self.__infCont[37:39]
        self.__MCC = self.__infCont[39:43]
        self.__MNC = self.__infCont[43:45]
        self.__LAC = self.__infCont[45:49]
        self.__CellID = self.__infCont[49:55]
        #statusInformation
        self.__terminalInfCont=self.__infCont[55:57]
        self.__voltageLevel=self.__infCont[57:59]
        self.__GSMsignalStrength=self.__infCont[59:61]
        self.__alarmLanguage=self.__infCont[61:65]



    #Separacion de la fecha
    def dateTime(self):
        self.__Year = int(self.__dateTime[:2],10)
        self.__Month = int(self.__dateTime[3:5],10)
        self.__Day = int(self.__dateTime[5:7],10)
        self.__Hour = int(self.__dateTime[7:9],10)
        self.__Minute = int(self.__dateTime[9:11],10)
        self.__Second = int(self.__dateTime[11:13],10)

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
        self.__course = hextobin(self.__courseStatus)

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
        self.__     
        self.__terminalInfCont = hextobin(self.__terminalInfCont)
        if self.__voltageLevel == '00':
            self.__voltageLevel  = "No power(shutdown)"
        else if self.__voltageLevel == '01':
            self.__voltageLevel  = "Extreme Low Battery":
        else if self.__voltageLevel == '02':
            self.__voltageLevel  = "Very Low Battery":
        else if self.__voltageLevel == '03':
            self.__voltageLevel  = "Low Battery":
        else if self.__voltageLevel == '04':
            self.__voltageLevel  = "Medium":
        else if self.__voltageLevel == '05':
            self.__voltageLevel  = "High":
        else if self.__voltageLevel == '06':
            self.__voltageLevel  = "Very High":
        else
            self.__voltageLevel  = "FORMAT ERROR":
           
        #numeros de satelites
        self.__satellites = int(self.__cantSatellitesGPS[2])
        #informacion de la direccion
        self.__course = hextobin(self.__courseStatus)

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