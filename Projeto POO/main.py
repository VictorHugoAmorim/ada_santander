from cadastra_cliente import *
from cadastra_cliente import Cadastro


def sys():

    while True:
        print('1- Cadastrar cliente\n2- Alterar cadastro de cliente\n3- Consultar clientes cadastrados',sep='')
        print('4- Cadastrar medicamento\n5- Alterar cadastro de medicamento\n6- Consultar medicamentos cadastrados\n0- Sair')
        user_choice = input('Por favor, escolha o número da ação desejada:\n ')
        if user_choice == '0':
            break
        elif user_choice in ['1','2','3','4','5']:    
            #Case 1
            if user_choice == '1':
                cadastro = Cadastro('','','')
                cadastros_clientes = cadastro.armazena_dados()
            
            elif user_choice == '2':
                try:
                    cadastro.altera_cliente(cadastros_clientes)
                except:
                    print('Impossivel, nenhum cadastro encontrado!\n')
            elif user_choice == '3':
                try:
                    cadastro.exibe_clientes(cadastros_clientes)
                except:
                    print('Impossivel, nenhum cadastro encontrado!\n')
            #Continuar a partir daqui
        

if __name__ == '__main__':
    sys()