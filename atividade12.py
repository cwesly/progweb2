'''
Atividade 12 - File - Disc
Sistema de agendamento:

O usuário informa nome, idade, data e horário.

Os dados ficam armazenados em um dicionário.

Depois são salvos em um arquivo de texto.

E o programa consegue ler os atendimentos já agendados.

...........................................................
Inputs:

  nome = input("Digite o nome do paciente: ")

    idade = input("Digite a idade do paciente: ")

    data = input("Digite a data do atendimento (dd/mm/aaaa): ")

    horario = input("Digite o horário do atendimento (hh:mm): ")



Menu:



    print("\n=== Sistema de Agendamento - Psicóloga ===")

    print("1. Agendar novo atendimento")

    print("2. Mostrar atendimentos agendados")

    print("3. Sair")
'''

NOME_ARQUIVO = "agendamentos.txt"

def carregar_agendamentos():
    agendamentos = []

    with open(NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                nome, idade, data, horario = linha.split(";")
                agendamento = {
                    "nome": nome,
                    "idade": idade,
                    "data": data,
                    "horario": horario
                }
                agendamentos.append(agendamento)
    return agendamentos

def salvar_agendamentos(agendamentos):
    with open(NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
        for agendamento in agendamentos:
            linha = f"{agendamento['nome']};{agendamento['idade']};{agendamento['data']};{agendamento['horario']}\n"
            arquivo.write(linha)

def agendar_novo_atendimento(lista_de_agendamentos):
    print("\n--- Novo Agendamento ---")
    nome = input("Digite o nome do paciente: ")
    idade = input("Digite a idade do paciente: ")
    data = input("Digite a data do atendimento (dd/mm/aaaa): ")
    horario = input("Digite o horário do atendimento (hh:mm): ")

    novo_agendamento = {
        "nome": nome,
        "idade": idade,
        "data": data,
        "horario": horario
    }

    lista_de_agendamentos.append(novo_agendamento)
    salvar_agendamentos(lista_de_agendamentos)
    print("\n>>> Atendimento agendado com sucesso! <<<")

def mostrar_atendimentos_agendados(lista_de_agendamentos):
    print("\n--- Atendimentos Agendados ---")
    if not lista_de_agendamentos:
        print("Nenhum atendimento agendado no momento.")
    else:
        for i, agendamento in enumerate(lista_de_agendamentos, start=1):
            print(f"{i}. Paciente: {agendamento['nome']}")
            print(f"   Idade: {agendamento['idade']}")
            print(f"   Data: {agendamento['data']}")
            print(f"   Horário: {agendamento['horario']}")
            print("-" * 25)


if __name__ == "__main__":
    atendimentos = carregar_agendamentos()

    while True:
        print("\n=== Sistema de Agendamento - Psicóloga ===")
        print("1. Agendar novo atendimento")
        print("2. Mostrar atendimentos agendados")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            agendar_novo_atendimento(atendimentos)
        elif escolha == '2':
            mostrar_atendimentos_agendados(atendimentos)
        elif escolha == '3':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")