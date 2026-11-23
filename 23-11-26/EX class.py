class Produto:
    def __init__(self, nome, preço, estoque):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque

     #FORMA CURTA DE CHAMAR
    def exibir(self):
     print(f"produto: {self.nome}")
     print(f"Preço: {self.preço}")
     print(f"Estoque: {self.estoque}")
     print("-" *  80)

p1 = Produto("Arroz", 5.99, 30)
p2 = Produto("Macarrão", 8.5, 80)

print(type(p1))
print(p1)
print(p1  == p2)

#FORMA EXTENSA DE CHAMAR
print(p1.nome)
print(p1.preço)
print(p1.estoque)

p1.exibir()
p2.exibir()

#Exemplos 
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo   #Privado

    def get_saldo(self):  #getter
        return self.__saldo

    def depositar(self, valor):  #setter
        if valor > 0:
            self.__saldo += valor
                