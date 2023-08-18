from cadastra_cliente import *
from cadastra_cliente import Cadastro
from medicamentos import *
from medic_quimio import *
from medic_fit import *
from laboratorio import *
from vendas import *
from lendocsv import lendo_csv

def sys():
    lendo_csv()
    while True:
        print('1- Cadastrar cliente\n2- Alterar cadastro de cliente\n3- Consultar clientes cadastrados',sep='')
        print('4- Cadastrar medicamento\n5- Alterar cadastro de medicamento\n6- Consultar medicamentos cadastrados\n0- Sair')
        user_choice = input('Por favor, escolha o número da ação desejada:\n ')
        if user_choice == '0':
            print("Encerrando o programa...")
            break
        elif user_choice in ['1','2','3','4','5','6','0']:    
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
            elif user_choice == '4': # Cadastrar medicamento
                try:
                    print('1 - Cadastrar medicamento fitoterápico\n2 - Cadastrar medicamento quimioterápico')
                    user_choice_medic = input('Por favor, escolha o número da ação desejada:\n ')
                    if user_choice_medic =='1':
                        pass
                    elif user_choice_medic =='2':
                        pass
                    else:
                        print("Opção inexistente")
                except:
                    print('Impossivel, nenhum cadastro encontrado!\n')

            elif user_choice == '6': #Listar medicamentos cadastrados
                try:
                    print('1 - Listar todos os medicamentos cadastrados\n2 - Listar medicamentos fitoterápicos cadastrados\n3 - Listar medicamentos quimioterápicos cadastrados')
                    user_choice_listamedic = input('Por favor, escolha o número da ação desejada:\n ')
                    if user_choice_listamedic =='1':
                        print(sorted(Medicamentos.lista_medicamentos, key=lambda med:med.nome))
                    elif user_choice_listamedic =='2':
                        print(sorted(MedicFit.lista_fit, key=lambda med:med.nome))
                    elif user_choice_listamedic =='3':
                        print(sorted(MedicQuimio.lista_quimio, key=lambda med:med.nome))
                    else:
                        print("Opção inexistente")
                except:
                    print('Impossivel, nenhum cadastro encontrado!\n')
            
            #Continuar a partir daqui
        

if __name__ == '__main__':
    sys()