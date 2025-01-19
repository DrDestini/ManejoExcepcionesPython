'''
Excepciónes personalizadas que usaremos tanto cuando el array está vacío como cuando
se intenta añadir un gasto negativo al sistem.
'''
class ExcepcionVacio(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class ExcepcionNumPos(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

'''
Clase principal del programa, contiene el manejo de las siguientes excepciones:

Excepciones Personalizadas - Las excepciones definidas anteriormente que usaremos en caso de que el array esté vacío o el gasto introducido sea negativo
ValueError - Error que salta cuando se introduce un tipo de datos inválido
FileNotFoundError - Cuando el fichero requerido no se encuentra
IoError - Para los errores de entrada/salida de ficheros

(Exception) - Para las excepciones no esperadas que puedan ocurrir durante la ejecución
'''       
class ControlGastos:
    def __init__(self):
        self.gastos = []
    
    def cargar_gastos(self):
        try:
            nombre = input("Introduce el nombre del fichero:")
            with open(nombre, "r") as fich:
                for linea in fich:
                    lineaArgs = linea.strip().split('||')
                    gasto = {'descripcion':lineaArgs[0], 'coste':float(lineaArgs[1])}
                    if(gasto['coste'] < 0):
                        raise ExcepcionNumPos("El gasto no puede ser negativo")
                    if gasto not in self.gastos:
                        self.gastos.append(gasto)
            print("Fichero cargado con éxito!")
        except ExcepcionNumPos as e:
            print(f"Error en los datos del fichero: {e}")
        except ValueError as e:
            print(f"Error al leer el fichero. Datos corruptos.")
        except FileNotFoundError as e:
            print(f"El fichero {nombre} no ha sido encontrado: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
      
    def anadir_gasto(self):
        try:
            descripcion = input("Introduce la descripción del gasto: ")
            coste = float(input("Introduce el coste: "))
            if coste < 0:
                raise ExcepcionNumPos("El gasto no puede ser negativo")
            self.gastos.append({"descripcion":descripcion, "coste":coste})
            print("Gasto añadido con éxito!")
        except ExcepcionNumPos as e:
            print(f"Error al introducir el gasto: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")    
    
    def ver_gastos(self):
        try:
            if not self.gastos:
                raise ExcepcionVacio("Se han encontrado 0 items.")
            print("\nGastos:")
            total = 0
            for i, gasto in enumerate(self.gastos):
                print(f"{i}. {gasto['descripcion']}: {gasto['coste']:.2f}€")
                total += gasto['coste']
            print(f"--- TOTAL: {total:.2f}€ ---")
        except ExcepcionVacio as e:
            print(f"El libro de gastos está vacío: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
            
    def guardar_gastos(self):
        try:
            if not self.gastos:
                raise ExcepcionVacio("Se han encontrado 0 items.")
            nombre = input("Introduce el nombre del archivo (ej: reporte.txt): ")
            with open(nombre, "w") as fich:
                for gasto in self.gastos:
                    fich.write(f"{gasto['descripcion']}||{gasto['coste']}")
                print(f"Gastos exportados con éxito en el fichero: {fich.name}")
        except ExcepcionVacio as e:
            print(f"No hay nada que exportar: {e}")
        except IOError as e:
            print(f"Error de fichero: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    def run(self):
        while True:
            print("#------GESTION DE GASTOS-------#")
            print("1. Cargar datos")
            print("2. Añadir gasto")
            print("3. Ver datos")
            print("4. Exportar datos")
            print("5. Salir")

            try:
                eleccion = int(input("Elegir opcion: "))
                if eleccion == 1:
                    self.cargar_gastos()
                elif eleccion == 2:
                    self.anadir_gasto()
                elif eleccion == 3:
                    self.ver_gastos()
                elif eleccion == 4:
                    self.guardar_gastos()
                elif eleccion == 5:
                    print("Saliendo...")
                    break
                else:
                    print("Elección inválida. Intentelo de nuevo...")
                
                input("Pulsa [ENTER] para continuar...")
            except ValueError:
                print("Elección inválida. Introduce un número!")
            except Exception as e:
                print(f"Error inesperado. {e}")

'''
Casos a intentar:

(1) - Opcion inválida en el menú (ValueError)
(2) - Cargar un fichero inexistende (FileNotFoundError)
(3) - Ver gastos con array vacio (ExcepcionVacio)
(4) - Introducir un gasto con coste no numerico (ValueError)
(5) - Introducir un gasto con coste negativo (ExcepcionNumPos)
(6) - Modificar un fichero guardado e intentar cargar un fichero corrupto (ValueError)
(7) - Modificar el fichero con un gasto negativo (ExcepcionNumPos)

'''

if __name__ == "__main__":
    programa = ControlGastos()
    programa.run()