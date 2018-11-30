class Variable (object):
    
    def __init__(self,chain): 
        self.__chain = chain 
        self.__pLen,self.poNum,self.infCont,self.__infSerialNum,self.__errChk = self.mochar() 
        

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
