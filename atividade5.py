#Atividade - 05- list e tuplas
#1. Dada uma lista de números, retorne os números que aparecem mais de uma vez sem repetir o resultado.

'''
# Entrada: [1, 2, 3, 4, 5, 3, 2, 6, 1] # Saída: [1, 2, 3]
lista = [1, 2, 3, 4, 5, 3, 2, 6, 1]
duplicados = []

for numero in lista:
    if lista.count(numero) > 1:
        if numero not in duplicados:
            duplicados.append(numero)
    else:
        print(f"Número {numero} não aparece mais de uma vez.")

duplicados.sort()
print(duplicados)

'''
#2.  Dada uma lista de strings, crie uma nova lista contendo apenas as palavras que possuem todas as suas letras em maiúsculo e que têm um comprimento maior que 4.

# Entrada: ['PYTHON', 'java', 'JAVASCRIPT', 'C', 'RUBY']
# Saída: ['PYTHON', 'JAVASCRIPT']
'''
lista = ['PYTHON', 'java', 'JAVASCRIPT', 'C', 'RUBY']
lista_maiuscula = []

for palavra in lista:
    if palavra.isupper() and len(palavra) > 4:
        lista_maiuscula.append(palavra)
    
print(lista_maiuscula)
'''
#3. Dada uma tupla contendo pares de números, retorne a soma de todos os segundos elementos de cada par.

# Entrada: ((1, 2), (3, 4), (5, 6))
# Saída: 12 (2 + 4 + 6)
'''
tuplas = ((1, 2), (3, 4), (5, 6))
soma = 0
for elemento in tuplas:
    print("Número a ser somado: ", elemento[1])
    soma += elemento[1]

print(f"Soma: {soma}")
'''
#4. Dada uma lista de tuplas, converta-a em uma lista de listas e, em seguida, aplique uma modificação: adicione 10 ao segundo elemento de cada sub-lista.

# Entrada: [(1, 2), (3, 4), (5, 6)]     # Saída: [[1, 12], [3, 14], [5, 16]]
'''
tuplas = [(1, 2), (3, 4), (5, 6)]
lista = []

for elemento in tuplas:
    sub_lista = list(elemento)
    sub_lista[1] += 10
    lista.append(sub_lista)

print(f"Lista de tuplas: {tuplas}")
print(f"Lista adicionada 10: {lista}")
'''

#5. Receba um numero pelo input e imprima a lista de números abaixo;
'''
ex.:

        input - 4

         1
         12
         123
         1234
         1234
         123
         12
         1
'''
numero = int(input("Digite um número: "))

for i in range(1, numero + 1):
    linha = ""
    for j in range(1, i + 1):
        linha += str(j)
    print(linha)

for i in range(numero, 0, -1):
    linha = ""
    for j in range(1, i + 1):
        linha += str(j)
    print(linha)