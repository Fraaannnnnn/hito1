#importaremos desde el mdoulo registro
from registro import *
from clientes import *

#Crearemos el menu donde podremos elegir la opcion que decidamos
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Registrar Cliente")
    print("2. Visualizar Clientes")
    print("3. Realizar Compra")
    print("4. Salir")

#aqui crearemos las funciones de menu
def main():
    archivo_clientes = "clientes.txt"
    archivo_compras_formato = "compras_{}.txt"

    clientes_registrados = cargar_clientes(archivo_clientes)
#y aqui crearemos para que hagamos la eleccion de lo que queremos hacer
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1/2/3/4): ")
#tambien tendremos que llamar algunas variables para que se ejecute en condiciones
        if opcion == '1':
            registrar_cliente(archivo_clientes)
        elif opcion == '2':
            visualizar_clientes(archivo_clientes)
        elif opcion == '3':
            nombre_cliente = input("Nombre del Cliente para realizar la compra: ")
            cliente_seleccionado = next(
                (c for c in clientes_registrados if c['nombre'] == nombre_cliente), None
            )
            realizar_compra_cliente(
                cliente_seleccionado, archivo_clientes, archivo_compras_formato
            )
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
