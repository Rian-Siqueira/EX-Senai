class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir (self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print("-" * 80)


c1 = Carro("Chana","CAOA Changan ", 2011 )
c2 = Carro("Dacia","Sandero", 2026 )

c1.exibir()
c2.exibir()