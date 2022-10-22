import json

def leerJson(ubicacion):
    # ubicacion = "C:/Users/wwwed/OneDrive/Escritorio/Fase 2/DATOS.json"
    # print(ubicacion)

    fichero = open(ubicacion)

    dataJson = fichero.read()

    fichero.close()

    # Convertir cadena de caracteres JSON a un diccionario
    datos_diccionario = json.loads(dataJson)
    
    # print(datos_diccionario["usuarios"])

    # for i in (datos_diccionario["usuarios"]):
    #     print(i["nick"] +" "+ i["password"])


    return datos_diccionario


# leerJson()