import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    #random.seed(100)

    num_aleatorio = random.random() * 100
    numero_secreto = round(num_aleatorio)

    #ou podemos gerar assim

    numero_secreto = random.randrange(1, 101)

    print(numero_secreto)

    #### Adicionando dificuldade
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    rodada = 1

    #### Adicionando pontuação

    pontos = 1000

    #### Usando While

    # while (rodada <= total_de_tentativas):
    #     print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    #     chute_str = input("Digite o seu número: ")
    #     chute = int(chute_str)
    #
    #     acertou = chute == numero_secreto
    #     maior = chute > numero_secreto
    #     menor = chute < numero_secreto
    #
    #     if (acertou):
    #         print("Você acertou!")
    #     else:
    #         if (maior):
    #             print("Você errou! O seu chute foi maior que o número secreto.")
    #         elif (menor):
    #             print("Você errou! O seu chute foi menor que o número secreto.")
    #
    #     rodada = rodada + 1

    #### Usando For

    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número: ")
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            print(f"Você fez {pontos} pontos!")
            break

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1


    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()