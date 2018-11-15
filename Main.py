from Temporal import Variable
from Creator import concreteCreator 

# Quita el 0x del cast a hex y agrega 0 de ser necesario esto por el formato del mensaje
def hexValidate(bytesAmount): 
    bytesAmount = bytesAmount[2:]
    bytesAmount = bytesAmount.upper() 
    if len(bytesAmount) == 1:
        bytesAmount = "0" + bytesAmount 
    return bytesAmount

#Valida si el mensaje que se recibe tiene el formato necesario para ser un Little Duck
def validate(chain):
    chainLen = len(chain)-10
    bytesAmount = str(hex(int(chainLen / 2))) 
    bytesAmount = int(hexValidate(bytesAmount))
    
    start = chain[:4]   
    if start != "7878": return False 
    end = chain[-4:] 
    if end != "0D0A": return False
    temp = chain[4:]
    pLen = temp[:2] 
    try: 
        pLen = int(temp[:2])
    except: 
        pass
    if pLen != bytesAmount:
        return False
    return True

#Main del protocolo, pensado para ser repetido, recibiendo un mensaje validandolo y generando una respuesta
def LittlestDuck(chain): 

    if(validate(chain)):
        creator=concreteCreator()
        respuesta=creator.factory(chain)
        print(respuesta)
    else: 
        respuesta="GET THE DUCK OUT OF HERE"
        print(respuesta)

#Mensaje de tipo LogIn
#chain = "78780D01012345678901234500018CDD0D0A"
#Mensaje de tipo Location Data
#chain = "78781F120B081D112E10CC027AC7EB0C46584900148F01CC00287D001FB8000380810D0A"
#Mensaje de tipo Alarm Data
chain = "787825160B0B0F0E241DCF027AC8870C4657E60014020901CC00287D001F726506040101003656A40D0A"

LittlestDuck(chain)
    
