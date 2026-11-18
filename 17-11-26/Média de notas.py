y = 0
for i in range (1, 5):
  p = float(input("Digite a nota do aluno: "))
  y += p
m = y/4
print("A média das notas é:", m)
if m >= 7:
  print("Aprovado")
elif m >= 5:
  print("Recuperação")
else:
  print("Reprovado")   