import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/Semana2/1.2.1. Desarrollo de Ejemplos de Técnicas de Programación.py',
        '2': 'Unidad 1/Semana3/1.3.1. Temperatura POO.py',
        '3': 'Unidad 1/Semana3/1.3.2. Temperatura Tradicional.py',
        '4': 'Unidad 1/Semana4/1.4.1. Ejemplos del Mundo Real y Características de la POO.py',
        '5': 'Unidad 2/Semana5/2.5.1. Tipos de datos, Identificadores.py',
        '6': 'Unidad 2/Semana6/2.6.1 Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '7': 'Unidad 2/Semana7/2.7.1. Constructores y Destructores.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()