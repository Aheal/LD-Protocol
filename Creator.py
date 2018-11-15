from Temporal import Variable 
from loginData import LoginData 
from alarmData import AlarmData 
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
        #if(variable.__poNum == "13"):
         #   cc=new concreteclass(variable.__infCont)
          #  return cc.information()
       # if(variable.__poNum == "15"):
        #    cc=new concreteclass(variable.__infCont)
         #   return cc.information()
        #if(variable.__poNum == "16"):
         #   cc=new concreteclass(variable.__infCont)
          #  return cc.information()
        #if(variable.__poNum == "80"):
         #   cc=new concreteclass(variable.__infCont)
          #  return cc.information()
        return "Numero de protocolo invalido"
