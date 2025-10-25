import datetime
import random
import math

tarefas = [
    "Ler um capítulo de livro",
    "Fazer exercício físico",
    "Estudar um novo tópico",
    "Cozinhar uma refeição",
    "Meditar por 30 minutos",
    "Organizar a casa",
    "Assistir a um documentário"
]

tempos_gastos_minutos = []
tempo_total_gasto = datetime.timedelta(0)

for dia in range(7):
    tarefa = random.choice(tarefas)
    duracao_minutos = random.randint(20, 90)

    inicio_tarefa = datetime.datetime.now()

    duracao_delta = datetime.timedelta(minutes=duracao_minutos)
    fim_tarefa = inicio_tarefa + duracao_delta

    tempos_gastos_minutos.append(duracao_minutos)

    tempo_total_gasto += duracao_delta

    print(f"Dia {dia + 1} - Iniciando a tarefa: '{tarefa}' em {inicio_tarefa.strftime('%H:%M:%S')}")
    print(f"Tempo estimado: {duracao_minutos} minutos...")
    print(f"Tarefa '{tarefa}' concluída em {fim_tarefa.strftime('%H:%M:%S')}")
    print("\n" + "." * 60 + "\n")

print("--- Relatório Estatístico da Semana ---")
segundos_totais = tempo_total_gasto.total_seconds()
total_horas = math.floor(segundos_totais / 3600)
minutos_restantes = math.floor((segundos_totais % 3600) / 60)

print(f"Tempo total gasto na semana: {total_horas} horas e {minutos_restantes} minutos.")

soma_minutos = math.fsum(tempos_gastos_minutos)
media_minutos = soma_minutos / len(tempos_gastos_minutos)

print(f"Média de tempo por tarefa: {media_minutos:.2f} minutos.")

maior_duracao = max(tempos_gastos_minutos)
menor_duracao = min(tempos_gastos_minutos)

print(f"Maior duração em uma tarefa: {maior_duracao} minutos.")
print(f"Menor duração em uma tarefa: {menor_duracao} minutos.")