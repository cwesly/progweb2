import json
import random
import math
import datetime

MEDIA_APROVACAO = 7.0
NUMERO_DE_NOTAS = 3

alunos_base = [
    {"matrícula": 101, "nome": "Ana Silva"},
    {"matrícula": 102, "nome": "Bruno Costa"},
    {"matrícula": 103, "nome": "Carla Martins"},
    {"matrícula": 104, "nome": "Daniel Moreira"},
    {"matrícula": 105, "nome": "Elisa Fernandes"}
]

print(f"Iniciando processamento de {len(alunos_base)} alunos...")

alunos_resultados = []

data_avaliacao = datetime.datetime.now().isoformat()

for aluno in alunos_base:
    notas = []
    for i in range(NUMERO_DE_NOTAS):
        nota = random.uniform(0.0, 10.0)
        notas.append(round(nota, 1))
    
    soma_das_notas = math.fsum(notas)
    media = soma_das_notas / len(notas)

    if media >= MEDIA_APROVACAO:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    
    aluno_final = {
        "matrícula": aluno["matrícula"],
        "nome": aluno["nome"],
        "notas": notas,
        "media": round(media, 2),
        "situacao": situacao
    }

    alunos_resultados.append(aluno_final)

dados_finais = {
"titulo": "Relatório de Avaliação",
"data_avaliacao": data_avaliacao,
"media_para_aprovacao": MEDIA_APROVACAO,
"alunos": alunos_resultados
}

json_resultado = json.dumps(dados_finais, indent=4, ensure_ascii=False)

print(json_resultado)