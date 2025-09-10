'''
Atividade - 03 - Strings
1. Receber Nomes e Notas de Alunos e Imprimir Maior Nota

nomes = []
notas = []
nomeAluno = ""
notaAluno = -1
maior_nota = -999999
controle = 0

while nomeAluno != "n":
    nomeAluno = input("Digite um nome (n - sair):")
    if nomeAluno == "n":
        print(f"A maior nota é: {maior_nota}")
        break
    
    notaAluno = float(input(f"Digite a nota de {nomeAluno}: "))
    nomes.append(nomeAluno)
    notas.append(notaAluno)
    controle = controle + 1
    
    if notaAluno > maior_nota:
        maior_nota = notaAluno

for i in range(len(nomes)):
    print(nomes[i], end= " ")
    print(notas[i])
'''
#2 - Escreve um programa que dada uma String A, substitua todas as ocorrências de "banana" por "Maçã"
'''
frase = input("Escreva uma frase com banana: ")
frase = frase.replace("banana", "maçã")
print(frase)
'''
#3. Escreva um programa que receba um texto e troque todas as vogais por A
'''
vogal = "aeiouAEIOU"
frase = input("Escreva uma frase: ")
fraseModificada = ""

for letra in frase:
    if letra in vogal:
        fraseModificada += "A"
    else:
        fraseModificada += letra

print(fraseModificada)
'''
#4. Escreva um programa que receba nome do usuário e escreva de trás para frente.

'''
nome = input("Escreva seu nome: ")
nomeReverso = ""

for i in range(len(nome)-1, -1, -1):
    nomeReverso += nome[i]
print(f"O seu nome reverso é: {nomeReverso}")
'''

#5. Peça ao usuário para inserir uma frase e conte quantas vezes uma letra específica aparece na frase usando o método `.count()`.
'''
letra_especifica = "a"
frase = input("Escreva uma frase: ")
numero_letra = frase[::-1].count(letra_especifica)
print(f"A letra {letra_especifica} aparece {numero_letra} vezes na frase.")
'''