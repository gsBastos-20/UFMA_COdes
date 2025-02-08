maior = 0
menor = float("inf")
for i in range(1, 5):
    peso = float(input("Digite o seu peso: "))
    if peso >= maior:
       maior = peso
    if peso <= menor:
        menor = peso
print(f"o maior peso é {maior}")
print(f"o menor peso é ")