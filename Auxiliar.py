
def drop(): 
    print("Get the DUCK out of here!") 
    exit(0) 

## Quita el 0x del cast a hex y agrega 0 de ser necesario
## esto por el formato del mensaje
def hexValidate(bytesAmount): 
    bytesAmount = bytesAmount[2:]
    bytesAmount = bytesAmount.upper() 
    if len(bytesAmount) == 1:
        bytesAmount = "0" + bytesAmount 
    return bytesAmount

##
def validate(chain): 

    chainLen = len(chain)
    bytesAmount = str(hex(int((chainLen / 2)-7))) 
    bytesAmount = hexValidate(bytesAmount)
    

    print(f"Chain Length (char): {chainLen}") 
    print(f"Bytes Amount: {bytesAmount}")

    start = chain[:4]   
    print(f"Start: {start}")
    if start != "7878": drop() 
    
    end = chain[-4:] 
    print(f"End: {end}")
    if end != "0D0A": drop() 
    
    temp = chain[4:]
    pLen = temp[:2] 
    try: 
        pLen = int(temp[:2])
    except: 
        pass 

    print(f"pLen: {pLen}")
    if pLen != bytesAmount: drop()

    print("All good Ducky fellas!") 
    return True


chain = "78780A01ANDRESESPAPUSI00018CDD0D0A"

validate(chain)
    