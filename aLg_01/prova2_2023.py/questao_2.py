def criaVetores(inicio, fim):
    v = []
    for i in range(inicio, fim+1):
        v.append(i)
    return v
    
começa = int(input("Digite um nuemro: "))
fim = int(input("Digite um numero: "))

print(criaVetores(começa, fim))
