from datetime import datetime, timedelta

#1. Crie um programa que exiba a data e hora atual no formato:
#Hoje é 18/09/2025 e agora são 11:40
'''
data_hora_atual = datetime.now()
print(f"Hoje é {data_hora_atual.strftime('%d/%m/%Y')} e agora são {data_hora_atual.strftime('%H:%M')}")
'''

#2. Crie uma função que receba uma data de nascimento no formato dd/mm/aaaa e retorne a idade da pessoa.
'''
def transformacao_data_nascimento(data_nascimento):
    data_hoje = datetime.now()
    idade = data_hoje.year - data_nascimento.year
    print(idade)
    

data_nascimento_str = input("Digite sua data de nascimento: ")
data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')
transformacao_data_nascimento(data_nascimento)
'''
#3. Mostre a data de ontem, hoje e amanhã usando timedelta.
'''
hoje = datetime.now()

um_dia = timedelta(days=1)

ontem = hoje - um_dia
amanha = hoje + um_dia

print(f"Ontem foi {ontem.strftime('%d/%m/%Y')}, hoje é {hoje.strftime('%d/%m/%Y')} e amanhã é {amanha.strftime('%d/%m/%Y')}.")
'''

#4 Você recebeu a string "2025-05-10 14:30".
#Converta para um objeto datetime e exiba apenas a hora (14:30).
'''
data_str = "2025-05-10 14:30"

data = datetime.strptime(data_str, '%Y-%m-%d %H:%M')
hora = data.strftime('%H:%M')

print(hora)
'''
#5. Faça um programa que calcule quantos dias faltam para o próximo Natal (25/12 do ano atual).
'''
'''
hoje = datetime.now()
natal = datetime(year=hoje.year, month=12, day=25)
tempo_restante = natal - hoje

print(f"Faltam {tempo_restante.days} dias para o natal.")