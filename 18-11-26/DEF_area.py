def calcular_area_retangular(b,a):
    area = b * a
    return area

b = float(input("Digite a base do retângulo: "))
a = float(input("Digite a altura do retângulo: "))
print(f"A área do retângulo é: {calcular_area_retangular(b,a)}")
