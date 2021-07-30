from random import randint
from time import sleep

while True:
    print("by: Rogy Rulles")
    nm = int(input("Você quer um mar com quanto de matriz: "))
    mt = 0
    mar = list()


    #Def print
    def printmat(ma):
        print("   ", end=' ')
        total = 0
        for d in range(0, nm):
            print(f" {total}", end=' ')
            total += 1
        print()
        for a in range(0, nm):
            print(f"{ma[a]}")
        print("\n\n")

    #Def MAR REAL
    def gereal():
        matriz = list()
        for a in range(0, nm):
            barcos = randint(0, 1)
            matriz.append(barcos)
        return matriz

    while (mt < nm):
        mar.append([mt, gereal()])
        mt += 1



    #MAR FALSO
    marfalso = list()
    nm1 = nm
    mt = 0
    #Def gerador do mar falso
    def gerfalso():
        matriz = list()
        for a in range(0, nm1):
            barcos = 8
            matriz.append(barcos)
        return matriz
    while (mt < nm1):
        marfalso.append([mt, gerfalso()])
        mt += 1

    #print Matriz do mar falso
    printmat(marfalso)



    print(f"\nA matriz do mar tem {len(mar)*nm} posições!!!")
    count = 0

    p2 = 1
    p3 = 0

    for a, b in enumerate(mar):
        for c in enumerate(b[1]):
            if c[1] == 1:
                count += 1

    bomb = count
    barcos = count
    print(f"\n\nTem {count} navios no mar!!! Está pronto para atacalos??? \nVocê tem {bomb} bombas!!!")
    print(f"Você tem que destruir pelo menos 50% dos {count} barcos para ganhar!!!")


    while bomb != 0:
        p1 = int(input("\nDigite a linha da matriz para tentar destruir os navios do inimigo: "))
        p2 = 1
        p3 = int(input("Agora digite a coluna da matriz para tentar destruir os navios do inimigo: "))

        if mar[p1][p2][p3] == 1:
            marfalso[p1][p2][p3] = 1
            count -= 1
            bomb -= 1
            print("\nParabéns você acertou um navio inimigo!!!")
            print(f"Restam {bomb} bombas!!\n")
            printmat(marfalso)
        else:
            bomb -= 1
            marfalso[p1][p2][p3] = 4
            print("\nVocê errou!!!")
            print("Tente novamente")
            print(f"Restam {bomb} bombas\n")
            printmat(marfalso)



    if count != 0:
        mult = count * 100
        porcentagem = mult / barcos

        print(f"\n{porcentagem}")
        if porcentagem >= 50:
            print("Você ganhou Parabens!!!")
            for a in range(0, 5):
                print(f"Saindo em {a} segundos!!")
                sleep(1)
        else:
            print("Você perdeu tente novamente")
            for a in range(0, 5):
                print(f"Saindo em {a} segundos!!")
                sleep(1)

    if count == 0:
        print("Você destruiu todos os navios... Parabens!!!")
        for a in range(0, 5):
            print(f"Saindo em {a} segundos!!")
            sleep(1)
