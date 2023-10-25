class Calculadora:
    def __init__(self):
        pass

    def pedir_numero(self):
        try:
            numero = float(input("Ingresa un número: "))
            return numero
        except ValueError:
            print("Error: Ingresa un número válido.")
            return None

    def suma(self):
        numero1 = self.pedir_numero()
        numero2 = self.pedir_numero()

        if numero1 is not None and numero2 is not None:
            resultado = numero1 + numero2
            print(f"La suma de {numero1} y {numero2} es: {resultado}")


mi_calculadora = Calculadora()


mi_calculadora.suma()


class ManejoArchivos:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def leer_y_mostrar_contenido(self):
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
                print("Contenido del archivo:")
                print(contenido)
        except FileNotFoundError:
            print(f"El archivo '{self.nombre_archivo}' no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {str(e)}")


archivo_a_leer = ManejoArchivos('nombre_de_tu_

archivo_a_leer.leer_y_mostrar_contenido()



from PIL import Image
import random

class AsignadorImagenes:
    def __init__(self):
        self.asignaciones = {}

    def asignar_imagenes_automaticamente(self, cantidad):
        for numero in range(1, cantidad + 1):
            ruta_imagen = f'imagen{numero}.jpg'  # Suponiendo que las imágenes se llaman imagen1.jpg, imagen2.jpg, etc.
            imagen = Image.open(ruta_imagen)
            self.asignaciones[numero] = imagen

    def imprimir_imagen_al_azar(self):
        if self.asignaciones:
            numero_aleatorio = random.choice(list(self.asignaciones.keys()))
            imagen_aleatoria = self.asignaciones[numero_aleatorio]
            imagen_aleatoria.show()
        else:
            print("No hay imágenes asignadas.")


asignador = AsignadorImagenes()


asignador.asignar_imagenes_automaticamente(5)


asignador.imprimir_imagen_al_azar()




