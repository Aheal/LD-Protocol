class LocationData(object):

    def __init__(self,chainmochada):
        self.__infCont = chainmochada


    def GPS_HR(self,hex):
        a = int(hex,16)
        b= a/30000.0
        degrees = b//60
        minutes = b%60
        print (degrees, ' degrees and ', round(minutes,4), 'minutes' )
    
    #asignacion de partes del paquete Location Data
    def assignarMain(self):
        self.__dateTime = self.__infCont[12:]
        self.__cantSatellitesGPS = self.__infCont[13:15]
        self.__latitud = self.__infCont[15:23]
        self.__longitud = self.__infCont[23:31]
        self.__speed = self.__infCont[31:33]
        self.__courseStatus = self.__infCont[33:37]

        self.__MCC = self.__infCont[37:41]
        self.__MNC = self.__infCont[41:43]
        self.__LAC = self.__infCont[43:47]
        self.__CellID = self.__infCont[47:53]

    #Separacion de la fecha
    def dateTime(self):
        self.__Year = int(self.__dateTime[:2],16)
        self.__Month = int(self.__dateTime[3:5],16)
        self.__Day = int(self.__dateTime[5:7],16)
        self.__Hour = int(self.__dateTime[7:9],16)
        self.__Minute = int(self.__dateTime[9:11],16)
        self.__Second = int(self.__dateTime[11:13],16)

    def hextobin(self,cadena):
        my_hexdata = cadena
        scale = 16 ## equals to hexadecimal
        num_of_bits = len(cadena)
        x = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
        return x  
    
    #infomcion de la direccion en el GPS
    def GPSinfo(self):
        #numero de bits en la informacion de GPS
        self.__lenghtGPSinfo = int(self.__cantSatellitesGPS[1],16)
        #numeros de satelites
        self.__satellites = int(self.__cantSatellitesGPS[2],16)
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
        
        self.__courseDegrees = int(self.__course,16)
    
        #self.__degreesLatitud = self.GPS_HR(self.__latitud)
        #self.__degreesLongitud = self.GPS_HR(self.__longitud)
        self.__decimalSpeed = int(self.__speed,16)
        