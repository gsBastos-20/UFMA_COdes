v = []
for i in range(1, 5 + 1):
    num = int(input("Digite um numero: "))
    v.append(num)
   
menor = min(v)
maior = max(v)

posiçao_maior = [i for i, v in enumerate(v) if v == maior]
posiçao_menor = [i for i, v in enumerate(v) if v == menor]

print(f"\nA lista completa é {v}")
print(f"O maior numero é {maior} se encontra na posiçao {posiçao_maior}")
print(f"O maior numero é {menor} se encontra na posiçao {posiçao_menor}")