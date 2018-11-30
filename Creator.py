from Temporal import Variable 
from loginData import LoginData 
from alarmData import AlarmData 
from statusInformation import StatusInformation
from locationData import LocationData

class concreteCreator (object):

    def factory(self,chain): 
        var=Variable(chain)
        if(var.poNum == "01"):
            cc = LoginData(var.infCont)
            return cc.information()
        if(var.poNum == "12"):
            cc = LocationData(var.infCont)
            return cc.information()
        if(var.poNum == "16"):
            cc = AlarmData(var.infCont)
            return cc.information()
        if(var.poNum == "13"):
            cc = StatusInformation(var.infCont)
            return cc.information()
        return "Numero de protocolo invalido"
