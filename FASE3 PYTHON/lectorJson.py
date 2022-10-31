import json
from operator import mod
import re
from datetime import datetime

from aiohttp import Payload
import pruebaTrabajo


def leerJson(ubicacion):
    # ubicacion = "Fase2.json"
    # print(ubicacion)

    fichero = open(ubicacion)

    dataJson = fichero.read()

    fichero.close()
    

    # Convertir cadena de caracteres JSON a un diccionario
    datos_diccionario = json.loads(dataJson)
    
    # print(datos_diccionario["usuarios"])

    # for i in (datos_diccionario["usuarios"]):
    #     print(i["nick"] +" "+ i["password"])
    
    # cuac = re.findall(r'-?\d+\.?\d*', dataJson)
    # cuac = list(set(cuac))
    # x = dataJson
    # for i in cuac:
    #     # x = dataJson.replace(i,("\""+ i+"\""))
    #     dataJson = re.sub(i, ("\""+ i+"\""), dataJson)



    # cadena_reemplazada = re.sub('-?\d+\.?\d*', replacedd(), dataJson)

   

        

    # print(dataJson)
    # print(datos_diccionario)
    
    return datos_diccionario



def escribir_json(prefijo):
    now = datetime.now()
    date = str(now.day) + str(now.month) + str(now.year) + str(now.hour) + str(now.minute) + str(now.second)
    # print(date)

    nonce, CadenaEvaludada = pruebaTrabajo.prueba_de_Trabajo(date, prefijo)
    
    info = {}
    # info['clients'] = []
    info['INDEX'] = "0"
    info['TIMESTAMP'] = str(now)
    info['NONCE'] = str(nonce)
    info['DATA'] = ""

    info['DATA'] = {}
    info['DATA']['FROM'] = ""
    info['DATA']['SKINS'] = []
    # info['DATA']['SKINS'].append({
    #     "SKIN": "985739",
    #     "VALUE": "4134"
    # })

    info['PREVIOUSHASH'] = "0000"
    info['ROOTMERKLE'] = ""
    info['HASH'] = (CadenaEvaludada)


    
    
    # data['clients'].append({
    # 'first_name': 'Theodoric',
    # 'last_name': 'Rivers',
    # 'age': 36,
    # 'amount': 1.11})

    with open('blockchain/bloque.json', 'w') as file:
        json.dump(info, file, indent=4)


def modJson(wallet, skin, value):
    with open('blockchain/bloque.json') as f:
        payloads = json.load(f)

    # payloads['DATA'] = {}
    payloads['DATA']['FROM'] = wallet
    # payloads['DATA']['SKINS'] = []
    payloads['DATA']['SKINS'].append({
        "SKIN": str(skin),
        "VALUE": str(value)
    })

    with open('blockchain/bloque.json', 'w') as file:
        json.dump(payloads, file, indent=4)


def modRoomerkle(data):
    with open('blockchain/bloque.json') as f:
        payloads = json.load(f)

    # payloads['DATA'] = {}
    payloads['ROOTMERKLE'] = data
    # payloads['DATA']['SKINS'] = []

    with open('blockchain/bloque.json', 'w') as file:
        json.dump(payloads, file, indent=4)

# escribir_json("0000")
# modJson("wallet", "skin", "value")
# modJson("wallet", "a", "3223")

