#funcion para comprar
#llamaremos a clientes y productos
def realizar_compra(cliente, productos):
    nueva_compra = {"productos": productos}
    cliente["compras"].append(nueva_compra)
    return nueva_compra

#Aqui calcularemos el total de los precios de productos
def calcular_total(compra, lista_productos):
    return sum(producto["precio"] for producto in lista_productos if producto in compra["productos"])
