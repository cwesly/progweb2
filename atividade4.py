'''
Atividade - 04 - Vetor
Monte um cadastro simples de pessoas com nome, idade, altura , estudante e hobbies:

nome    string
idade     int
altura     float
estudante True
hobbies :   list [ 'futebol', 'musica', 'programação']

Use  while para cadastrar vários alunos e mostrar no final. Para sair Aperte "N"
'''
cadastro_pessoas = []
resposta = ""
while resposta != "n":
    resposta = input("Deseja realizar um cadastro (n - sair)?: ")

    if resposta == "n":
        break

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    estudante = bool(input("É estudante (vazio p/ não)? "))
    hobies = input("Seus hobbies: ") 
    cadastro_pessoas.append([nome, idade, altura, estudante, hobies])

print(cadastro_pessoas)