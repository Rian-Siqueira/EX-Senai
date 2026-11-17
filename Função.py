def saudar(nome):
    print(f"Olá, {nome}!")

saudar("Ana")
saudar("João")
saudar("Maria")




def estatistica(nums):
    total = sum(nums)
    media = total / len(nums)
    return total, media

t,m = estatistica([8,9,7])
print(f"total: {t}, média:{m}")



def somar(a,b): return a + b
def subtrair(a,b): return a - b
def multiplicar(a,b): return a * b
def dividir(a,b):
    if b == 0: return "Erro: divisão por zero!"
    return a / b

while True:
    op = input("Operação (+-*/): ")
    if op == "0": break
    a  = float(input("Num 1: "))
    b  = float(input("Num 2: "))

# chamar função conforme a operação 
    if op == "+": print(somar(a,b))
    elif op == "-": print(subtrair(a,b))
    elif op == "*": print(multiplicar(a,b))
    elif op == "/": print(dividir(a,b))
    else: print("Operação inválida!")
   
