#funcion donde se cargaran los clientes en un
def cargar_clientes(archivo):
    #craremos una lista de clientes para que se guarden ahi
    clientes = []
    #Aqui sera donde rellenaremos la informacion para para cliente
    try:
        with open(archivo, 'r') as archivo_clientes:
            for linea in archivo_clientes.readlines():
                datos_cliente = linea.strip().split(',')
                cliente = {
                    "nombre": datos_cliente[0],
                    "direccion": datos_cliente[1],
                    "telefono": datos_cliente[2],
                    "correo": datos_cliente[3],
                    "pais": datos_cliente[4],
                    "compras": []
                }
                clientes.append(cliente)
        return clientes
    except FileNotFoundError:
        return []

#Aqui sera donde se guardaran los clientes
def guardar_cliente(cliente, archivo):
    with open(archivo, 'a') as archivo_clientes:
        archivo_clientes.write(f"{cliente['nombre']},{cliente['direccion']},{cliente['telefono']},{cliente['correo']},{cliente['pais']}\n")

#funcion en la que guardaremos las compras
def guardar_compra(cliente, archivo):
    archivo_compras = archivo.format(cliente['nombre'])
    #se guardara en un archivo de compras
    with open(archivo_compras, 'a') as archivo_compras_cliente:
        for compra in cliente["compras"]:
            productos = ",".join(f"{producto['nombre']}:{producto['precio']}" for producto in compra["productos"])
            archivo_compras_cliente.write(f"{productos}\n")
