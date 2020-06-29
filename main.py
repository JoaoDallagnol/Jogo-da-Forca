import os
import time
from funções.registro import cadastro
from funções.menu import menu_desafiante, opções_competidor
from funções.resultado import resultado
from funções.escolhas import opcao, alternativa

os.system("cls")
cadastro()
arquivo = open("loginforca.txt","r")
desafiante = arquivo.readline()
competidor = arquivo.readline()
arquivo.close()
while True:
    os.system("cls")
    print("O Desafiante é: ",desafiante)
    print("O Competidor é: ",competidor)
    menu_desafiante()
    repetição = []
    erro = 0
    op = opcao()
    if op == "0":
        os.system("cls")
        palavra_chave = input("Desafiante digite a palavra chave: ")
        palavra_escondida = list("*" * len(palavra_chave))
        palavra_lista = (list(palavra_chave))
        print(palavra_escondida)
        

        dica1 = input("Desafiante digite a primeira dica: ")
        dica2 = input("Desafiante digite a segunda dica: ")
        dica3 = input("Desafiante digite a terceira dica: ")
        lista_dica = [dica1, dica2, dica3]
        dica = 0

        while True:
            os.system("cls")
            opções_competidor()
            op = opcao()
            if op == "0":
                print(palavra_escondida)
                letra = alternativa()
                if letra in palavra_chave and letra not in repetição and erro <= 5:
                    print("Você acertou essa letra!!")
                    for i in range(0, len(palavra_escondida)):
                        if letra in palavra_chave[i]:
                            palavra_escondida[i] = letra

                            print(palavra_escondida)
                            time.sleep(2)
                    if palavra_escondida == palavra_lista:
                        print("Você acertou a palavra!!")
                        vencedor = competidor
                        perdedor = desafiante
                        resultado(vencedor, perdedor, palavra_chave)
                        time.sleep(4)
                        break

                elif letra in repetição:
                    print("Você ja tentou essa letra!!")
                    time.sleep(3)
                    
                elif erro == 5:
                    print("Você perdeu!!")
                    vencedor = desafiante
                    perdedor = competidor
                    resultado(vencedor, perdedor, palavra_chave)
                    time.sleep(3)
                    break
                else:
                    erro = erro + 1
                    repetição.append(letra)
                    print("Você errou a letra !!")
                    print(f"Você tem {erro} erro(s), max de 5")
                    time.sleep(3)
                
            elif op == "1":
                dica = dica + 1
                if dica <=3:
                    for i in range(0, dica):
                        lista_dicafinal = lista_dica[i]
                    print(f"A dica é: {lista_dicafinal}")
                    time.sleep(3)
                else:
                    print("Suas dicas acabaram, tente chutar uma alternativa")
                    time.sleep(3)
                
            elif op == "2":
                break
            else:
                print("Opção Inválida, Tente novamente")
                time.sleep(3)
    elif op == "1":
        break
    elif op == "2":
        os.remove("loginforca.txt")
        break
    else:
        print("Opção Inválida, Tente Novamente")
print("Volte Sempre")