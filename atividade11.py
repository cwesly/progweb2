'''
Atividade 11 - Dicionário
'''
#1. Escreva um programa que conte a frequência de palavras em uma frase e armazene o resultado em um dicionário.
'''
dados = {}
quantidadePalavras = 0

frase = input("Frase: ")
palavras = frase.split()

for palavra in palavras:
    if palavra in dados:
        dados[palavra] += 1
    else:
        dados[palavra] = 1

print(dados)
'''
#2. Crie um programa que calcule a média das notas de alunos e armazene os resultados em um dicionário onde as chaves são os nomes dos alunos e os valores são suas respectivas médias.
'''
dados = {}
aluno = ''
mediaAluno = 0

def mediaAlunos():
    quantidade = 0
    while quantidade < 3:
        aluno = input("Nome: ") 
        nota_1 = float(input("Nota 1: "))
        nota_2 = float(input("Nota 2: "))
        nota_3 = float(input("Nota 3: "))

        soma_notas = nota_1 + nota_2 + nota_3

        mediaAluno  = soma_notas / 3

        dados[aluno] = round(mediaAluno, 1)
        quantidade += 1

mediaAlunos()
print("/n", dados)
'''
#3. Desenvolva um programa que receba uma lista de compras (produto e quantidade) e crie um dicionário representando o carrinho de compras.
'''
carrinho_de_compras = {}

print("Digite os produtos e as quantidades. Digite 'fim' no nome do produto para encerrar.")

while True:
    produto = input("Nome do produto: ")
    if produto.lower() == 'fim':
        break

# Validação para garantir que a quantidade seja um número
while True:
    try:
        quantidade = int(input(f"Quantidade de '{produto}': "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro para a quantidade.")

carrinho_de_compras[produto] = quantidade
print("\n--- Carrinho de Compras Finalizado ---")
print(carrinho_de_compras)
'''
#4. Faça um programa que receba o nome de vários convidados para uma festa e armazene a quantidade de vezes que cada nome aparece em um dicionário.
'''
frequencia_convidados = {}

print("Digite os nomes dos convidados. Digite 'fim' para encerrar a lista.")

while True:
    nome = input("Nome do convidado: ")
    if nome.lower() == 'fim':
        break   

if nome in frequencia_convidados:
    frequencia_convidados[nome] += 1
else:
    frequencia_convidados[nome] = 1

print("\n--- Frequência de Nomes na Lista de Convidados ---")
print(frequencia_convidados)
'''
#5. Escreva um programa que receba uma data de nascimento (dia, mês, ano) e retorne o signo da pessoa usando um dicionário.
'''
resultado_signo = {}

dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
ano = int(input("Digite o ano de nascimento: "))

signo = ""
if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
signo = "Áries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
signo = "Touro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
signo = "Gêmeos"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
signo = "Câncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
signo = "Leão"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
signo = "Virgem"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
signo = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
signo = "Escorpião"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
signo = "Sagitário"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
signo = "Capricórnio"
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
signo = "Aquário"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
signo = "Peixes"
else:
signo = "Data inválida"

resultado_signo['data'] = f"{dia}/{mes}/{ano}"
resultado_signo['signo'] = signo

print("\n--- Resultado ---")
print(f"A pessoa nascida em {resultado_signo['data']} é do signo de {resultado_signo['signo']}.")
'''