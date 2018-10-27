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
        
    def nepe(self): 
        print("Hey, Inheritance!")
