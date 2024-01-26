import time

class Elevador:
    
    def __init__(self, atualCapacidade,andarSelecionado):
        self.totalCapacidade = 6
        self.atualCapacidade = atualCapacidade
        self.totalAndar = 10
        self.atualAndar = 0
        self.andarSelecionado = andarSelecionado
        self.terreo = 0

    def subir(self):
        while True:
            if self.atualCapacidade < 6:
                self.andarSelecionado = int(input("Selecione o andar desejado: "))   
                while self.atualAndar == self.totalAndar and self.andarSelecionado == self.atualAndar:
                    print("Você está no andar mais alto!")
                    self.andarSelecionado = int(input("Selecione o andar desejado: "))
                self.descer()
                while self.atualAndar == self.terreo and self.andarSelecionado == self.terreo:
                    print("Você está no Térreo!")
                    time.sleep(2)
                    self.subir()
                if self.atualAndar > self.andarSelecionado:
                    self.descer()
                while self.atualAndar < self.andarSelecionado:
                    self.atualAndar +=1               
                    print (f"Subindo!")
                    self.atualAndar = self.andarSelecionado
                    print (f"{self.atualAndar}º andar")
                    time.sleep(2)
            else: 
                print("ELEVADOR LOTADO, aguarde novamente!")
                for n in range (6,1,-1):
                    n-=1
                    print(n)
                    time.sleep(1)
                self.atualCapacidade -= 1
                self.subir()

    def descer(self):
        if self.atualAndar == self.totalAndar or self.atualAndar > self.andarSelecionado:
            while True:
                if self.atualAndar == self.terreo:
                    print("Você está no Térreo!")
                    time.sleep(2)
                    self.subir()
                elif self.atualAndar < self.andarSelecionado:
                    self.subir()
                while self.atualAndar > self.andarSelecionado:
                    self.atualAndar -=1               
                    print (f"Descendo!")
                    time.sleep(2)
                    self.atualAndar = self.andarSelecionado
                    print (f"{self.atualAndar}º andar")
                    self.subir()

# ---------------------------------------------------------------------------------------------------

Atlas = Elevador(atualCapacidade=6, andarSelecionado=None)
Atlas.subir()
Atlas.descer()

             





   

     
     



