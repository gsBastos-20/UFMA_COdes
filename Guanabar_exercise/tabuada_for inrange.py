n1 = int(input("Vocé vai querer a tabuada de qual nuemro: "))
ope = input("escolha a operaçao: ")
for i in range(1, 11):
    if ope == "soma":
        print(n1 + i)
    elif ope == "subtraçao":
        print(n1 -i)
    elif ope == "multiplicaçao":
        print(n1 * i)
    elif ope == "divisao":
        print(n1 / i)
    