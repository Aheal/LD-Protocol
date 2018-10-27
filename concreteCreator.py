class concreteCreator (object):

    def factory(self): 

        if(self.__poNum == "01"):
            login  = Login()
            return login 
        if(self.__poNum == "12"):
            pass
        if(self.__poNum == "13"):
            pass
        if(self.__poNum == "15"):
            pass 
        if(self.__poNum == "16"):
            pass
        if(self.__poNum == "80"):
            pass 
        print("No duck here!") 
