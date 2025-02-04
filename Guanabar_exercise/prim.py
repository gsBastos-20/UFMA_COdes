num = int(input("Digite umn numero: "))
eh_primo = True
if num < 2:
    eh_primo = False
else:
   for i in range(2, num):
       if num % i == 0:
           eh_primo = False
           break
if eh_primo:
    print(f"{num} é primo")
else:
    print(f"{num} nao é primo")           

   

   
