from Class.Arquivos import Arquivos
from time import sleep
from Utils.limparTerminal import limpar_terminal

arquivos = Arquivos()

while(True): 
    limpar_terminal()
    print("""
    Selecione uma opção:
    [1] - Criar Arquivos
    [2] - Organizar Arquivos
    [3] - Deletat Todos os arquivos
    [4] - Sair do sistema
    """)
    option = int(input(""))

    if (option == 1):
        limpar_terminal()
        sleep(2)
        qtd = int(input("Qual a quantidade de arquivos que deseja criar: "))
        print("Cricando os arquivos e diretórios...")
        arquivos.criarArquivos(qtd)
        sleep(2)
    elif (option == 2):
        limpar_terminal()
        sleep(2)
        print("Organizando os arquivos em seus diretórios respectivos...")
        arquivos.organizarArquivos()
        sleep(2)
    elif (option == 3):
        limpar_terminal()
        sleep(2)
        print("Você deseja deletar todos os arquivos? Digite [S] ou [N]")
        confirmation = str(input())

        if (confirmation.upper() == "S"):
            print("Deletando...")
            arquivos.deletarTudo()
            sleep(2)
        elif (confirmation.upper() == "N"):
            continue
        else:
            print("Opção invalida, tente novamente mais tarde...")
            sleep(2)
            continue
    elif(option == 4):
        limpar_terminal()
        sleep(2)
        print("Saindo do sistema...")
        sleep(2)
        break
    else:
        limpar_terminal()
        sleep(2)
        print("Opção invalida...")
        
