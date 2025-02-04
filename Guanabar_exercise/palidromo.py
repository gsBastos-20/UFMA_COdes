frase = input("Digite uma frase: ").replace(" ", "").lower()  
inversa = ""

for i in range(len(frase) -1, -1, -1):
    inversa += frase[i]

if frase == inversa:
    print("a frase é um palidromo")
else:
    print("A frase nao um palidromo")