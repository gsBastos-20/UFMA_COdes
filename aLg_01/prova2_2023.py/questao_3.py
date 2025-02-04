def chaves(primos):
    v = []
    for i in range(len(primos)):
        for j in range(i+1, len(primos)):
           for k in range(j+1, len(primos)):
              razao = primos[i] * primos[j] * primos[k]
              v.append(razao)
    return v

a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))
d = int(input("Digite um numero: "))

print(chaves([a, b, c, d]))