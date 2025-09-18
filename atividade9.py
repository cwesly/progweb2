""" 1. criar uma atividade em Python simulando o Jogo da Mega-Sena usando a biblioteca random. O jogo consiste em gerar 6 números aleatórios e o usuário deverá tentar adivinhar quais são esses números.

Passo a Passo:
Gerar os Números Sorteados: Vamos gerar 6 números aleatórios entre 1 e 60 (como na Mega-Sena).
Receber os Números do Usuário: O usuário escolherá 6 números para tentar adivinhar os sorteados.
Comparar os Números: Vamos comparar os números escolhidos pelo usuário com os números sorteados.
Exibir o Resultado: O programa dirá quantos acertos o usuário teve. """
import random

def sorteio():
    while len(vetor_sorteado) < 6:
        numero = random.randint(1, 60)
        if numero not in vetor_sorteado:
            vetor_sorteado.append(numero)
    vetor_sorteado.sort()
    print("Números sorteados:", vetor_sorteado)

def acertos():
    acertos = 0
    for numero in vetor_usuario:
        if numero in vetor_sorteado:
            acertos += 1
    
    if acertos == 6:
        print("Parabéns! Você acertou todos os números e ganhou o prêmio máximo!")
    
    print(f"Você teve {acertos} acerto(s).")


vetor_sorteado = []
vetor_usuario = [1,2,8,50,30,45]

sorteio()
acertos()