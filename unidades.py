class UnidadD:
    def __init__(self):
        self.valor=0
    def avanzar(self):
        self.valor+=1
class Unidadb:
    def __init__(self):
        self.valor=0
    def avanzar(self):
        self.valor+=1
             

    
if __name__=='__main__':
    u=UnidadD()
    cont=0
    while cont<20:
        print(u.valor)
        u.avanzar()
        cont+=1
