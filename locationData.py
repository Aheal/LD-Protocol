class LocationData(object):

    
    def __init__(self,infCont):
        self.procesar(infCont)

    def procesar(self,infCont):
        #GPS INFORMATION
        self.__dateTime = infCont[:12]
        print(self.__dateTime)
        self.dateTime()

        self.__cantSatellitesGPS = infCont[12:14]
        self.__latitud = infCont[14:22]
        self.__longitud = infCont[22:30]
        self.__speed = infCont[30:32]
        self.__courseStatus = infCont[32:36]
        self.GPSinfo()
        #LBS INFORMATION
        self.__MCC = infCont[36:40]
        self.__MNC = infCont[40:42]
        self.__LAC = infCont[42:46]
        self.__CellID = infCont[46:52]


    def GPS_HR(self,hex):
        a = int(hex,16)
        b= a/30000.0
        degrees = b//60
        minutes = b%60
        print (degrees, ' degrees and ', round(minutes,4), 'minutes' )        

    #Separacion de dateTime por partes
    def dateTime(self):
        #Pedos para convertir directo de hexa a int
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
        self.__lenghtGPSinfo = (self.__cantSatellitesGPS[0])
        #numeros de satelites
        self.__satellites = (self.__cantSatellitesGPS[1])

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
        
    def information(self):
        #return "Location Data Packet \nGPS Information \nDateTime: ",self.__Year, "-" ,self.__Month ,"-"+ self.__Day ," " ,self.__Hour ,":",self.__Minute,";",self.__Second,"\nQUACK"
        return "Location Data Packet \nGPS Information \nDateTime: " + self.__Year+ "-" +self.__Month +"-"+ self.__Day + " " +self.__Hour +":"+self.__Minute+";"+self.__Second+"\n"+"Lenght of GPS information: "+self.__lenghtGPSinfo+" Number of satelites: "+self.__satellites+"\n"   +"Latitud: " + self.__latitud + " Longitud: " + self.__longitud + "\n"        +"Speed: " + self.__speed + " Course Status: " + self.__courseStatus + "\n"+"LBS Information \n"        +"MCC: " + self.__MCC + " MNC: " + self.__MNC + "\n"+"LAC: " + self.__LAC + " Cell ID: " + self.__CellID + "\n"+"¡QUAK!"
