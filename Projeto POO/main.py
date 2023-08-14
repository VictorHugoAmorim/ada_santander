from cadastra_cliente import *


def sys():

    while True:
        print('1- Cadastrar cliente\n2- Alterar cadastro de cliente\n3- Consultar clientes cadastrados',sep='')
        print('4- Cadastrar medicamento\n5- Alterar cadastro de medicamento\n6- Consultar medicamentos cadastrados\n0- Sair')
        user_choice = input('Por favor, escolha o número da ação desejada: ')
        if user_choice == '0':
            break
        elif user_choice in ['1','2','3','4','5']:    
            #Case 1
            if user_choice == '1':
                Cadastro.exec()
            
            #Continuar a partir daqui
        break

if __name__ == '__main__':
    sys()