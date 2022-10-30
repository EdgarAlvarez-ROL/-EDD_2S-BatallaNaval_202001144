from hashlib import sha256

def prueba_de_Trabajo(date, prefijo):
    index = 0
    roomerkle = "a"
    # nonce = "0"
    Data= str(index) + date + "0000" + roomerkle
    CadenaEvaludada=""
    nonce=0
    # prefijo="0000"

    while True:
        nonce += 1
        CadenaEvaludada=Data+""+str(nonce)
        
        if(str(sha256(CadenaEvaludada.encode('utf-8')).hexdigest()).find(prefijo)==0):
            print(nonce, sha256(CadenaEvaludada.encode('utf-8')).hexdigest())
            CadenaEvaludada = sha256(CadenaEvaludada.encode('utf-8')).hexdigest()
            break;
    
    return nonce, CadenaEvaludada