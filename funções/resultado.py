def resultado(vencedor, perdedor, palavra_chave):
    try:
        historico = open("histórico.txt","a")
        historico.write("Palavra = " + palavra_chave + "\n")
        historico.write("O vencedor foi " + vencedor + "\n")
        historico.write("O perdedor foi " + perdedor + "\n")
        historico.write("\n")
        historico.close()

    except:
        historico = open("histórico.txt","w")
        historico.write("Palavra = " + palavra_chave + "\n")
        historico.write("O vencedor foi " + vencedor + "\n")
        historico.write("O perdedor foi " + perdedor + "\n")
        historico.write("\n")
        historico.close()
