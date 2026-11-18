def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def km_para_milhas(km):
    milhas = km * 0.6214371
    return milhas

def kg_para_libras(kg):
    libras = kg * 2.2046
    return libras






while True:
    print("\n=== MENU ===" \
    "\n1 - Celsious para Fahrenheit" \
    "\n2 - km para milhas" \
    "\n3 - kg para libras" \
    "\n0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
     celsius = float(input("Digite a temperatura em Celsius: "))
     print(f"{celsius}°C é igual a {celsius_para_fahrenheit(celsius):.2f}°F")
   
    elif opcao == "2":
        km = float(input("Digite a distancia em km:"))
        print(f"{km} km é igual a {km_para_milhas(km):.2f} milhas")

    elif opcao == "3":
        kg = float(input("Digite o peso em kg:"))
        print(f"{kg} kg é igual a {kg_para_libras(kg):.2f} libras")

    elif opcao == "0":
        print("Saindo do programa...")
        break    

    else:
        print("Opção inválida.")

