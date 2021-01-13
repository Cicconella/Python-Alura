
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "elefante"
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    # Enquanto nao acertou e nao enforcou
    while (not acertou and not enforcou):

        print("Jogando...")

        chute = input("Qual é a letra? ")
        # para remover espacos
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()