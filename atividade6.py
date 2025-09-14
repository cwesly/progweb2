#1. Crie uma função chamada calcular_media que recebe três notas como parâmetros e retorna a média dessas notas.
'''
def calcular_media(*args):
    return sum(args)

numero_1 = 80
numero_2 = 10
numero_3 = 90

print(calcular_media(numero_1, numero_2, numero_3))
'''
#2.  Escreva uma função chamada contar_pares que receba um número n como parâmetro e retorne a quantidade de números pares de 0 até n
'''
def contar_pares(numero_ate_pares):
    for i in range(0, numero_ate_pares+1, 2):
        print(i, end=" ")

numero_pares = 9
contar_pares(numero_pares)
'''
#3.  Crie uma função chamada calculadora que receba três argumentos:
#num1 (número)
#num2 (número)
#operacao (string: "soma", "subtracao", "multiplicacao", "divisao")
'''
def calculadora(numero_1, numero_2, operacao):
    if operacao == "soma":
        return numero_1 + numero_2
    elif operacao == "subtracao":
        return numero_1 - numero_2
    elif operacao == "multiplicacao":
        return numero_1 * numero_2
    elif operacao == "divisao":
        return numero_1 / numero_2
    else:
        return "Operação inválida"

numero_1 = 15
numero_2 = 5
operacao = "divisao"

print(calculadora(numero_1, numero_2, operacao))
'''

#4.  Crie uma função chamada estatisticas que receba qualquer quantidade de números usando *args.
#A função deve retornar um dicionário contendo:
#"soma" → soma de todos os números
#"media" → média dos números
#"maior" → maior número
#"menor" → menor número
'''
def estatisticas(*args):
    soma = sum(args)
    
    quantidade_numeros = len(args)
    media = soma / quantidade_numeros

    maior_numero = max(args)
    menor_numero = min(args)

    return {
        "Soma": soma,
        "Media": media,
        "Maior": maior_numero,
        "Menor": menor_numero
    }

print(estatisticas(48,56,92,18))
'''