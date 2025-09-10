#1
'''
a , b = 0 , 1
for i in range(10):
    print (a, end=" ")
    a , b = b, a + b
'''
#2
primos = 0
numero = 1
divisores = 0
while primos > 10:
    for i in range(1, numero):
        if numero % i:
            divisores += 1
    if divisores == 2:
        primos += 1
        divisores = 0
        print(numero)
        numero += 1

#3
numero = float(input("Digite um número para saber a raiz: "))
while numero != 0:
    raiz = numero ** 0.5
    print(f"A raiz quadrada de {numero} é {raiz: .4f}")
    numero = float(input("Digite um número para saber a raiz: "))
    
#4
numero = int(input("Digite um número:"))
for i in range(1,11):
    print(f"{i} X {numero} = {numero * i}")