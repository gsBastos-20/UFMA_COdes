impar = 0
for i in range(1, 501,2):
    if i % 3 == 0:
        impar += i
print(f'A soma de todos os numeros imapares ,multiplos de 3 é {impar}')