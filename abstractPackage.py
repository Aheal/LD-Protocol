
## Todo lo que empieza con: 
## p   = package
## po  = protocol 
## inf = information
## cont = content
## Clase abstracta que recibe el mensaje, lo procesa y
## define el protocol number para determina el tipo 
## de objeto creado.
class abtractPackage(object): 

    def __init__(self,chain): 
        self.__chain = chain 

        self.__pLen,self.__poNum,self.__infCont,self.__infSerialNum,self.__errChk = self.mochar() 

        print(f"""
        Hello Duck Fellas!

            * Chain = {self.__chain}
            * pLen = {self.__pLen}
            * infCont = {self.__infCont}
            * poNum = {self.__poNum}
            * infSerialNum = {self.__infSerialNum}
            * errChk = {self.__errChk}
        
        """)

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
   

nepe = abtractPackage("78780D01ROMANES00018CDD0D0A") 

