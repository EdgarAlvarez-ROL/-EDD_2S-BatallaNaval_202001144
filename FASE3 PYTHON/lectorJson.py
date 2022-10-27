import json
import re

cont = -1

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


# leerJson("")
