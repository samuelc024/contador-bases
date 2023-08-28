from contador import *
m=Cronometro()
opcion=input("Escoja la base en la cual quiere contar:\n 1.Decimal ")
print("¿Cuanto desea contar?")
b=int(input())
if a=="decimal" or "Decimal":
    for i in range (0,b+1):
        print(m.decimal.valor)
        m.decimal.avanzar()
elif a=="binario" or "Binario":
    for i in range (b):
        m.decimal.avanzar()
        print(bin(m.decimal.valor))
elif a=="octal" or "Octal":
    for i in range (0,b+1):
        m.decimal.avanzar()
        print(oct(m.decimal.valor))
elif a=="hexal" or "hexadecimal":
    for i in range (b):
        m.decimal.avanzar()
        print(hex(m.decimal.valor))   
   
    