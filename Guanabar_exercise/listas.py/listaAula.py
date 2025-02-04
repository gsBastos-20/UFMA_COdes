'''num = [2, 3, 6, 1, 5]
num.insert(2, 7)


print(f"Essa lista tem {len(num)} elementos")
print(num[3])

num[3] = 9

print(num[3])

num.append(10)
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)
print(f"Essa lista tem {len(num)} elementos")

print(num)

num.pop()

print(num)

num.pop(2)

print(num)

num.remove(3)
print(num)

valores = []
valores.append(2)
valores.append(3)
valores.append(5)
valores.append(7)
for v in valores:
    print(f"os valor é: {v}", end=" ") 


valores = []
valores.append(2)
valores.append(3)
valores.append(5)
valores.append(7)

for c, v in enumerate(valores):
   print(f" Na posiçao {c} o valor é: {v}")'''
lista = []
for num in range(1, 5):
    v = int(input("Digite um numero: "))
    lista.append(v)
print(lista)


print("------------------------")


for c, v in enumerate(lista):
   print(f" Na posiçao {c} o valor é: {v}")



