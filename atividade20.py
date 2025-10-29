import os

class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

    def __str__(self):
        return f"Tarefa: {self.titulo} - {self.descricao}"

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, descricao):
        tarefa = Tarefa(titulo, descricao)
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(self.tarefas, 1):
                print(f"{i}. {tarefa}")

def menu():
    gerenciador = GerenciadorTarefas()
    while True:
        print("Menu:")
        print("1 - Adicionar nova tarefa")
        print("2 - Listar todas as tarefas")
        print("3 - Sair do programa")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            gerenciador.adicionar_tarefa(titulo, descricao)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcao == '2':
            gerenciador.listar_tarefas()
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcao == '3':
            break
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

menu()