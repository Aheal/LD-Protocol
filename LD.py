
## Todo lo que empieza con: 
## p   = package
## po  = protocol 
## inf = information
## cont = content
## Clase abstracta que recibe el mensaje, lo procesa y
## define el protocol number para determina el tipo 
## de objeto creado.
class abstractPackage(object):

    def __init__(self): 
        pass
    def __init__(self,chain): 
        self.__chain = chain 

        self.__pLen,self.__poNum,self.__infCont,self.__infSerialNum,self.__errChk = self.mochar() 

        print(f"""
        Hello Duck Fellas!

            * Chain = {self.__chain}
            * pLen = {self.__pLen}
            * poNum = {self.__poNum}
            * infCont = {self.__infCont}
            * infSerialNum = {self.__infSerialNum}
            * errChk = {self.__errChk}
        
        """) 

        self.factory()

    def mochar(self):

        temp = self.__chain[4:] 
        pLen = temp[:2]

        temp = self.__chain[6:] 
        poNum = temp[:2]
        
        infCont = self.__chain[8:-12]

        temp = self.__chain[-4:] 
        errChk = temp[-4:]

        temp = self.__chain[-8:]
        infSerialNum = temp[:-4] 
        return pLen, poNum, infCont, infSerialNum, errChk 
    
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

    def nepe(self): 
        print("Hey, Inheritance!")
   
class Login(abstractPackage): 

    def __init__(self): 
        print("i am alive!") 
        self.nepe()

    def nepe(self): 
        abstractPackage.nepe(self)


nepe = abstractPackage("78780D01ROMANES00018CDD0D0A") 

