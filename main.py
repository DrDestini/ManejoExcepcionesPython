class ExcepcionVacio(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        
class ControlGastos:
    def __init__(self):
        self.gastos = []
    
    def cargar_gastos(self):
        try:
            nombre = input("Introduce el nombre del fichero:")
            with open(nombre, "r") as fich:
                for linea in fich:
                    lineaArgs = linea.strip().split('||')
                    gasto = {'descripcion':lineaArgs[0], 'coste':lineaArgs[1]}
                    if gasto not in self.gastos:
                        self.gastos.append(gasto)
        except FileNotFoundError as e:
            print(f"El fichero {nombre} no ha sido encontrado:\n{e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
      
    def anadir_gasto(self):
        try:
            descripcion = input("Introduce la descripción del gasto: ")
            coste = float(input("Introduce el coste: "))
            if coste < 0:
                raise ValueError("El coste no puede ser negativo.")
            self.gastos.append({"descripcion":descripcion, "coste":coste})
            print("Gasto añadido con éxito!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")    
    
    def ver_gastos(self):
        try:
            if not self.gastos:
                raise ExcepcionVacio("Se han encontrado 0 items.")
            print("\nGastos:")
            for i, gasto in enumerate(self.gastos):
                print(f"{i}. {gasto['descripcion']}: {gasto['coste']:.2f}€")
        except ExcepcionVacio as e:
            print(f"El libro de gastos está vacío: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
            
    def guardar_gastos(self):
        try:
            nombre = input("Introduce el nombre del archivo (ej: reporte.txt): ")
            with open(nombre, "w") as fich:
                for gasto in self.gastos:
                    fich.write(f"{gasto['descripcion']}||{gasto['coste']}")
                print(f"Gastos guardados con exito en la direccion:\n{fich.name}")
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
            except ValueError:
                print("Elección inválida. Introduce un número!")
            except Exception as e:
                print(f"Error inesperado. {e}")


             
if __name__ == "__main__":
    programa = ControlGastos()
    programa.run()