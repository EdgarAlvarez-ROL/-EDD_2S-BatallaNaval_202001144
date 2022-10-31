from hashlib import sha256
from sys import prefix

def hash_ID(Data):
    # Data
    # prefijo="0000"
    nonce = 0
    prefijo = "0000"

    while True:
        nonce += 1
        CadenaEvaludada=Data+""+str(nonce)
        
        if(str(sha256(CadenaEvaludada.encode('utf-8')).hexdigest()).find(prefijo)==0):
            print(nonce, sha256(CadenaEvaludada.encode('utf-8')).hexdigest())
            CadenaEvaludada = sha256(CadenaEvaludada.encode('utf-8')).hexdigest()
            break;
    
    return CadenaEvaludada