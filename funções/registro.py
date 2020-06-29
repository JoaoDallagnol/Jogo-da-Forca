def cadastro():
    try:
        arquivo = open("loginforca.txt","r")
        desafiante = arquivo.readline()
        competidor = arquivo.readline()
        arquivo.close()
    except:
        arquivo = open("loginforca.txt","w")
        desafiante = input("Informe o nome do Desafiante: ")
        competidor = input("Informe o nome do Competidor: ")
        arquivo.write(desafiante + "\n")
        arquivo.write(competidor + "\n")
        arquivo.close()