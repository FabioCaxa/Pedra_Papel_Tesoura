import os
import random

print("======================")
print("Pedra, Papel e Tesoura")
print("======================")

placar_jogador = 0
placar_computador = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\nPlacar:  \nJogador:{placar_jogador} - Computador:{placar_computador}")
    print("\nEscolha uma opção:")
    print("| 0 - Pedra | 1- Papel | 2- Tesoura |")
    try:
        escolha_jogador = int(input())
    except ValueError:
        print("Entrada inválida. Por favor, escolha apenas 0, 1 ou 2.")
        continue

    escolha_computador = random.randint(0, 2)

    if escolha_jogador == 0:
        print("Você escolheu Pedra")
        if escolha_computador == 0:
            print("O computador escolheu Pedra")
            print("Empate")
        elif escolha_computador == 1:
            print("O computador escolheu Papel")
            print("O computador Venceu!")
            placar_computador += 1
        else:
            print("O computador escolheu Tesoura")
            print("Você venceu!")
            placar_jogador += 1

    elif escolha_jogador == 1:
        print("Você escolheu Papel")
        if escolha_computador == 0:
            print("O computador escolheu Pedra")
            print("Você venceu!")
            placar_jogador += 1
        elif escolha_computador == 1:
            print("O computador escolheu Papel")
            print("Empate")
        else:
            print("O computador escolheu Tesoura")
            print("O computador Venceu!")
            placar_computador += 1

    elif escolha_jogador == 2:
        print("Você escolheu Tesoura")
        if escolha_computador == 0:
            print("O computador escolheu Pedra")
            print("O computador Venceu!")
            placar_computador += 1
        elif escolha_computador == 1:
            print("O computador escolheu Papel")
            print("Você venceu!")
            placar_jogador += 1
        else:
            print("O computador escolheu Tesoura")
            print("Empate")

    else:
        print("Valor incorreto. Por favor, utilize apenas 0, 1 ou 2")
        continue

    print(f"\nPlacar:  \nJogador:{placar_jogador} - Computador:{placar_computador}")

    print("\nGostaria de Jogar novamente?")
    print("| 0 - Sim | 1 - Não |")
    while True:
        try:
            continuar = int(input("Escolha 0 para Sim ou 1 para Não: "))
            if continuar == 0:
                break
            elif continuar == 1:
                print("\nFim do Jogo!")
                exit()
            else:
                print("Valor incorreto, por favor utilize 0 ou 1")
        except ValueError:
            print("Entrada inválida. Por favor, escolha apenas 0 ou 1.")
            continue