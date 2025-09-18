# Exercício 1**: Crie um arquivo `produtos.csv` que armazene o nome e preço de produtos. Depois, faça um programa que leia esse arquivo e calcule o preço médio. 

'''
file = open('produtos.csv', 'w')
file.write('Arroz,20.5\n')
file.write('Feijão,7.8\n')
file.write('Macarrão,5.4\n')
file.close()

def calcular_preco_medio():
    total = 0
    count = 0
    file = open('produtos.csv', 'r')

    for linha in file.readlines():
        nome, preco = linha.strip().split(',')
        total += float(preco)
        count += 1
    if count == 0:
        return 0
    return total / count

preco_medio = calcular_preco_medio()
print(f"{preco_medio:.2f}")
'''

# Exercício 2**: Usando JSON, crie um arquivo `inventario.json` que armazene produtos e quantidades de uma loja. Crie funções para adicionar um produto, remover um produto e listar todos os produtos. 3. 

'''
def adicionar_produto(nome, quantidade):
    f_leitura = open('inventario.json', 'r')
    inventario_dict = json.load(f_leitura)
    f_leitura.close()

    inventario_dict[nome] = quantidade
    
    f_escrita = open('inventario.json', 'w')
    json.dump(inventario_dict, f_escrita, indent=4)
    f_escrita.close()
    
    print(f"Produto '{nome}' adicionado/atualizado.")

def remover_produto(nome):
    f_leitura = open('inventario.json', 'r')
    inventario_dict = json.load(f_leitura)
    f_leitura.close()

    if nome in inventario_dict:
        del inventario_dict[nome]
        
        f_escrita = open('inventario.json', 'w')
        json.dump(inventario_dict, f_escrita, indent=4)
        f_escrita.close()
        
        print(f"Produto '{nome}' removido.")
    else:
        print(f"Erro: Produto '{nome}' não encontrado no inventário.")

def listar_produtos():
    f = open('inventario.json', 'r')
    inventario_dict = json.load(f)
    f.close()
    
    print("\n--- Inventário da Loja ---")
    for nome_produto, qtd in inventario_dict.items():
        print(f"- {nome_produto}: {qtd} unidades")
    print("------------------------\n")

adicionar_produto('Maçã', 50)
adicionar_produto('Banana', 75)
listar_produtos()
remover_produto('Maçã')
listar_produtos()
'''

# Exercício 3**: Leia um arquivo de texto `diario.txt` e conte o número de palavras nele. Adicione uma função que, ao rodar, acrescente a data e o total de palavras no final do arquivo.
'''
diario = open('diario.txt', 'w')
diario.write("Hoje foi um dia produtivo. Consegui terminar meu projeto de programação.\n")
diario.close()

diario = open('diario.txt', 'r')

def contar_palavras():
    conteudo = diario.read()
    palavras = conteudo.split()
    return len(palavras)

total_palavras = contar_palavras()
print(f"Número total de palavras no diário: {total_palavras}")
diario.close()
'''