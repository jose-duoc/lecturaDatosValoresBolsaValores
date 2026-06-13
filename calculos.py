import json
def leer_y_calcular_total(nombre_archivo):
    monto_total_general = 0.0
    #Abrir archivo
    with open(nombre_archivo,'r',encoding='utf-8') as archivo:
        for linea in archivo:
            if "Data Recibida:" in linea:
                partes = linea.split("Data Recibida: ")
                json_puro = partes[1].strip()
                try:
                    compras = json.loads(json_puro)
                    for compra in compras:
                        monto_total_general += float(compra["monto"])
                except json.JSONDecodeError:
                    print("Error, se saltó línea")
    return monto_total_general
def obtener_estadisticas_clientes(nombre_archivo):
    estadisticas = {}
    with open(nombre_archivo,'r',encoding='utf-8') as archivo:
        for linea in archivo:
            if "Data Recibida:" in linea:
                partes = linea.split("Data Recibida: ")
                json_puro = partes[1].strip()
                try:
                    compras = json.loads(json_puro)
                    for compra in compras:
                        nombre = compra["cliente"]
                        monto = float(compra["monto"])
                        if nombre in estadisticas:
                            estadisticas[nombre]["compras"] +=1
                            estadisticas[nombre]["total_gasto"] += monto
                        else:
                            estadisticas[nombre] = {"compras":1,"total_gasto":monto}
                except json.JSONDecodeError:
                    continue
    return estadisticas