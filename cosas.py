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
