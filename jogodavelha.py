jogo_velha = [[0,0,0],
                [0,0,0],
                    [0,0,0]]
jogo = jogo_velha

print("By: Rogy Rulles")

def V_H():
    #Linhas
    if jogo[0][0] == jogo[0][1] == jogo[0][2] == 0:
        return 0
    elif jogo[0][0] == jogo[0][1] == jogo[0][2]:
        print("\nDeu velha na linha UM!!!")
        return 1


    if jogo[1][0] == jogo[1][1] == jogo[1][2] == 0:
        return 0
    elif jogo[1][0] == jogo[1][1] == jogo[1][2]:
        print("\nDeu velha na linha DOIS!!!")
        return 1


    if jogo[2][0] == jogo[2][1] == jogo[2][2] == 0:
        return 0
    elif jogo[2][0] == jogo[2][1] == jogo[2][2]:
        print("\nDeu velha na linha TRÊS!!!")
        return 1


    #Colunas
    if jogo[0][0] == jogo[1][0] == jogo[2][0] == 0:
        return 0
    elif jogo[0][0] == jogo[1][0] == jogo[2][0]:
        print("\nDeu velha na coluna UM!!!")
        return 1

    if jogo[0][1] == jogo[1][1] == jogo[2][1] == 0:
        return 0
    elif jogo[0][1] == jogo[1][1] == jogo[2][1]:
        print("\nDeu velha na coluna DOIS!!!")
        return 1

    if jogo[0][1] == jogo[1][1] == jogo[2][1] == 0:
        return 0
    elif jogo[0][1] == jogo[1][1] == jogo[2][1]:
        print("\nDeu velha na coluna TRÊS!!!")
        return 1

    #Diagonal
    if jogo[0][0] == jogo[1][1] == jogo[2][2] == 0:
        return 0
    elif jogo[0][0] == jogo[1][1] == jogo[2][2]:
        print("\nDeu velha na diagonal na diagonal  \  !!!")
        return 1

    if jogo[0][2] == jogo[1][1] == jogo[2][0] == 0:
        return 0
    if jogo[0][2] == jogo[1][1] == jogo[2][0]:
        print("\nDeu velha na diagonal na diagonal  /  !!!")
        return 1


verificado = 0


def inp(ver):
    while ver != 1:
        for pa in range(1, 3):
            if pa == 1:
                while True:
                    print(f"\nPlayer 1! Deseja colocar o número em qual posição? Sendo: \n"
                          "   0 1 2\n"
                          f"0 [{jogo[0][0]},{jogo[0][1]},{jogo[0][2]}]\n"
                            f"1 [{jogo[1][0]},{jogo[1][1]},{jogo[1][2]}]\n"
                            f"2 [{jogo[2][0]},{jogo[2][1]},{jogo[2][2]}]\n")
                    n1 = int(input("Qual a linha? 0, 1 ou 2: "))
                    n2 = int(input("Qual a coluna? 0, 1 ou 2: "))
                    if jogo[n1][n2] != 0:
                        print(f"Player 1 tente novamente!! A posição {n1} e {n2} já esta ocupada...")
                    if jogo[n1][n2] == 0:
                        jogo[n1][n2] = 1
                        break
                ver = V_H()
                if ver == 1:
                    break

            if pa == 2:
                while True:
                    print("\n\nPlayer 2! Deseja colocar o número em qual posição? Sendo: \n"
                          "   0 1 2\n"
                          f"0 [{jogo[0][0]},{jogo[0][1]},{jogo[0][2]}]\n"
                            f"1 [{jogo[1][0]},{jogo[1][1]},{jogo[1][2]}]\n"
                            f"2 [{jogo[2][0]},{jogo[2][1]},{jogo[2][2]}]\n")
                    n1 = int(input("Qual a linha? 0, 1 ou 2: "))
                    n2 = int(input("Qual a coluna? 0, 1 ou 2: "))
                    if jogo[n1][n2] != 0:
                        print(f"Player 2 tente novamente!! A posição {n1} e {n2} já esta ocupada...")
                    if jogo[n1][n2] == 0:
                        jogo[n1][n2] = 2
                        break
                ver = V_H()
                if ver == 1:
                    break


inp(verificado)

print(""
                      "   0 1 2\n"
                      f"0 [{jogo[0][0]},{jogo[0][1]},{jogo[0][2]}]\n"
                        f"1 [{jogo[1][0]},{jogo[1][1]},{jogo[1][2]}]\n"
                        f"2 [{jogo[2][0]},{jogo[2][1]},{jogo[2][2]}]\n")


