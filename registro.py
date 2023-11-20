#importaremos los modulos
from clientes import cargar_clientes, guardar_cliente, guardar_compra
from compras import realizar_compra, calcular_total

#Aqui tendremos los clientes registrados
def clientes_registrados(archivo):
    return cargar_clientes(archivo)

#Aqui sera donde podremos visualizar los clientes
def visualizar_clientes(archivo):
    print("\nClientes Registrados:")
    try:
        clientes = cargar_clientes(archivo)
        if not clientes:
            print("No hay clientes registrados.")
        else:
            for i, cliente in enumerate(clientes, 1):
                print(f"{i}. Nombre: {cliente['nombre']}, Teléfono: {cliente['telefono']}, Correo: {cliente['correo']}")
        print("\n")
    except Exception as e:
        print(f"Error al visualizar clientes: {e}")

#Aqui crearemos la funcion de realizar compra donde llamaremos a variables para que se pueda ejecutar en condiciones
def realizar_compra_cliente(cliente, archivo_clientes, archivo_compras_formato):
    try:
        if not cliente:
            print("Cliente no encontrado.")
            return

        print("\nRealizar Compra:")
        productos = []

        while True:
            nombre_producto = input("Nombre del Producto (dejar en blanco para finalizar): ")

            if not nombre_producto:
                break

            precio_producto = float(input("Precio del Producto: "))
            nuevo_producto = {"nombre": nombre_producto, "precio": precio_producto}
            productos.append(nuevo_producto)

        if not productos:
            print("No se agregaron productos a la compra.")
            return

        # Buscamos el cliente en la lista de clientes registrados usando el nombre
        cliente_actualizado = next(
            (c for c in clientes_registrados if c['nombre'] == cliente['nombre']), None
        )

        # Realizamos la compra con el cliente actualizado
        compra = realizar_compra(cliente_actualizado, productos)
        print(f"\nCompra realizada con éxito. Total: ${calcular_total(compra, productos)}\n")
        guardar_compra(cliente_actualizado, archivo_compras_formato)
    except ValueError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Error durante la compra: {error}")

#Aqui tendremos la funcion de registrar clientes
def registrar_cliente(archivo_clientes):
    print("Registro de Cliente:")
    #Aqui nos pedira la informacion para el registro de cliente
    try:
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        correo = input("Correo electrónico: ")
        pais = input("País: ")

        if not nombre or not direccion or not telefono or not correo or not pais:
            raise ValueError("Todos los campos son obligatorios.")

        nuevo_cliente = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "pais": pais,
            "compras": []
        }

#aqui guardaremos el resgistro del cliente
        guardar_cliente(nuevo_cliente, archivo_clientes)
        print(f"\n¡Cliente {nombre} registrado con éxito!\n")
    except ValueError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Error durante el registro del cliente: {error}")
