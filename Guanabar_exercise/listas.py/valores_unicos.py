valores = []
while True:
    n = int(input("Digite um valor: "))
    if n not in valores:
        valores.append(n)
        print("Valor adicionado com sucesso.")
    else:
        print("Valor duplicado, não podemos adicionar.")
    r = str(input("Quer continua? (sim ou não) "))
    if r in "Nn":
        break

print(f"Voçe digitou os valores {valores}")
