
def drop(): 
    print("Get the DUCK out of here!") 
    exit(0)

def validate(chain): 

    chainLen = len(chain)
    bytesAmount = chainLen / 2  

    print(f"Chain Length (char): {chainLen}") 
    print(f"Bytes Amount: {bytesAmount}")

    start = chain[:4]   
    print(f"Start: {start}")
    if start != "7878": 
        drop() 
    
    end = chain[-4:] 
    print(f"End: {end}")
    if end != "0D0A":
        drop() 
    
    temp = chain[4:]  
    pLen = temp[:2]  
    print(f"pLen: {pLen}")
    if pLen != bytesAmount: 
        drop()

    print("All good Ducky fellas!") 

chain = "787816protocolNinfoContentinfoSerialNerrorCeck0D0A"

validate(chain)
    